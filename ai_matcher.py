import os
import json
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("WorkWire.AIMatcher")

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
        score = 50  # base
        j_country = (j.get("country") or "").lower()
        if candidate_country and candidate_country != "Any Location":
            if candidate_country.lower() in j_country:
                score += 15
            else:
                score -= 20

        j_tags = set([t.lower() for t in j.get("tags", [])])
        j_text = (j.get("title", "") + " " + j.get("summary", "")).lower()

        overlap = []
        for t in tokens:
            if t in j_tags or t in j_text:
                score += 10
                overlap.append(t.title())

        score = min(max(score, 35), 98)
        missing = [t for t in j.get("tags", []) if t.lower() not in tokens][:2]

        results.append({
            "job_id": j["id"],
            "title": j["title"],
            "company": j["company"],
            "location": j["location"],
            "country": j.get("country", "Global"),
            "salary_range": j.get("salary_range", "Competitive"),
            "apply_url": j.get("apply_url"),
            "req_id": j.get("req_id", j["id"]),
            "match_score": score,
            "match_reason": f"Strong alignment with {j['company']}'s {j['department']} group. Your background directly touches core requirements.",
            "key_matching_skills": list(set(overlap))[:4] or j.get("tags", [])[:2],
            "skill_gaps_to_learn": missing or ["System Design Scalability"],
            "interview_tip": f"Be prepared to explain past architecture trade-offs and live system observability in depth for {j['company']}."
        })

    results.sort(key=lambda x: x["match_score"], reverse=True)
    return results[:5]

def match_candidate_jobs(candidate_skills: str, candidate_exp: str, candidate_country: str, candidate_bio: str, jobs: list):
    """
    Analyzes candidate's skills, experience, and bio using Gemini 3.8 Flash,
    comparing against active verified jobs to recommend the best career matches.
    """
    if not candidate_skills and not candidate_bio:
        return []

    client = get_gemini_client()
    if not client:
        return fallback_local_matcher(candidate_skills, candidate_exp, candidate_country, candidate_bio, jobs)

    # Prepare compact representation of available jobs
    catalog_summary = []
    for j in jobs[:30]:
        catalog_summary.append({
            "id": j["id"],
            "req_id": j.get("req_id", j["id"]),
            "title": j["title"],
            "company": j["company"],
            "country": j.get("country"),
            "location": j.get("location"),
            "department": j.get("department"),
            "experience_level": j.get("experience_level"),
            "salary": j.get("salary_range"),
            "tags": j.get("tags", []),
            "summary": j.get("summary", "")
        })

    prompt = f"""You are an elite Google Senior Talent Partner and Technical Career Advisor.
A candidate has submitted their career profile to find the best tech job matches in India and the United States.

Candidate Profile:
- Skills & Tech Stack: {candidate_skills}
- Experience Level: {candidate_exp}
- Preferred Region: {candidate_country}
- Background Summary / Resume snippet: {candidate_bio or "Not provided"}

Available Active Verified Openings:
{json.dumps(catalog_summary, indent=1)}

TASK:
Select the TOP 3 to 4 best matching positions for this candidate from the catalog above.
For each selected position, calculate an authentic Match Score (from 60% to 99%), write a sharp technical rationale on why they match, highlight overlapping skills, identify 1-2 skills gaps, and provide 1 practical interview preparation tip for that employer.

Respond STRICTLY with a valid JSON array of objects with the following schema:
[
  {{
    "job_id": "job-101",
    "match_score": 94,
    "match_reason": "Specific rationale explaining candidate alignment...",
    "key_matching_skills": ["Skill1", "Skill2"],
    "skill_gaps_to_learn": ["Gap1", "Gap2"],
    "interview_tip": "Specific technical interview advice for this company..."
  }}
]
Do not wrap in backticks or markdown, output ONLY the raw JSON array.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )
        text = response.text.strip()
        # Clean any accidental markdown backticks
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

        parsed = json.loads(text)
        # Hydrate with full job details
        enriched = []
        jobs_map = {j["id"]: j for j in jobs}
        for item in parsed:
            j_id = item.get("job_id")
            if j_id in jobs_map:
                job_ref = jobs_map[j_id]
                item["title"] = job_ref["title"]
                item["company"] = job_ref["company"]
                item["location"] = job_ref["location"]
                item["country"] = job_ref.get("country", "Global")
                item["salary_range"] = job_ref.get("salary_range", "Competitive")
                item["apply_url"] = job_ref.get("apply_url")
                item["req_id"] = job_ref.get("req_id", j_id)
                enriched.append(item)

        if enriched:
            enriched.sort(key=lambda x: x.get("match_score", 0), reverse=True)
            return enriched
    except Exception as e:
        logger.warning(f"Gemini matching failed or parse error: {e}. Falling back to semantic matching.")

    return fallback_local_matcher(candidate_skills, candidate_exp, candidate_country, candidate_bio, jobs)
