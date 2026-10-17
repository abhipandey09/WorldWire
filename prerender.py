import os
import re
import shutil
from datetime import datetime, timezone
import streamlit as st_mod
from job_store import get_approved_jobs
from pages_content import ABOUT_PAGE_MD, CONTACT_PAGE_MD, PRIVACY_PAGE_MD, TERMS_PAGE_MD

ADSENSE_META = '<meta name="google-adsense-account" content="ca-pub-6145233805932455">'
ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6145233805932455" crossorigin="anonymous"></script>'
GOATCOUNTER_SCRIPT = '<script data-goatcounter="https://mytomboy360.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'

COMMON_HEAD = f"""
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="/favicon.png">
    {ADSENSE_META}
    {ADSENSE_SCRIPT}
    {GOATCOUNTER_SCRIPT}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;0,900;1,700&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #f8fafc;
            color: #0f172a;
            line-height: 1.6;
        }}
        a {{ color: #2563eb; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .site-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 16px 20px 48px 20px;
        }}
        .top-intel-bar {{
            background: #0f172a;
            color: #e2e8f0;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }}
        .masthead {{
            border-bottom: 2px solid #0f172a;
            padding: 12px 0 16px 0;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .masthead-title {{
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 40px;
            font-weight: 900;
            letter-spacing: -0.5px;
            line-height: 1;
            color: #0f172a;
        }}
        .masthead-sub {{
            font-size: 13px;
            color: #475569;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-top: 6px;
            font-weight: 700;
        }}
        .nav-bar {{
            display: flex;
            gap: 16px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 10px;
            margin-bottom: 24px;
            overflow-x: auto;
            white-space: nowrap;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}
        .nav-bar a {{
            color: #334155;
            padding: 4px 8px;
            border-radius: 4px;
        }}
        .nav-bar a:hover {{
            background: #e2e8f0;
            color: #0f172a;
            text-decoration: none;
        }}
        .site-footer {{
            border-top: 3px solid #2563eb;
            margin-top: 48px;
            padding: 32px 16px 24px 16px;
            text-align: center;
            color: #64748b;
            font-size: 13px;
            background: #ffffff;
            border-radius: 8px;
        }}
        .footer-links {{
            margin-bottom: 14px;
            line-height: 2;
        }}
        .footer-links a {{
            margin: 0 10px;
            font-weight: 600;
            color: #0f172a;
        }}
        .footer-links a:hover {{ color: #2563eb; }}
        .job-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 6px rgba(15,23,42,0.04);
            transition: transform 0.15s ease;
        }}
        .tag-pill {{
            display: inline-block;
            background: #f1f5f9;
            color: #475569;
            font-size: 11px;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 4px;
            margin-right: 6px;
            margin-top: 6px;
        }}
        .apply-btn {{
            display: inline-block;
            background: #2563eb;
            color: #ffffff !important;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}
        .apply-btn:hover {{
            background: #1d4ed8;
            text-decoration: none;
        }}
        @media (max-width: 768px) {{
            .masthead-title {{ font-size: 30px; }}
            .top-intel-bar {{ flex-direction: column; align-items: flex-start; gap: 4px; }}
        }}
    </style>
"""

SCOPED_PRERENDER_CSS = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;0,900;1,700&display=swap" rel="stylesheet">
    <style id="prerender-styles">
        #prerender-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 16px 20px 48px 20px;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            color: #0f172a;
            line-height: 1.6;
        }
        #prerender-container * { box-sizing: border-box; }
        #prerender-container a { color: #2563eb; text-decoration: none; }
        #prerender-container a:hover { text-decoration: underline; }
        #prerender-container .top-intel-bar {
            background: #0f172a;
            color: #e2e8f0;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }
        #prerender-container .masthead {
            border-bottom: 2px solid #0f172a;
            padding: 12px 0 16px 0;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 12px;
        }
        #prerender-container .masthead-title {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 40px;
            font-weight: 900;
            letter-spacing: -0.5px;
            line-height: 1;
            color: #0f172a;
        }
        #prerender-container .masthead-sub {
            font-size: 13px;
            color: #475569;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-top: 6px;
            font-weight: 700;
        }
        #prerender-container .nav-bar {
            display: flex;
            gap: 16px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 10px;
            margin-bottom: 24px;
            overflow-x: auto;
            white-space: nowrap;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        #prerender-container .nav-bar a {
            color: #334155;
            padding: 4px 8px;
            border-radius: 4px;
        }
        #prerender-container .nav-bar a:hover {
            background: #e2e8f0;
            color: #0f172a;
            text-decoration: none;
        }
        #prerender-container .site-footer {
            border-top: 3px solid #2563eb;
            margin-top: 48px;
            padding: 32px 16px 24px 16px;
            text-align: center;
            color: #64748b;
            font-size: 13px;
            background: #ffffff;
            border-radius: 8px;
        }
        #prerender-container .footer-links {
            margin-bottom: 14px;
            line-height: 2;
        }
        #prerender-container .footer-links a {
            margin: 0 10px;
            font-weight: 600;
            color: #0f172a;
        }
        #prerender-container .footer-links a:hover { color: #2563eb; }
        @media (max-width: 768px) {
            #prerender-container .masthead-title { font-size: 30px; }
            #prerender-container .top-intel-bar { flex-direction: column; align-items: flex-start; gap: 4px; }
        }
    </style>
