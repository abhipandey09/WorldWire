import os
import streamlit as st_mod

def build_prerendered_html():
    articles = []
    try:
        from database import get_articles
        articles = get_articles(limit=12)
    except Exception:
        pass
    
    if not articles:
        articles = [
            {
                "title": "Panama Declares State of Emergency After 7.7 Quake and Swarm of Aftershocks",
                "summary": "President Jose Raul Mulino has signed an executive decree allocating emergency relief funds after an offshore earthquake caused widespread structural damage in Chiriqui and Bocas del Toro.",
                "category": "WORLD",
                "region": "LATIN AMERICA",
                "source_name": "Reuters / WorldWire",
                "image_url": "https://images.unsplash.com/photo-1547683905-f686c993aae5?auto=format&fit=crop&w=800&q=80"
            },
            {
                "title": "Global Central Banks Coordinate Liquidity Swap Lines Amid Currency Volatility",
                "summary": "Major monetary authorities have expanded standing bilateral liquidity facilities to ensure adequate cross-border funding as interest rate differentials drive historic capital shifts.",
                "category": "BUSINESS",
                "region": "GLOBAL",
                "source_name": "Bloomberg / WorldWire",
                "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=800&q=80"
            },
            {
                "title": "Next-Generation Semiconductor Alliances Accelerate High-Bandwidth Memory Expansion",
                "summary": "Leading chip manufacturers have announced joint packaging standards to dramatically increase throughput and efficiency for distributed machine learning clusters.",
                "category": "TECH",
                "region": "ASIA PACIFIC",
                "source_name": "Financial Times / WorldWire",
                "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80"
            }
        ]
    
    html = """
    <div id="prerender-container" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #0f172a; max-width: 1200px; margin: 0 auto; padding: 16px;">
        <header style="border-bottom: 3px double #0f172a; padding-bottom: 12px; margin-bottom: 24px; text-align: center;">
            <div style="font-size: 13px; text-transform: uppercase; letter-spacing: 2px; color: #dc2626; font-weight: 700; margin-bottom: 6px;">Global Real-Time Wire Service</div>
            <h1 style="font-family: Georgia, serif; font-size: 38px; font-weight: 900; margin: 0; letter-spacing: -0.5px;">WORLDWIRE</h1>
            <div style="font-size: 12px; color: #64748b; margin-top: 6px;">Live Dispatches & Analysis • Updated 24/7</div>
        </header>

        <section style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 40px;">
    """

    for a in articles:
        img_tag = f'<img src="{a["image_url"]}" alt="{a["title"]}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 12px;" />' if a.get("image_url") else ''
        cat = (a.get("category") or "WORLD").upper()
        region = (a.get("region") or "GLOBAL").upper()
        html += f"""
        <article style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            {img_tag}
            <div style="font-size: 11px; font-weight: 700; color: #dc2626; text-transform: uppercase; margin-bottom: 6px;">{cat} • {region}</div>
            <h2 style="font-family: Georgia, serif; font-size: 20px; line-height: 1.3; margin: 0 0 10px 0;">{a['title']}</h2>
            <p style="font-size: 14px; line-height: 1.6; color: #334155; margin: 0 0 12px 0;">{a.get('summary', '')}</p>
            <div style="font-size: 12px; color: #94a3b8; border-top: 1px solid #f1f5f9; padding-top: 8px;">Source: {a.get('source_name', 'WorldWire Wire Service')}</div>
        </article>
        """

    html += """
        </section>

        <footer style="border-top: 2px solid #0f172a; padding: 24px 0; text-align: center; margin-top: 40px; font-size: 13px; color: #475569;">
            <p style="margin-bottom: 12px;">
                <a href="?page=about" style="color: #0f172a; text-decoration: none; font-weight: 600; margin: 0 8px;">About Us</a> |
                <a href="?page=contact" style="color: #0f172a; text-decoration: none; font-weight: 600; margin: 0 8px;">Contact Bureau</a> |
                <a href="?page=privacy" style="color: #0f172a; text-decoration: none; font-weight: 600; margin: 0 8px;">Privacy Policy</a> |
                <a href="?page=terms" style="color: #0f172a; text-decoration: none; font-weight: 600; margin: 0 8px;">Terms of Service</a>
            </p>
            <p>© 2026 WORLDWIRE INTERNATIONAL MEDIA NETWORK. All rights reserved.</p>
        </footer>
    </div>
    """
    return html

def inject_prerender():
    try:
        static_dir = os.path.join(os.path.dirname(st_mod.__file__), 'static')
        index_path = os.path.join(static_dir, 'index.html')
        if not os.path.exists(index_path):
            return
        
        with open(index_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Inject Meta Tag
        meta_tag = '<meta name="google-adsense-account" content="ca-pub-6145233805932455">'
        if "google-adsense-account" not in html:
            html = html.replace("<head>", f"<head>\n    {meta_tag}")

        # 2. Inject AdSense script
        ads_tag = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6145233805932455" crossorigin="anonymous"></script>'
        if "ca-pub-6145233805932455" not in html:
            html = html.replace("</head>", f"{ads_tag}\n</head>")

        # 3. Inject GoatCounter analytics
        gc_tag = '<script data-goatcounter="https://mytomboy360.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
        if "mytomboy360.goatcounter.com" not in html:
            html = html.replace("</head>", f"{gc_tag}\n</head>")

        # 4. Inject semantic HTML content inside <div id="root"></div> if empty
        if '<div id="root"></div>' in html:
            content = build_prerendered_html()
            if content:
                html = html.replace('<div id="root"></div>', f'<div id="root">{content}</div>')

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # 5. Copy ads.txt into static directory
        ads_src = os.path.join(os.path.dirname(__file__), 'ads.txt')
        if os.path.exists(ads_src):
            import shutil
            shutil.copy(ads_src, os.path.join(static_dir, 'ads.txt'))

        print("Prerendered HTML, AdSense meta/script, and ads.txt injected successfully into index.html")
    except Exception as e:
        print(f"Error injecting prerender: {e}")

if __name__ == "__main__":
    inject_prerender()
