import os
import re
import shutil
from datetime import datetime, timezone
import streamlit as st_mod

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
    <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #f8fafc;
            color: #0f172a;
            line-height: 1.6;
        }}
        a {{ color: #dc2626; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .site-container {{
            max-width: 1240px;
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
            border-bottom: 3px double #0f172a;
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
            font-size: 42px;
            font-weight: 900;
            letter-spacing: -0.5px;
            line-height: 1;
            color: #0f172a;
        }}
        .masthead-sub {{
            font-size: 13px;
            color: #475569;
            letter-spacing: 0.1em;
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
            border-top: 3px solid #dc2626;
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
        .footer-links a:hover {{ color: #dc2626; }}
        @media (max-width: 768px) {{
            .masthead-title {{ font-size: 30px; }}
            .top-intel-bar {{ flex-direction: column; align-items: flex-start; gap: 4px; }}
        }}
    </style>
"""

def get_header_html():
    now_str = datetime.now(timezone.utc).strftime("%A, %B %d, %Y")
    return f"""
    <div class="top-intel-bar">
        <div>🌐 <b>WORLDWIRE INTERNATIONAL WIRE</b> &nbsp;|&nbsp; {now_str}</div>
        <div>PUBLISHED AT MYTOMBOY360.COM</div>
    </div>
    <header class="masthead">
        <div>
            <h1 class="masthead-title"><a href="/" style="color: #0f172a; text-decoration: none;">WORLDWIRE</a></h1>
            <div class="masthead-sub">Global Real-Time Intelligence & International News Desk</div>
        </div>
        <div style="text-align: right; font-size: 12px; color: #64748b; font-weight: 600;">
            <div style="color: #dc2626; font-weight: 800;">🔴 LIVE WIRE DISPATCHES</div>
            <div>Publisher: Abhishek Pandey (TechSnapZone)</div>
        </div>
    </header>
    <nav class="nav-bar">
        <a href="/">Top Stories</a>
        <a href="/about.html">About Bureau</a>
        <a href="/contact.html">Contact Us</a>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms of Service</a>
    </nav>
    """

def get_footer_html():
    return """
    <footer class="site-footer">
        <div class="footer-links">
            <a href="/">Top Stories</a> |
            <a href="/about.html">About Us</a> |
            <a href="/contact.html">Contact Bureau</a> |
            <a href="/privacy.html">Privacy Policy</a> |
            <a href="/terms.html">Terms of Service</a> |
            <a href="https://www.reuters.com" target="_blank" rel="noopener">Reuters Wire ↗</a> |
            <a href="https://www.apnews.com" target="_blank" rel="noopener">Associated Press ↗</a> |
            <a href="https://www.bloomberg.com" target="_blank" rel="noopener">Bloomberg Markets ↗</a>
        </div>
        <p>© 2026 <b>WORLDWIRE NEWS NETWORK</b> • Published at <b>mytomboy360.com</b> by Abhishek Pandey (TechSnapZone).</p>
        <p style="margin-top: 6px;">Verified Editorial, Corrections & AdSense Compliance: <a href="mailto:techsnapzone@gmail.com" style="color: #dc2626; font-weight: 700;">techsnapzone@gmail.com</a></p>
    </footer>
    """

CATEGORY_IMAGES = {
    "TECHNOLOGY": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w={width}&q=80",
    "TECH": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w={width}&q=80",
    "POLITICS": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w={width}&q=80",
    "GOVERNANCE": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w={width}&q=80",
    "ECONOMY": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w={width}&q=80",
    "MARKETS": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w={width}&q=80",
    "BUSINESS": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w={width}&q=80",
    "SCIENCE": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?auto=format&fit=crop&w={width}&q=80",
    "HEALTH": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w={width}&q=80",
    "DEFENSE": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w={width}&q=80",
    "SECURITY": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w={width}&q=80",
    "ENERGY": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w={width}&q=80",
    "CLIMATE": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w={width}&q=80",
    "ENVIRONMENT": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w={width}&q=80",
    "WORLD": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w={width}&q=80",
    "GLOBAL": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w={width}&q=80",
}

def get_clean_image_url(art, width=800):
    """
    Return a clean, lightweight external image URL.
    Replaces heavy base64 data URIs with category-specific editorial Unsplash images
    to keep static HTML files under 25KB and avoid Google crawler timeouts.
    """
    raw_url = art.get("image_url") if isinstance(art, dict) else None
    if raw_url and isinstance(raw_url, str):
        raw_url = raw_url.strip()
        if raw_url.startswith("http://") or raw_url.startswith("https://"):
            return raw_url

    cat = (art.get("category") or "WORLD").upper().strip() if isinstance(art, dict) else "WORLD"
    for key, template in CATEGORY_IMAGES.items():
        if key in cat:
            return template.format(width=width)
    return CATEGORY_IMAGES["WORLD"].format(width=width)

def format_date_str(dt):
    if not dt:
        return "Recent dispatch"
    try:
        if isinstance(dt, str):
            dt = datetime.fromisoformat(dt.replace("Z", "+00:00"))
        return dt.strftime("%B %d, %Y at %H:%M UTC")
    except Exception:
        return str(dt)[:19]

def build_prerendered_homepage_html(articles):
    if not articles:
        return ""
    
    hero = articles[0]
    grid_articles = articles[1:7] if len(articles) > 1 else []
    stream_articles = articles[7:] if len(articles) > 7 else []

    hero_img = get_clean_image_url(hero, width=1200)
    hero_author = hero.get("author") or "Abhishek Pandey, WorldWire News Desk"
    hero_date = format_date_str(hero.get("published_at"))

    html = f"""
    <div id="prerender-container" class="site-container">
        {get_header_html()}

        <!-- Breaking Ticker -->
        <div style="background: #991b1b; color: #ffffff; padding: 10px 16px; border-radius: 6px; margin-bottom: 24px; display: flex; align-items: center; gap: 12px; font-size: 14px;">
            <span style="background: #ef4444; color: #fff; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">BREAKING NEWS</span>
            <span style="font-weight: 600;">{hero['title']}</span>
        </div>

        <!-- Featured Lead Hero Story -->
        <section style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; margin-bottom: 36px; box-shadow: 0 2px 8px rgba(15,23,42,0.06);">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));">
                <div>
                    <img src="{hero_img}" alt="{hero['title']}" style="width: 100%; height: 100%; min-height: 280px; max-height: 420px; object-fit: cover;" />
                </div>
                <div style="padding: 28px 24px; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px;">
                        🔥 LEAD DISPATCH • {hero.get('category', 'WORLD').upper()} • {hero.get('region', 'GLOBAL').upper()}
                    </div>
                    <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 28px; line-height: 1.25; margin-bottom: 12px; font-weight: 800;">
                        <a href="/article-{hero['id']}.html" style="color: #0f172a;">{hero['title']}</a>
                    </h2>
                    <p style="font-size: 15px; color: #334155; line-height: 1.6; margin-bottom: 16px;">{hero.get('summary', '')}</p>
                    <div style="font-size: 12px; color: #64748b; margin-bottom: 18px; border-top: 1px solid #f1f5f9; padding-top: 10px;">
                        ✍️ <b>By {hero_author}</b> &nbsp;•&nbsp; ⏱️ {hero_date} &nbsp;•&nbsp; 📰 Wire Attribution: {hero.get('source_name', 'WorldWire Wire Desk')}
                    </div>
                    <div>
                        <a href="/article-{hero['id']}.html" style="display: inline-block; background: #dc2626; color: #ffffff; padding: 10px 22px; border-radius: 6px; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 0.04em;">Read Full Dispatch →</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Top Stories Grid -->
        <div style="border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-bottom: 20px;">
            <h3 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; color: #0f172a;">TOP WIRE DISPATCHES & INTELLIGENCE RADAR</h3>
        </div>
        <section style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 40px;">
    """

    for a in grid_articles:
        img = get_clean_image_url(a, width=800)
        a_date = format_date_str(a.get("published_at"))
        a_author = a.get("author") or "Abhishek Pandey, WorldWire News Desk"
        html += f"""
        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 1px 4px rgba(15,23,42,0.04);">
            <div>
                <img src="{img}" alt="{a['title']}" style="width: 100%; height: 180px; object-fit: cover; border-radius: 6px; margin-bottom: 12px;" />
                <div style="font-size: 11px; font-weight: 800; color: #dc2626; text-transform: uppercase; margin-bottom: 6px;">
                    {a.get('category', 'WORLD').upper()} • {a.get('region', 'GLOBAL').upper()}
                </div>
                <h4 style="font-family: 'Playfair Display', Georgia, serif; font-size: 19px; line-height: 1.3; margin-bottom: 10px; font-weight: 700;">
                    <a href="/article-{a['id']}.html" style="color: #0f172a;">{a['title']}</a>
                </h4>
                <p style="font-size: 14px; color: #475569; line-height: 1.5; margin-bottom: 12px;">{a.get('summary', '')}</p>
            </div>
            <div style="border-top: 1px solid #f1f5f9; padding-top: 10px; font-size: 12px; color: #94a3b8; display: flex; justify-content: space-between; align-items: center;">
                <span>By {a_author.split(',')[0]}</span>
                <a href="/article-{a['id']}.html" style="font-weight: 700;">Read More →</a>
            </div>
        </article>
        """

    html += """
        </section>

        <!-- Latest Dispatches Stream -->
        <div style="border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-bottom: 20px;">
            <h3 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; color: #0f172a;">LATEST WIRE REPORTING ARCHIVE</h3>
        </div>
        <section style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 40px;">
    """

    for s in stream_articles:
        s_date = format_date_str(s.get("published_at"))
        s_img = get_clean_image_url(s, width=400)
        html += f"""
        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; display: grid; grid-template-columns: 160px 1fr; gap: 18px; align-items: center;">
            <img src="{s_img}" alt="{s['title']}" style="width: 160px; height: 110px; object-fit: cover; border-radius: 6px;" />
            <div>
                <div style="font-size: 11px; font-weight: 800; color: #dc2626; text-transform: uppercase;">
                    {s.get('category', 'WORLD').upper()} • {s.get('region', 'GLOBAL').upper()} • {s_date}
                </div>
                <h4 style="font-family: 'Playfair Display', Georgia, serif; font-size: 18px; font-weight: 700; margin: 4px 0 6px 0;">
                    <a href="/article-{s['id']}.html" style="color: #0f172a;">{s['title']}</a>
                </h4>
                <p style="font-size: 13px; color: #475569; line-height: 1.4; margin-bottom: 8px;">{s.get('summary', '')}</p>
                <div style="font-size: 12px; color: #94a3b8;">
                    📰 Source: {s.get('source_name', 'WorldWire Wire Service')} | <a href="/article-{s['id']}.html" style="font-weight: 700;">Full Dispatch →</a>
                </div>
            </div>
        </article>
        """

    html += f"""
        </section>

        <!-- Journalistic Mission & E-E-A-T Notice -->
        <section style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 24px; margin-bottom: 30px;">
            <h4 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 8px;">About WorldWire Editorial Newsroom</h4>
            <p style="font-size: 14px; color: #334155; line-height: 1.6; margin-bottom: 10px;">
                WorldWire (published at <b>mytomboy360.com</b>) is an independent international journal of global affairs and wire intelligence edited by <b>Abhishek Pandey (TechSnapZone)</b>. 
                All dispatches are verified across sovereign diplomatic communiques, official registries, and primary international press agencies including Reuters, Bloomberg, and the Associated Press.
            </p>
            <p style="font-size: 13px; color: #64748b;">
                Every story undergoes human review and fact-checking prior to publication. For inquiries, syndication, or corrections, contact our editorial bureau directly at <a href="mailto:techsnapzone@gmail.com" style="color: #dc2626; font-weight: 700;">techsnapzone@gmail.com</a>.
            </p>
        </section>

        {get_footer_html()}
    </div>
    """
    return html

def build_article_page_html(article, other_articles):
    art_id = article["id"]
    title = article["title"]
    summary = article.get("summary", "")
    content = article.get("content", "")
    category = (article.get("category") or "WORLD").upper()
    region = (article.get("region") or "GLOBAL").upper()
    author = article.get("author") or "Abhishek Pandey, WorldWire News Desk"
    source = article.get("source_name") or "WorldWire Wire Desk"
    source_url = article.get("source_url") or ""
    image_url = get_clean_image_url(article, width=1200)
    pub_dt = article.get("published_at")
    pub_date_str = format_date_str(pub_dt)
    pub_iso = pub_dt.isoformat() if hasattr(pub_dt, "isoformat") else datetime.now(timezone.utc).isoformat()

    # Format paragraphs
    paragraphs_raw = content.split("\n\n") if content else [summary]
    body_html = ""
    for p in paragraphs_raw:
        p_clean = p.strip()
        if p_clean:
            body_html += f'<p style="font-size: 18px; line-height: 1.8; color: #1e293b; margin-bottom: 22px; font-family: \'Newsreader\', Georgia, serif;">{p_clean}</p>\n'

    # Related articles
    related_html = ""
    for rel in other_articles[:4]:
        if rel["id"] != art_id:
            related_html += f"""
            <div style="border-bottom: 1px solid #f1f5f9; padding: 10px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #dc2626; text-transform: uppercase;">{rel.get('category', 'WORLD')}</div>
                <a href="/article-{rel['id']}.html" style="font-weight: 700; color: #0f172a; font-size: 15px; font-family: 'Playfair Display', Georgia, serif;">{rel['title']}</a>
            </div>
            """

    source_btn = f'<a href="{source_url}" target="_blank" rel="noopener" style="display: inline-block; background: #0f172a; color: #ffffff; padding: 8px 18px; border-radius: 6px; font-size: 13px; font-weight: 600; text-decoration: none; margin-top: 12px;">Verify at {source} ↗</a>' if source_url else ''

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>{title} | WorldWire</title>
    <meta name="description" content="{summary[:160]}">
    <link rel="canonical" href="https://mytomboy360.com/article-{art_id}.html">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{summary}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:url" content="https://mytomboy360.com/article-{art_id}.html">
    <meta property="og:type" content="article">
    {COMMON_HEAD}
    <!-- Schema.org NewsArticle Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": {repr(title)},
        "image": [{repr(image_url)}],
        "datePublished": {repr(pub_iso)},
        "dateModified": {repr(pub_iso)},
        "author": [{{
            "@type": "Person",
            "name": {repr(author.split(',')[0])},
            "jobTitle": "Lead Editor & Publisher",
            "url": "https://mytomboy360.com/about.html"
        }}],
        "publisher": {{
            "@type": "Organization",
            "name": "WorldWire",
            "url": "https://mytomboy360.com",
            "logo": {{
                "@type": "ImageObject",
                "url": "https://mytomboy360.com/favicon.png"
            }}
        }},
        "description": {repr(summary)}
    }}
    </script>
</head>
<body>
    <div class="site-container">
        {get_header_html()}

        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 36px 32px; margin-bottom: 36px; box-shadow: 0 2px 10px rgba(15,23,42,0.04);">
            <div style="font-size: 13px; font-weight: 800; color: #dc2626; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 12px;">
                {category} &nbsp;•&nbsp; {region} &nbsp;•&nbsp; WIRE DISPATCH
            </div>
            
            <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 36px; line-height: 1.25; color: #0f172a; margin-bottom: 16px; font-weight: 900;">
                {title}
            </h1>

            <div style="font-size: 13px; color: #64748b; border-bottom: 1px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 24px;">
                ✍️ <b>By {author}</b> &nbsp;|&nbsp; ⏱️ Published <b>{pub_date_str}</b> &nbsp;|&nbsp; 📰 Wire Attribution: <b>{source}</b>
            </div>

            <!-- Featured Image -->
            <div style="margin-bottom: 28px;">
                <img src="{image_url}" alt="{title}" style="width: 100%; max-height: 520px; object-fit: cover; border-radius: 8px;" />
                <div style="font-size: 12px; color: #94a3b8; margin-top: 6px; font-style: italic;">Photojournalism wire visual • Attributed to {source} editorial archive</div>
            </div>

            <!-- Executive Summary Callout -->
            <div style="background: #f8fafc; border-left: 4px solid #dc2626; padding: 18px 20px; border-radius: 0 8px 8px 0; margin-bottom: 28px; font-size: 16px; font-weight: 500; color: #334155; line-height: 1.6;">
                <b>Executive Briefing:</b> {summary}
            </div>

            <!-- Full Article Body -->
            <div class="article-body" style="max-width: 820px;">
                {body_html}
            </div>

            <!-- Wire Attribution Box -->
            <div style="background: #f1f5f9; border-radius: 6px; padding: 18px; margin-top: 32px; border-top: 2px solid #0f172a;">
                <div style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Primary Wire Intelligence & Editorial Oversight</div>
                <div style="font-size: 13px; color: #475569; line-height: 1.5;">
                    This report was synthesized and editorially verified by Abhishek Pandey from primary wire communiques, official sovereign ministries, and accredited international press registries ({source}).
                </div>
                {source_btn}
            </div>

            <div style="margin-top: 28px;">
                <a href="/" style="font-weight: 700; font-size: 14px;">← Back to Top Headlines</a>
            </div>
        </article>

        <!-- Read Next Section -->
        <section style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; margin-bottom: 36px;">
            <h3 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 14px;">More Dispatches from WorldWire Desk</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                {related_html}
            </div>
        </section>

        {get_footer_html()}
    </div>
</body>
</html>
    """
    return html

def build_about_page_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>About Us | WorldWire News Bureau</title>
    <meta name="description" content="About WorldWire: An independent international news publication operated by Abhishek Pandey (TechSnapZone). Learn about our E-E-A-T editorial standards.">
    <link rel="canonical" href="https://mytomboy360.com/about.html">
    {COMMON_HEAD}
</head>
<body>
    <div class="site-container">
        {get_header_html()}

        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 36px 32px; margin-bottom: 36px; line-height: 1.7;">
            <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase; margin-bottom: 10px;">EDITORIAL MISSION & TRANSPARENCY</div>
            <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 34px; font-weight: 900; margin-bottom: 14px; color: #0f172a;">
                The International Journal of Global Affairs & Wire Intelligence
            </h1>
            <p style="font-size: 16px; color: #475569; font-style: italic; margin-bottom: 24px;">
                Delivering unvarnished, factual, and verified international reporting across geopolitics, markets, science, and technological shifts.
            </p>
            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin-bottom: 24px;">

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; margin-bottom: 10px;">Our Mission & Publishing Entity</h2>
            <p style="margin-bottom: 20px; color: #334155;">
                <b>WorldWire</b> is an independent digital news and geopolitical wire publication operated on <b>mytomboy360.com</b> by <b>Abhishek Pandey (TechSnapZone)</b>. Founded to provide global readers, researchers, policy observers, and technology professionals with real-time, non-partisan dispatches, WorldWire synthesizes verified international events into comprehensive briefings with clear, primary-source attribution and full editorial oversight.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; margin-bottom: 10px;">Editorial Standards & E-E-A-T Framework</h2>
            <p style="margin-bottom: 12px; color: #334155;">We adhere strictly to high journalistic standards of accuracy, transparency, and accountability:</p>
            <ul style="margin-left: 24px; margin-bottom: 20px; color: #334155;">
                <li style="margin-bottom: 8px;"><b>Multi-Source Cross Verification:</b> All published events are verified against international diplomatic records, sovereign wire reports, and reputable press agencies (including Reuters, Associated Press, Agence France-Presse, Bloomberg, and the BBC).</li>
                <li style="margin-bottom: 8px;"><b>Neutral Tone & Strict Attribution:</b> We report facts, verified statements, and economic metrics without sensationalist commentary or speculative hyperbole. Every dispatch cites the primary news desk responsible for original field reporting.</li>
                <li style="margin-bottom: 8px;"><b>Global Breadth:</b> Our coverage actively monitors developments across North America, Latin America, Europe, Africa, the Middle East, and Asia-Pacific.</li>
                <li style="margin-bottom: 8px;"><b>Human Accountability & Editorial Oversight:</b> WorldWire is edited and published by Abhishek Pandey. Every story is reviewed, verified, and authorized through our editorial desk before publication. Reader inquiries and corrections are handled directly via verified email <b>techsnapzone@gmail.com</b>.</li>
            </ul>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; margin-bottom: 10px;">Editorial Methodology & Newsroom Standards</h2>
            <p style="margin-bottom: 20px; color: #334155;">
                WorldWire's editorial desk actively monitors global press feeds, diplomatic communiques, and sovereign wire archives around the clock. Our editorial research workflow cross-checks multilingual primary documents against international news repositories, synthesizing them into comprehensive, verified executive dispatches. Every dispatch undergoes manual review, fact-checking, and editorial authorization by Abhishek Pandey before being published.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; margin-bottom: 10px;">Dedicated Coverage Desks</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 24px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
                    <h3 style="font-size: 15px; font-weight: 800; margin-bottom: 6px; color: #0f172a;">🌐 Geopolitics & World</h3>
                    <p style="font-size: 13px; color: #64748b;">Diplomatic treaties, regional conflicts, sovereign summit communiques, and humanitarian missions.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
                    <h3 style="font-size: 15px; font-weight: 800; margin-bottom: 6px; color: #0f172a;">📈 Global Markets & Economy</h3>
                    <p style="font-size: 13px; color: #64748b;">Central bank rate actions, trade corridors, sovereign debt cycles, energy spot markets, and supply chains.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
                    <h3 style="font-size: 15px; font-weight: 800; margin-bottom: 6px; color: #0f172a;">⚡ Technology & Computing</h3>
                    <p style="font-size: 13px; color: #64748b;">Artificial intelligence infrastructure, semiconductor fabrication, telecommunications, and quantum systems.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px;">
                    <h3 style="font-size: 15px; font-weight: 800; margin-bottom: 6px; color: #0f172a;">🔬 Science & Climate</h3>
                    <p style="font-size: 13px; color: #64748b;">Space exploration missions, biomedical Nobel breakthroughs, renewable energy deployment, and weather anomalies.</p>
                </div>
            </div>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; margin-bottom: 10px;">Fact-Checking & Corrections Policy</h2>
            <p style="color: #334155;">
                Accuracy is our cornerstone. If a dispatch contains a factual error or misattribution, we issue immediate, transparent corrections. Readers and journalists wishing to report an inaccuracy may reach our corrections desk directly at <b>techsnapzone@gmail.com</b>.
            </p>
        </article>

        {get_footer_html()}
    </div>
</body>
</html>
    """

def build_contact_page_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Contact Bureau | WorldWire News Service</title>
    <meta name="description" content="Contact WorldWire News Bureau. Verified editorial, corrections, and Google AdSense compliance contact details for mytomboy360.com.">
    <link rel="canonical" href="https://mytomboy360.com/contact.html">
    {COMMON_HEAD}
</head>
<body>
    <div class="site-container">
        {get_header_html()}

        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 36px 32px; margin-bottom: 36px; line-height: 1.7;">
            <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase; margin-bottom: 10px;">CONTACT BUREAU</div>
            <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 34px; font-weight: 900; margin-bottom: 14px; color: #0f172a;">
                Connect with WorldWire Bureau
            </h1>
            <p style="font-size: 16px; color: #475569; font-style: italic; margin-bottom: 24px;">
                We welcome inquiries from readers, press colleagues, researchers, and partners worldwide.
            </p>
            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin-bottom: 24px;">

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 22px;">
                    <h2 style="font-size: 18px; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Official Communication Channels</h2>
                    
                    <div style="margin-bottom: 16px;">
                        <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase;">Primary Verified Contact</div>
                        <div style="font-size: 15px; font-weight: 700; color: #0f172a;">📧 techsnapzone@gmail.com</div>
                        <div style="font-size: 13px; color: #64748b;">Direct inbox monitored daily for all editorial, syndication, and partnership inquiries.</div>
                    </div>

                    <div style="margin-bottom: 16px;">
                        <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase;">Editorial & Content Desk</div>
                        <div style="font-size: 15px; font-weight: 700; color: #0f172a;">📧 techsnapzone@gmail.com (Subject: [Editorial Inquiry])</div>
                        <div style="font-size: 13px; color: #64748b;">For questions regarding story coverage, press quotes, and syndication.</div>
                    </div>

                    <div style="margin-bottom: 16px;">
                        <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase;">Corrections & Fact-Checking Desk</div>
                        <div style="font-size: 15px; font-weight: 700; color: #0f172a;">📧 techsnapzone@gmail.com (Subject: [Correction Request])</div>
                        <div style="font-size: 13px; color: #64748b;">Direct priority line for factual rectifications, source attribution, and updates.</div>
                    </div>

                    <div>
                        <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase;">Advertising & AdSense Compliance</div>
                        <div style="font-size: 15px; font-weight: 700; color: #0f172a;">📧 techsnapzone@gmail.com (Subject: [Compliance])</div>
                        <div style="font-size: 13px; color: #64748b;">For Google AdSense policy coordination, sponsorship, and commercial matters.</div>
                    </div>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 22px;">
                    <h2 style="font-size: 18px; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Publication Entity & Bureau Information</h2>
                    <p style="font-size: 14px; color: #334155; margin-bottom: 12px;">
                        <b>Publication:</b> WorldWire<br>
                        <b>Primary Domain:</b> https://mytomboy360.com<br>
                        <b>Publisher & Editor-in-Chief:</b> Abhishek Pandey (TechSnapZone)<br>
                        <b>Verified Contact Email:</b> techsnapzone@gmail.com<br>
                        <b>Geographic Headquarters:</b> Digital International Wire Desk<br>
                        <b>Publishing Cadence:</b> 24/7 Real-Time Global Reporting
                    </p>
                    <p style="font-size: 13px; color: #64748b; line-height: 1.5;">
                        We review all emails within 24 hours. For breaking news tips or primary document submissions, please include verifiable primary source links and official communiques.
                    </p>
                </div>
            </div>
        </article>

        {get_footer_html()}
    </div>
</body>
</html>
    """

def build_privacy_page_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Privacy Policy | WorldWire</title>
    <meta name="description" content="WorldWire Privacy Policy. Comprehensive disclosures on cookies, Google AdSense, GDPR, CCPA, and data privacy for mytomboy360.com.">
    <link rel="canonical" href="https://mytomboy360.com/privacy.html">
    {COMMON_HEAD}
</head>
<body>
    <div class="site-container">
        {get_header_html()}

        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 36px 32px; margin-bottom: 36px; line-height: 1.7;">
            <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase; margin-bottom: 10px;">LEGAL & COMPLIANCE</div>
            <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 34px; font-weight: 900; margin-bottom: 10px; color: #0f172a;">
                WorldWire Privacy Policy
            </h1>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 24px;">
                Effective Date: January 1, 2026 | Last Updated: October 12, 2026 | Domain: mytomboy360.com
            </p>
            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin-bottom: 24px;">

            <p style="margin-bottom: 18px; color: #334155;">
                At <b>WorldWire (mytomboy360.com)</b>, the privacy of our visitors is of paramount importance to us. This Privacy Policy document outlines the types of information collected and recorded by WorldWire and how we utilize it in full compliance with international regulations including GDPR, CCPA, and Google AdSense partner guidelines.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">1. Consent</h2>
            <p style="margin-bottom: 18px; color: #334155;">By using our website, you hereby consent to our Privacy Policy and agree to its terms.</p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">2. Standard Log Files</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                WorldWire follows a standard procedure of utilizing log files. These files log visitors when they access websites. The information collected by log files includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, and number of clicks. These are not linked to any information that is personally identifiable. The purpose is for analyzing trends, administering the site, and gathering demographic information.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">3. Cookies and Web Beacons</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                Like any other digital publication, WorldWire uses 'cookies' to store information including visitors' preferences and the pages on the website that the visitor accessed. The information is used to optimize user experience.
            </p>

            <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px; padding: 20px; margin-bottom: 22px;">
                <h3 style="font-size: 16px; font-weight: 800; color: #1e3a8a; margin-bottom: 8px;">4. Google AdSense & DoubleClick DART Cookies (Mandatory Disclosure)</h3>
                <p style="font-size: 14px; color: #1e40af; line-height: 1.6; margin-bottom: 10px;">
                    Google is one of our third-party advertising vendors on our site (<code>mytomboy360.com</code>). It uses cookies, known as DART cookies, to serve advertisements to our site visitors based upon their visit to WorldWire and other sites across the internet.
                </p>
                <ul style="font-size: 14px; color: #1e40af; margin-left: 20px; line-height: 1.6;">
                    <li>Third party vendors, including Google, use cookies to serve ads based on a user's prior visits to your website or other websites.</li>
                    <li>Google's use of advertising cookies enables it and its partners to serve ads to users based on their visit to our sites and/or other sites on the Internet.</li>
                    <li>Users may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>. Alternatively, users can opt out of a third-party vendor's use of cookies for personalized advertising by visiting <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">www.aboutads.info</a>.</li>
                </ul>
            </div>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">5. Third-Party Privacy Policies</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                WorldWire's Privacy Policy does not apply to other advertisers or websites. Thus, we advise you to consult the respective Privacy Policies of these third-party ad servers for more detailed information. It may include their practices and instructions about how to opt-out of certain options.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">6. Privacy-First Analytics (GoatCounter)</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                We utilize GoatCounter, an open-source, privacy-first web analytics platform that does not track users across websites, does not use tracking cookies, and does not harvest personally identifiable data. All statistical data collected is strictly aggregated to gauge readership popularity and geographic distribution.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">7. CCPA Privacy Rights (Do Not Sell My Personal Information)</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                Under the California Consumer Privacy Act (CCPA), consumers have the right to request disclosure or deletion of collected personal data, and to request that a business not sell their personal data. WorldWire does not sell personal information.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">8. GDPR Data Protection Rights</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                Every user is entitled to data access, rectification, erasure, restriction of processing, objection to processing, and data portability under the General Data Protection Regulation (GDPR).
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">9. Contact Us Regarding Privacy</h2>
            <p style="color: #334155;">
                If you have questions or require more information about our Privacy Policy, contact our Data Protection Administrator directly at <b>techsnapzone@gmail.com</b>.
            </p>
        </article>

        {get_footer_html()}
    </div>
</body>
</html>
    """

def build_terms_page_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Terms of Service | WorldWire</title>
    <meta name="description" content="WorldWire Terms of Service. Legal agreements, intellectual property guidelines, and disclaimers for mytomboy360.com.">
    <link rel="canonical" href="https://mytomboy360.com/terms.html">
    {COMMON_HEAD}
</head>
<body>
    <div class="site-container">
        {get_header_html()}

        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 36px 32px; margin-bottom: 36px; line-height: 1.7;">
            <div style="font-size: 12px; font-weight: 800; color: #dc2626; text-transform: uppercase; margin-bottom: 10px;">LEGAL & COMPLIANCE</div>
            <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 34px; font-weight: 900; margin-bottom: 10px; color: #0f172a;">
                WorldWire Terms of Service
            </h1>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 24px;">
                Effective Date: January 1, 2026 | Last Updated: October 12, 2026 | Domain: mytomboy360.com
            </p>
            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin-bottom: 24px;">

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">1. Acceptance of Terms</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                By accessing or reading the WorldWire intelligence portal at <b>mytomboy360.com</b> (and all affiliated subdomains and digital services), you agree to be bound by these Terms of Service and all applicable international laws and regulations. If you do not agree with any of these terms, you are prohibited from using or accessing this site.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">2. Intellectual Property & Fair Use Attribution</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                All original editorial syntheses, branding, layout architectures, and software codebase associated with WorldWire are protected by copyright. External reporting, cited quotes, and third-party trademarks referenced in news dispatches remain the intellectual property of their respective originating news wire agencies (Reuters, AP, Bloomberg, BBC, etc.).
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">3. Disclaimer of Financial & Legal Advice</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                Articles, market figures, and economic indicators published across WorldWire are provided purely for educational and journalistic informational purposes. Nothing published on this site constitutes financial, legal, investment, or geopolitical consulting advice. Readers must conduct independent verification before executing financial transactions based on real-time news data.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">4. External Hyperlinks</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                WorldWire dispatches cite and link to primary source publications, diplomatic archives, and original wire services. WorldWire is not responsible for the contents or availability of any linked external third-party site.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">5. Modifications to Terms</h2>
            <p style="margin-bottom: 18px; color: #334155;">
                WorldWire reserves the right to revise these Terms of Service at any time without prior notice. By continuing to access this website, you agree to be bound by the then-current version of these Terms.
            </p>

            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-weight: 800; margin-bottom: 10px;">6. Contact Information</h2>
            <p style="color: #334155;">
                For legal, copyright, or terms inquiries, contact the publisher at <b>techsnapzone@gmail.com</b>.
            </p>
        </article>

        {get_footer_html()}
    </div>
</body>
</html>
    """

def build_sitemap_xml(articles):
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
    for a in articles:
        dt = a.get("published_at")
        d_str = dt.strftime("%Y-%m-%d") if hasattr(dt, "strftime") else now_iso
        xml += f"""  <url>
    <loc>https://mytomboy360.com/article-{a['id']}.html</loc>
    <lastmod>{d_str}</lastmod>
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
    Generate all pre-rendered HTML pages, article permalinks, legal pages,
    and update sitemap.xml and index.html in Streamlit's static directory.
    """
    try:
        from database import get_articles
        articles = get_articles(limit=100, status="published")
    except Exception as e:
        print(f"Database query error in prerender: {e}")
        articles = []

    proj_dir = os.path.dirname(__file__)
    static_dirs = []

    # Streamlit module internal static directory
    try:
        mod_static = os.path.join(os.path.dirname(st_mod.__file__), 'static')
        if os.path.isdir(mod_static):
            static_dirs.append(mod_static)
    except Exception:
        pass

    # Project local static directory
    proj_static = os.path.join(proj_dir, 'static')
    os.makedirs(proj_static, exist_ok=True)
    static_dirs.append(proj_static)

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
    if articles or not os.path.exists(sitemap_src):
        sitemap_content = build_sitemap_xml(articles)
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
        "about.html": build_about_page_html(),
        "contact.html": build_contact_page_html(),
        "privacy.html": build_privacy_page_html(),
        "terms.html": build_terms_page_html()
    }
    for filename, page_content in pages.items():
        with open(os.path.join(proj_dir, filename), "w", encoding="utf-8") as f:
            f.write(page_content)
        for s_dir in static_dirs:
            with open(os.path.join(s_dir, filename), "w", encoding="utf-8") as f:
                f.write(page_content)

    # 5. Generate article permalinks (article-{id}.html)
    for art in articles:
        art_filename = f"article-{art['id']}.html"
        art_html = build_article_page_html(art, articles)
        with open(os.path.join(proj_dir, art_filename), "w", encoding="utf-8") as f:
            f.write(art_html)
        for s_dir in static_dirs:
            with open(os.path.join(s_dir, art_filename), "w", encoding="utf-8") as f:
                f.write(art_html)

    # 6. Inject homepage content and AdSense tags into index.html
    for s_dir in static_dirs:
        idx_path = os.path.join(s_dir, "index.html")
        if os.path.exists(idx_path):
            with open(idx_path, "r", encoding="utf-8") as f:
                idx_html = f.read()

            # Inject AdSense Meta Tag
            if "google-adsense-account" not in idx_html:
                idx_html = idx_html.replace("<head>", f"<head>\n    {ADSENSE_META}")

            # Inject AdSense Script
            if "pagead2.googlesyndication.com" not in idx_html:
                idx_html = idx_html.replace("</head>", f"{ADSENSE_SCRIPT}\n</head>")

            # Inject GoatCounter Script
            if "mytomboy360.goatcounter.com" not in idx_html:
                idx_html = idx_html.replace("</head>", f"{GOATCOUNTER_SCRIPT}\n</head>")

            # Inject real homepage editorial content inside <div id="root">
            homepage_body = build_prerendered_homepage_html(articles)
            if homepage_body:
                if '<div id="root">' in idx_html:
                    prefix = idx_html.split('<div id="root">')[0] + '<div id="root">'
                    idx_html = f"{prefix}\n{homepage_body}\n</div>\n  </body>\n</html>\n"

            with open(idx_path, "w", encoding="utf-8") as f:
                f.write(idx_html)

            # Save a copy as index_prerendered.html in project dir for Docker build bundling
            if homepage_body:
                with open(os.path.join(proj_dir, "index_prerendered.html"), "w", encoding="utf-8") as f:
                    f.write(idx_html)

    # 7. Ensure all article and static files from proj_dir are synced into all static directories
    import glob
    for pattern in ["article-*.html", "*.html", "sitemap.xml", "robots.txt", "ads.txt"]:
        for src_file in glob.glob(os.path.join(proj_dir, pattern)):
            fname = os.path.basename(src_file)
            if fname == "index_prerendered.html":
                continue
            for s_dir in static_dirs:
                dest_file = os.path.join(s_dir, fname)
                try:
                    if not os.path.exists(dest_file) or os.path.abspath(src_file) != os.path.abspath(dest_file):
                        shutil.copy(src_file, dest_file)
                except Exception:
                    pass

    # If index_prerendered.html exists, copy it directly over index.html in Streamlit static
    prerendered_src = os.path.join(proj_dir, "index_prerendered.html")
    if os.path.exists(prerendered_src):
        for s_dir in static_dirs:
            dest_idx = os.path.join(s_dir, "index.html")
            try:
                if os.path.abspath(prerendered_src) != os.path.abspath(dest_idx):
                    shutil.copy(prerendered_src, dest_idx)
            except Exception:
                pass

    print(f"Successfully generated static site: {len(articles)} articles, sitemap, legal pages, and index.html")

def inject_prerender():
    generate_all_static_pages()

if __name__ == "__main__":
    generate_all_static_pages()