"""

def get_header_html():
    now_str = datetime.now(timezone.utc).strftime("%A, %B %d, %Y")
    return f"""
    <div class="top-intel-bar">
        <div>💼 <b>WORKWIRE CAREER DESK</b> &nbsp;|&nbsp; {now_str}</div>
        <div>CURATED TECH OPPORTUNITIES • INDIA &amp; UNITED STATES</div>
    </div>
    <header class="masthead">
        <div>
            <h1 class="masthead-title"><a href="/" style="color: #0f172a; text-decoration: none;">WORKWIRE</a></h1>
            <div class="masthead-sub">Verified Engineering, AI &amp; Tech Opportunities in India &amp; US</div>
        </div>
        <div style="text-align: right; font-size: 12px; color: #64748b; font-weight: 600;">
            <div style="color: #2563eb; font-weight: 800;">🛡️ 100% HUMAN VETTED POSITIONS</div>
            <div>Publisher: Abhishek Pandey (TechSnapZone)</div>
        </div>
    </header>
    <nav class="nav-bar">
        <a href="/">All Opportunities</a>
        <a href="/about.html">About Bureau</a>
        <a href="/contact.html">Contact Us</a>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms &amp; Safety</a>
    </nav>
    """

def get_footer_html():
    return """
    <footer class="site-footer">
        <div class="footer-links">
            <a href="/">Job Directory</a> |
            <a href="/about.html">About Us</a> |
            <a href="/contact.html">Contact Bureau</a> |
            <a href="/privacy.html">Privacy Policy</a> |
            <a href="/terms.html">Terms of Service</a>
        </div>
        <p>© 2026 <b>WORKWIRE CAREER NETWORK</b> • Published at <b>mytomboy360.com</b> by Abhishek Pandey (TechSnapZone).</p>
        <p style="margin-top: 6px;">Verified Editorial, Employer Disclosures &amp; AdSense Compliance: <a href="mailto:techsnapzone@gmail.com" style="color: #2563eb; font-weight: 700;">techsnapzone@gmail.com</a></p>
    </footer>
    """

def build_prerendered_homepage_html(jobs):
    if not jobs:
        return ""

    cards_html = ""
    for job in jobs:
        clean_id = job["id"].replace("job-", "")
        country_flag = "🇮🇳" if job.get("country") == "India" else "🇺🇸"
        tags_html = "".join([f'<span class="tag-pill">{t}</span>' for t in job.get("tags", [])[:5]])

        cards_html += f"""
        <article class="job-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 22px; margin-bottom: 20px; box-shadow: 0 1px 4px rgba(15,23,42,0.04);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 12px;">
                <div>
                    <span style="font-size: 11px; font-weight: 800; color: #2563eb; text-transform: uppercase; letter-spacing: 0.05em;">
                        {country_flag} {job.get('country', 'GLOBAL').upper()} • {job.get('department', 'ENGINEERING').upper()}
                    </span>
                    <h2 style="font-size: 20px; font-weight: 700; color: #0f172a; margin-top: 4px;">
                        <a href="/job-{clean_id}.html" style="color: #0f172a;">{job['title']}</a>
                    </h2>
                    <div style="font-size: 14px; color: #475569; font-weight: 600; margin-top: 2px;">
                        🏢 {job['company']} &nbsp;•&nbsp; 📍 {job['location']}
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 13px; font-weight: 800; color: #059669; background: #ecfdf5; padding: 4px 10px; border-radius: 4px;">
                        💰 {job.get('salary_range', 'Competitive Rate')}
                    </div>
                    <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">
                        Level: {job.get('experience_level', 'Mid Level')}
                    </div>
                </div>
            </div>

            <p style="font-size: 14px; color: #334155; line-height: 1.5; margin-bottom: 14px;">
                {job.get('summary', '')}
            </p>

            <div style="margin-bottom: 16px;">
                {tags_html}
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 12px; font-size: 12px; color: #64748b;">
                <div>
                    ✅ Verified by Editor Abhishek Pandey
                </div>
                <div>
                    <a href="/job-{clean_id}.html" style="font-weight: 700; color: #2563eb; margin-right: 14px;">View Role Specification →</a>
                    <a href="{job.get('apply_url')}" target="_blank" rel="noopener nofollow" class="apply-btn" style="padding: 6px 14px; font-size: 11px;">Apply on Company Site ↗</a>
                </div>
            </div>
        </article>
        """

    html = f"""
    <div id="prerender-container" class="site-container">
        {get_header_html()}

        <!-- Editorial Hero Notice -->
        <section style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 32px 28px; border-radius: 8px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(15,23,42,0.08);">
            <div style="max-width: 820px;">
                <span style="background: #2563eb; color: #ffffff; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">VERIFIED OPPORTUNITIES DESK</span>
                <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 32px; font-weight: 800; margin: 12px 0 8px 0; line-height: 1.2;">Curated Technology &amp; Leadership Opportunities in India &amp; United States</h2>
                <p style="font-size: 15px; color: #cbd5e1; line-height: 1.6;">
                    Every position listed on WorkWire is reviewed by <b>Abhishek Pandey (TechSnapZone)</b>. We filter out speculative ghost postings, verify direct corporate application endpoints, and highlight transparent salary benchmarks across India and the US tech corridors.
                </p>
            </div>
        </section>

        <!-- Directory Header -->
        <div style="border-bottom: 2px solid #0f172a; padding-bottom: 8px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-end;">
            <h3 style="font-family: 'Playfair Display', Georgia, serif; font-size: 24px; font-weight: 800; color: #0f172a;">Active Verified Positions</h3>
            <span style="font-size: 13px; color: #64748b; font-weight: 600;">Showing {len(jobs)} Vetted Openings</span>
        </div>

        <section>
            {cards_html}
        </section>

        {get_footer_html()}
    </div>
    """
    return html

def build_job_page_html(job):
    job_id = job["id"]
    clean_id = job_id.replace("job-", "")
    title = job["title"]
    company = job["company"]
    location = job.get("location", "India / United States")
    country = job.get("country", "India")
    salary = job.get("salary_range", "Competitive")
    summary = job.get("summary", "")
    description_md = job.get("description", "")
    apply_url = job.get("apply_url", "https://mytomboy360.com")
    posted_iso = job.get("posted_at", datetime.now(timezone.utc).isoformat())
    country_code = "IN" if country == "India" else "US"

    # Convert Markdown-like headers & bullet points into clean semantic HTML
    desc_html = ""
    for line in description_md.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("### "):
            desc_html += f'<h3 style="font-size: 18px; font-weight: 800; color: #0f172a; margin-top: 24px; margin-bottom: 8px;">{line[4:]}</h3>\n'
        elif line.startswith("- "):
            desc_html += f'<li style="font-size: 15px; color: #334155; line-height: 1.6; margin-bottom: 6px; margin-left: 20px;">{line[2:]}</li>\n'
        else:
            desc_html += f'<p style="font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 14px;">{line}</p>\n'

    tags_html = "".join([f'<span class="tag-pill">{t}</span>' for t in job.get("tags", [])])

    schema_json = f"""{{
        "@context": "https://schema.org/",
        "@type": "JobPosting",
        "title": {repr(title)},
        "description": {repr(description_md[:2000])},
        "identifier": {{
            "@type": "PropertyValue",
            "name": {repr(company)},
            "value": {repr(job_id)}
        }},
        "datePosted": {repr(posted_iso[:10])},
        "employmentType": "FULL_TIME",
        "hiringOrganization": {{
            "@type": "Organization",
            "name": {repr(company)},
            "sameAs": {repr(apply_url)}
        }},
        "jobLocation": {{
            "@type": "Place",
            "address": {{
                "@type": "PostalAddress",
                "addressLocality": {repr(location.split(',')[0])},
                "addressCountry": {repr(country_code)}
            }}
        }}
    }}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>{title} at {company} | WorkWire Careers</title>
    <meta name="description" content="{summary[:160]}">
    <link rel="canonical" href="https://mytomboy360.com/job-{clean_id}.html">
    <meta property="og:title" content="{title} at {company}">
    <meta property="og:description" content="{summary}">
    <meta property="og:url" content="https://mytomboy360.com/job-{clean_id}.html">
    <meta property="og:type" content="article">
    {COMMON_HEAD}
    <!-- Schema.org JobPosting Structured Data for Google for Jobs -->
    <script type="application/ld+json">
    {schema_json}
    </script>
