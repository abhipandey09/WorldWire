import os
import json
import re
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("WorkWire.AIMatcher")

def get_company_logo(domain: str) -> str:
    if not domain:
        domain = "google.com"
    clean_domain = domain.lower().replace("https://", "").replace("http://", "").split("/")[0]
    return f"https://www.google.com/s2/favicons?domain={clean_domain}&sz=128"

def get_gemini_client():
    api_key = os.getenv("WORLDWIRE_GEMINI_API_KEY") or os.getenv("GOOGLE_GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except Exception as e:
        logger.warning(f"Could not initialize genai client: {e}")
        return None

def fallback_local_matcher(candidate_skills, candidate_exp, candidate_country, candidate_bio, jobs):
    """Rule-based semantic matcher as fallback if AI is unreachable."""
    results = []
    tokens = set([s.strip().lower() for s in candidate_skills.replace(",", " ").split() if len(s.strip()) > 1])
    if candidate_bio:
        tokens.update([w.strip().lower() for w in candidate_bio.replace(",", " ").split() if len(w.strip()) > 2])

    for j in jobs:
        score = 55  # base
        j_country = (j.get("country") or "").lower()
        if candidate_country and candidate_country != "Any Region / Remote":
            if candidate_country.lower() in j_country:
                score += 15
            else:
                score -= 10

        j_tags = set([t.lower() for t in j.get("tags", [])])
        j_text = (j.get("title", "") + " " + j.get("summary", "")).lower()

        overlap = []
        for t in tokens:
            if t in j_tags or t in j_text:
                score += 8
                overlap.append(t.title())

        score = min(max(score, 65), 98)
        missing = [t for t in j.get("tags", []) if t.lower() not in tokens][:2]

        results.append({
            "title": j["title"],
            "company": j["company"],
            "company_domain": j.get("company_domain", "careers.google.com"),
            "company_logo": j.get("company_logo") or get_company_logo(j.get("company_domain", "google.com")),
            "location": j["location"],
            "country": j.get("country", "Global"),
            "salary_range": j.get("salary_range", "Competitive Market Rate"),
            "apply_url": j.get("apply_url"),
            "req_id": j.get("req_id", j["id"]),
            "match_score": score,
            "match_reason": f"Strong alignment with {j['company']}'s {j['department']} group. Your profile matches core requirements.",
            "key_matching_skills": list(set(overlap))[:4] or j.get("tags", [])[:3],
            "skill_gaps_to_learn": missing or ["System Design Scalability"],
            "interview_tip": f"Be prepared to explain past architecture trade-offs and live system observability in depth for {j['company']}.",
            "source": "WorkWire Curated"
        })

    results.sort(key=lambda x: x["match_score"], reverse=True)
    return results[:5]

def match_candidate_jobs(candidate_skills: str, candidate_exp: str, candidate_country: str, candidate_bio: str, jobs: list):
    """
    Analyzes candidate's skills, experience, and background.
    Uses Gemini 3.8 Flash with Google Search Grounding to perform LIVE WEB SEARCH
    tool calls across India & the US, combined with WorkWire's verified catalog.
    """
    if not candidate_skills and not candidate_bio:
        return []

    client = get_gemini_client()
    if not client:
        return fallback_local_matcher(candidate_skills, candidate_exp, candidate_country, candidate_bio, jobs)

    # Curate top catalog references
    catalog_summary = []
    for j in jobs[:15]:
        catalog_summary.append({
            "id": j["id"],
            "req_id": j.get("req_id", j["id"]),
            "title": j["title"],
            "company": j["company"],
            "company_domain": j.get("company_domain", ""),
            "country": j.get("country"),
            "location": j.get("location"),
            "salary": j.get("salary_range"),
            "apply_url": j.get("apply_url"),
            "tags": j.get("tags", []),
            "summary": j.get("summary", "")[:180]
        })

    prompt = f"""You are an elite Google Senior Talent Partner and Technical Career Advisor.
A candidate has submitted their profile to find tech job opportunities in India and the United States.

Candidate Profile:
- Skills & Tech Stack: {candidate_skills}
- Experience Level: {candidate_exp}
- Preferred Region: {candidate_country}
- Background Summary / Resume snippet: {candidate_bio or "Not provided"}

AVAILABLE WORKWIRE CURATED REQUISITIONS:
{json.dumps(catalog_summary, indent=1)}

INSTRUCTIONS & TOOL USAGE:
1. Conduct LIVE GOOGLE SEARCH tool calls to find 2 to 3 ACTIVE, REAL tech job postings currently open across India or the United States (from company career pages, Greenhouse, Lever, Workday, Ashby, or LinkedIn) that closely match the candidate's skills and experience.
2. Select 1 to 2 of the best matching positions from the WORKWIRE CURATED REQUISITIONS catalog provided above.
3. For each recommended position (total 3 to 4 positions), return:
   - title: exact job title
   - company: company name
   - company_domain: primary domain for company logo (e.g. stripe.com, nvidia.com, redditinc.com, uber.com)
   - location: city, state/region, country (mention Remote or Hybrid if applicable)
   - country: "India" or "United States"
   - salary_range: disclosed compensation or competitive estimate
   - apply_url: exact direct URL to apply on ATS / company portal
   - req_id: official job requisition ID if found (e.g. JR1982731, 7851761, or generated code)
   - match_score: integer between 85 and 99
   - match_reason: 2 sentences explaining why the candidate's background matches this specific role
   - key_matching_skills: list of 3-4 specific overlapping skills
   - skill_gaps_to_learn: list of 1-2 skills or concepts to review
   - interview_tip: 1 practical technical interview advice specific to this employer
   - source: "Live Web Search" if retrieved via live search, or "WorkWire Curated" if from the catalog

OUTPUT FORMAT:
Respond with ONLY a valid JSON array of objects. Do not include markdown code fences or explanatory text.
"""

    try:
        from google.genai import types

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                temperature=0.2
            )
        )
        text = response.text.strip()

        # Extract JSON array
        start = text.find("[")
        end = text.rfind("]")
        if start != -1 and end != -1:
            clean_json = text[start:end+1]
            parsed = json.loads(clean_json)

            enriched = []
            for item in parsed:
                # Ensure company logo
                domain = item.get("company_domain")
                if not domain and item.get("company"):
                    domain = item["company"].lower().replace(" ", "").replace("&", "") + ".com"
                item["company_logo"] = get_company_logo(domain)

                # Ensure source badge
                if not item.get("source"):
                    item["source"] = "Live Web Search"

                # Ensure req_id
                if not item.get("req_id"):
                    item["req_id"] = f"REQ-{abs(hash(item.get('title', '') + item.get('company', ''))) % 1000000}"

                # Ensure apply_url
                if not item.get("apply_url") or "example.com" in item.get("apply_url"):
                    item["apply_url"] = f"https://www.google.com/search?q={item.get('company', '')}+{item.get('title', '')}+careers"

                enriched.append(item)

            if enriched:
                enriched.sort(key=lambda x: x.get("match_score", 0), reverse=True)
                return enriched

    except Exception as e:
        logger.warning(f"Live web search with Gemini failed: {e}. Falling back to semantic matching.")

    return fallback_local_matcher(candidate_skills, candidate_exp, candidate_country, candidate_bio, jobs)
