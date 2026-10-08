import os
import json
import base64
import io
import re
import logging
from datetime import datetime, timezone
from PIL import Image
from dotenv import load_dotenv
from google import genai
from google.genai import types

import database

load_dotenv()
logger = logging.getLogger("WorldWire.NewsAgent")
logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

def get_gemini_client():
    if not API_KEY:
        raise ValueError("Google Gemini API key not found in environment (.env)")
    return genai.Client(api_key=API_KEY)

def optimize_image_bytes(raw_bytes: bytes, max_width: int = 1000, quality: int = 85) -> str:
    """Resize and compress image to JPEG base64 data URI to save DB space and speed up loading."""
    try:
        img = Image.open(io.BytesIO(raw_bytes))
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Calculate aspect ratio
        width, height = img.size
        if width > max_width:
            new_height = int((max_width / width) * height)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality, optimize=True)
        b64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/jpeg;base64,{b64_str}"
    except Exception as e:
        logger.warning(f"Error optimizing image bytes: {e}")
        b64_str = base64.b64encode(raw_bytes).decode("utf-8")
        return f"data:image/png;base64,{b64_str}"

def get_fallback_image(category: str, title: str) -> str:
    """Provide a reliable, high-resolution royalty-free editorial image matching the topic."""
    category_images = {
        "Technology": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80",
        "Politics": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=1200&q=80",
        "Economy": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1200&q=80",
        "Science": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?auto=format&fit=crop&w=1200&q=80",
        "Climate": "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?auto=format&fit=crop&w=1200&q=80",
        "Geopolitics": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80",
        "World": "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?auto=format&fit=crop&w=1200&q=80",
        "Culture": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?auto=format&fit=crop&w=1200&q=80"
    }
    for cat_key, img_url in category_images.items():
        if cat_key.lower() in category.lower():
            return img_url
    return "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=1200&q=80"

def generate_news_image(client, image_prompt: str, category: str, title: str) -> str:
    """Generate an editorial news image using Gemini image model, with robust fallback."""
    logger.info(f"Generating editorial image with prompt: {image_prompt[:100]}...")
    try:
        refined_prompt = (
            f"Editorial photojournalism news wire photo: {image_prompt}. "
            "High resolution, documentary style, realistic lighting, highly detailed, dramatic angle. "
            "No text, no watermarks, no cartoon, photojournalist camera."
        )
        img_response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=refined_prompt
        )
        if img_response.candidates and img_response.candidates[0].content.parts:
            for part in img_response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.data:
                    logger.info("Successfully received AI-generated image bytes.")
                    return optimize_image_bytes(part.inline_data.data)
    except Exception as e:
        logger.warning(f"AI image generation encountered an issue ({e}). Using editorial image fallback.")
    
    return get_fallback_image(category, title)