</head>
<body>
    <div class="site-container">
        {get_header_html()}

        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 36px 32px; margin-bottom: 36px; box-shadow: 0 2px 10px rgba(15,23,42,0.04);">
            <div style="font-size: 13px; font-weight: 800; color: #2563eb; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 12px;">
                {country.upper()} • {job.get('department', 'ENGINEERING').upper()} • VERIFIED VACANCY
            </div>

            <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 34px; line-height: 1.25; color: #0f172a; margin-bottom: 8px; font-weight: 900;">
                {title}
            </h1>

            <div style="font-size: 16px; font-weight: 600; color: #475569; margin-bottom: 20px;">
                🏢 Company: <b style="color: #0f172a;">{company}</b> &nbsp;|&nbsp; 📍 Location: <b style="color: #0f172a;">{location}</b>
            </div>

            <!-- Highlights Bar -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; margin-bottom: 28px;">
                <div>
                    <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #64748b;">Estimated Salary</div>
                    <div style="font-size: 15px; font-weight: 800; color: #059669; margin-top: 2px;">{salary}</div>
                </div>
                <div>
                    <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #64748b;">Experience Level</div>
                    <div style="font-size: 14px; font-weight: 700; color: #0f172a; margin-top: 2px;">{job.get('experience_level', 'Mid Level')}</div>
                </div>
                <div>
                    <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #64748b;">Employment Type</div>
                    <div style="font-size: 14px; font-weight: 700; color: #0f172a; margin-top: 2px;">{job.get('employment_type', 'Full-time')}</div>
                </div>
                <div>
                    <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #64748b;">Review Status</div>
                    <div style="font-size: 14px; font-weight: 700; color: #2563eb; margin-top: 2px;">Human Vetted</div>
                </div>
            </div>

            <!-- Skills Tags -->
            <div style="margin-bottom: 28px;">
                {tags_html}
            </div>

            <!-- Executive Summary Callout -->
            <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 18px 20px; border-radius: 0 8px 8px 0; margin-bottom: 28px; font-size: 15px; color: #1e3a8a; line-height: 1.6;">
                <b>Role Briefing:</b> {summary}
            </div>

            <!-- Full Job Description -->
            <div style="max-width: 840px;">
                {desc_html}
            </div>

            <!-- Direct Apply Call to Action -->
            <div style="background: #0f172a; color: #ffffff; border-radius: 8px; padding: 28px; margin-top: 36px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
                <div>
                    <div style="font-size: 18px; font-weight: 800; color: #ffffff;">Ready to apply for this position?</div>
                    <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">Applications are submitted directly on {company}'s official careers portal.</div>
                </div>
                <div>
                    <a href="{apply_url}" target="_blank" rel="noopener nofollow" class="apply-btn" style="background: #2563eb; padding: 12px 24px; font-size: 14px;">Apply on {company} Portal ↗</a>
                </div>
            </div>

            <div style="margin-top: 28px;">
                <a href="/" style="font-weight: 700; font-size: 14px; color: #2563eb;">← Return to All Tech Positions</a>
            </div>
        </article>

        {get_footer_html()}
    </div>
</body>
</html>
"""

def markdown_to_html_article(md_content, title, page_url):
    body_html = ""
    for line in md_content.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            body_html += f'<h1 style="font-family: \'Playfair Display\', Georgia, serif; font-size: 32px; font-weight: 900; color: #0f172a; margin-bottom: 16px;">{line[2:]}</h1>\n'
        elif line.startswith("## "):
            body_html += f'<h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin-top: 28px; margin-bottom: 12px;">{line[3:]}</h2>\n'
        elif line.startswith("### "):
            body_html += f'<h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin-top: 20px; margin-bottom: 8px;">{line[4:]}</h3>\n'
        elif line.startswith("- "):
            body_html += f'<li style="font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 6px; margin-left: 20px;">{line[2:]}</li>\n'
        elif line.startswith("1. ") or line.startswith("2. ") or line.startswith("3. ") or line.startswith("4. "):
            body_html += f'<li style="font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 6px; margin-left: 20px;">{line[3:]}</li>\n'
        elif line == "---":
            body_html += '<hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 24px 0;" />\n'
        else:
            body_html += f'<p style="font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 14px;">{line}</p>\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>{title} | WorkWire</title>
    <link rel="canonical" href="{page_url}">
    {COMMON_HEAD}
</head>
<body>
    <div class="site-container">
        {get_header_html()}
        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 36px 32px; margin-bottom: 36px; box-shadow: 0 2px 10px rgba(15,23,42,0.04); max-width: 900px; margin-left: auto; margin-right: auto;">
            {body_html}
        </article>
        {get_footer_html()}
    </div>
</body>
</html>
"""