def fetch_and_publish_news(target_category: str = None) -> dict:
    """
    Fetch the latest hot topic world news using Gemini with Google Search,
    generate or assign an image, and store in Neon PostgreSQL.
    """
    client = get_gemini_client()
    
    # Retrieve past 10 titles to prevent duplicate coverage
    recent_articles = database.get_articles(limit=10)
    existing_titles = [a['title'] for a in recent_articles] if recent_articles else []
    titles_exclusion = "\n".join([f"- {t}" for t in existing_titles])

    category_hint = f"Focus particularly on {target_category} if there is significant breaking news." if target_category else "Can be any top trending world topic (Politics, Economy, Technology, Science, Global Conflicts, Climate, Culture)."

    current_date_str = datetime.now(timezone.utc).strftime("%B %d, %Y")

    prompt = f"""
You are the Chief Global Wire Correspondent for 'WorldWire'.
Current date: {current_date_str}.
Your task is to search for the most significant, latest, breaking or trending global news story happening right now.
{category_hint}

CRITICAL RULES:
1. Use the Google Search tool to find REAL, ACTUAL verified news events happening today or in the last 24-48 hours.
2. DO NOT cover any of the following stories which we have already published:
{titles_exclusion if titles_exclusion else "None yet"}
3. Ensure the story is high impact, factual, and internationally relevant.
4. Output your response STRICTLY as a valid JSON object with the following schema:
{{
  "title": "A compelling, precise journalistic headline (max 100 characters)",
  "summary": "A concise 2-3 sentence executive briefing highlighting what happened and why it matters",
  "content": "A detailed 3-4 paragraph journalistic report covering: Paragraph 1: The breaking development and key facts. Paragraph 2: Historical context, key leaders/stakeholders, statements made. Paragraph 3: Global or regional implications and what to expect next.",
  "category": "World | Politics | Technology | Economy | Science | Climate | Geopolitics",
  "hot_topic_tag": "Breaking News | Trending | Global Wire | Deep Dive | Geopolitical Shift",
  "source_name": "Name of main news agency (e.g. Reuters, AP News, BBC, Bloomberg, AFP)",
  "source_url": "Direct link or publication URL found in search",
  "region": "Affected country or global region (e.g., North America, Western Europe, Asia-Pacific, Middle East, Global)",
  "image_prompt": "Detailed description for an editorial photo depicting this event (e.g., 'Diplomats meeting at the United Nations General Assembly in Geneva with flags', or 'Semiconductor fabrication cleanroom with engineers in suits')"
}}

Output ONLY the raw JSON object. Do not include markdown code block syntax (like ```json).
"""

    logger.info("Querying Gemini 3.8 Flash with Google Search grounding...")
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())]
        )
    )

    raw_text = response.text.strip()
    
    # Strip any markdown fences if model returned them
    raw_text = re.sub(r"^```(?:json)?\s*", "", raw_text, flags=re.MULTILINE)
    raw_text = re.sub(r"\s*```$", "", raw_text, flags=re.MULTILINE)

    # Parse JSON
    try:
        article_data = json.loads(raw_text)
    except json.JSONDecodeError:
        # Fallback regex extraction
        match = re.search(r"(\{.*\})", raw_text, re.DOTALL)
        if match:
            article_data = json.loads(match.group(1))
        else:
            raise ValueError(f"Could not parse valid JSON from Gemini output: {raw_text[:300]}")

    # Check grounding URLs if source_url is empty
    if not article_data.get("source_url") and response.candidates:
        grounding = response.candidates[0].grounding_metadata
        if grounding and grounding.grounding_chunks:
            for chunk in grounding.grounding_chunks:
                if chunk.web and chunk.web.uri:
                    article_data["source_url"] = chunk.web.uri
                    if chunk.web.title and not article_data.get("source_name"):
                        article_data["source_name"] = chunk.web.title
                    break

    if not article_data.get("source_name"):
        article_data["source_name"] = "WorldWire Global Bureau"

    # Generate or fetch image
    image_prompt = article_data.get("image_prompt", article_data.get("title"))
    image_url = generate_news_image(
        client, 
        image_prompt, 
        article_data.get("category", "World"), 
        article_data.get("title", "")
    )
    article_data["image_url"] = image_url

    # Prepare for database insertion
    db_payload = {
        "title": article_data.get("title"),
        "summary": article_data.get("summary"),
        "content": article_data.get("content"),
        "category": article_data.get("category", "World"),
        "hot_topic_tag": article_data.get("hot_topic_tag", "Trending"),
        "image_url": image_url,
        "source_name": article_data.get("source_name", "WorldWire Intel"),
        "source_url": article_data.get("source_url", ""),
        "region": article_data.get("region", "Global"),
        "published_at": datetime.now(timezone.utc)
    }

    inserted = database.insert_article(db_payload)
    if inserted:
        logger.info(f"Successfully published and stored article: '{db_payload['title']}'")
    else:
        logger.warning(f"Article with title '{db_payload['title']}' already existed in DB.")

    return db_payload

if __name__ == "__main__":
    database.init_db()
    result = fetch_and_publish_news()
    print("Published article:", result["title"])