def build_sitemap_xml(jobs):
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://mytomboy360.com/</loc>
    <changefreq>hourly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://mytomboy360.com/about.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://mytomboy360.com/contact.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://mytomboy360.com/privacy.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://mytomboy360.com/terms.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""
    for j in jobs:
        clean_id = j["id"].replace("job-", "")
        posted_date = j.get("posted_at", now_iso)[:10]
        xml += f"""  <url>
    <loc>https://mytomboy360.com/job-{clean_id}.html</loc>
    <lastmod>{posted_date}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
    xml += "</urlset>\n"
    return xml

def build_robots_txt():
    return """User-agent: *
Disallow: /*page=admin*
Disallow: /admin
Allow: /

User-agent: Mediapartners-Google
Disallow: /*page=admin*
Disallow: /admin
Allow: /

User-agent: AdsBot-Google
Disallow: /*page=admin*
Disallow: /admin
Allow: /

User-agent: Googlebot
Disallow: /*page=admin*
Disallow: /admin
Allow: /

Sitemap: https://mytomboy360.com/sitemap.xml
"""

def generate_all_static_pages():
    """
    Generate all pre-rendered HTML pages, job permalinks, legal pages,
    and update sitemap.xml and index.html in Streamlit's static directory.
    """
    jobs = get_approved_jobs(limit=100)
    proj_dir = os.path.dirname(__file__)

    mod_static = None
    try:
        cand = os.path.join(os.path.dirname(st_mod.__file__), 'static')
        if os.path.isdir(cand):
            mod_static = cand
    except Exception:
        pass

    static_dirs = [os.path.join(proj_dir, "static")]
    if mod_static and mod_static not in static_dirs:
        static_dirs.append(mod_static)

    for d in static_dirs:
        os.makedirs(d, exist_ok=True)

    # 1. Generate robots.txt
    robots_content = build_robots_txt()
    with open(os.path.join(proj_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)
    for s_dir in static_dirs:
        with open(os.path.join(s_dir, "robots.txt"), "w", encoding="utf-8") as f:
            f.write(robots_content)

    # 2. Copy ads.txt
    ads_src = os.path.join(proj_dir, "ads.txt")
    if os.path.exists(ads_src):
        for s_dir in static_dirs:
            shutil.copy(ads_src, os.path.join(s_dir, "ads.txt"))

    # 3. Generate sitemap.xml
    sitemap_src = os.path.join(proj_dir, "sitemap.xml")
    if jobs or not os.path.exists(sitemap_src):
        sitemap_content = build_sitemap_xml(jobs)
        with open(sitemap_src, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
    for s_dir in static_dirs:
        dest_file = os.path.join(s_dir, "sitemap.xml")
        try:
            if os.path.exists(sitemap_src) and os.path.abspath(sitemap_src) != os.path.abspath(dest_file):
                shutil.copy(sitemap_src, dest_file)
        except Exception:
            pass

    # 4. Generate legal/informational pages
    pages = {
        "about.html": markdown_to_html_article(ABOUT_PAGE_MD, "About Us", "https://mytomboy360.com/about.html"),
        "contact.html": markdown_to_html_article(CONTACT_PAGE_MD, "Contact Bureau", "https://mytomboy360.com/contact.html"),
        "privacy.html": markdown_to_html_article(PRIVACY_PAGE_MD, "Privacy Policy", "https://mytomboy360.com/privacy.html"),
        "terms.html": markdown_to_html_article(TERMS_PAGE_MD, "Terms of Service", "https://mytomboy360.com/terms.html")
    }
    for filename, page_content in pages.items():
        with open(os.path.join(proj_dir, filename), "w", encoding="utf-8") as f:
            f.write(page_content)
        for s_dir in static_dirs:
            with open(os.path.join(s_dir, filename), "w", encoding="utf-8") as f:
                f.write(page_content)

    # 5. Generate job permalinks (job-{clean_id}.html)
    for j in jobs:
        clean_id = j["id"].replace("job-", "")
        job_filename = f"job-{clean_id}.html"
        job_html = build_job_page_html(j)
        with open(os.path.join(proj_dir, job_filename), "w", encoding="utf-8") as f:
            f.write(job_html)
        for s_dir in static_dirs:
            with open(os.path.join(s_dir, job_filename), "w", encoding="utf-8") as f:
                f.write(job_html)

    # 6. Inject homepage content, scoped styling, and AdSense tags into Streamlit's real index.html
    try:
        if mod_static:
            idx_path = os.path.join(mod_static, "index.html")
            if os.path.exists(idx_path):
                with open(idx_path, "r", encoding="utf-8") as f:
                    idx_html = f.read()

                # Update Title
                idx_html = re.sub(r'<title>.*?</title>', '<title>WORKWIRE | Curated Tech & Leadership Careers in India & US</title>', idx_html)

                # Inject AdSense Meta Tag in <head>
                if "google-adsense-account" not in idx_html:
                    idx_html = idx_html.replace("<head>", f"<head>\n    {ADSENSE_META}")

                # Inject AdSense Script in <head>
                if "pagead2.googlesyndication.com" not in idx_html:
                    idx_html = idx_html.replace("</head>", f"    {ADSENSE_SCRIPT}\n</head>")

                # Inject GoatCounter Script in <head>
                if "mytomboy360.goatcounter.com" not in idx_html:
                    idx_html = idx_html.replace("</head>", f"    {GOATCOUNTER_SCRIPT}\n</head>")

                # Inject Scoped Pre-render CSS in <head>
                if 'id="prerender-styles"' not in idx_html:
                    idx_html = idx_html.replace("</head>", f"    {SCOPED_PRERENDER_CSS}\n</head>")

                # Inject Homepage Semantic Editorial Content inside <div id="root">
                homepage_body = build_prerendered_homepage_html(jobs)
                if homepage_body:
                    root_idx = idx_html.find('<div id="root">')
                    body_end_idx = idx_html.find('</body>')
                    if root_idx != -1 and body_end_idx != -1:
                        before_root = idx_html[:root_idx + len('<div id="root">')]
                        after_body = idx_html[body_end_idx:]
                        idx_html = f"{before_root}\n{homepage_body}\n</div>\n{after_body}"

                with open(idx_path, "w", encoding="utf-8") as f:
                    f.write(idx_html)
    except Exception as e:
        print(f"Error updating streamlit index.html: {e}")

    # 7. Ensure all job and static files from proj_dir are synced into all static directories (excluding index.html)
    import glob
    for pattern in ["job-*.html", "*.html", "sitemap.xml", "robots.txt", "ads.txt"]:
        for src_file in glob.glob(os.path.join(proj_dir, pattern)):
            fname = os.path.basename(src_file)
            if fname in ["index.html", "index_prerendered.html"]:
                continue
            for s_dir in static_dirs:
                dest_file = os.path.join(s_dir, fname)
                try:
                    if not os.path.exists(dest_file) or os.path.abspath(src_file) != os.path.abspath(dest_file):
                        shutil.copy(src_file, dest_file)
                except Exception:
                    pass

    print(f"Successfully generated static site: {len(jobs)} jobs, sitemap, legal pages, and index.html")

def inject_prerender():
    generate_all_static_pages()

if __name__ == "__main__":
    generate_all_static_pages()
