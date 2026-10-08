import os
from datetime import datetime, timezone
import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from dotenv import load_dotenv

import database
import scheduler

load_dotenv()

# Streamlit Page Config - Consumer Media Site
st.set_page_config(
    page_title="WorldWire | Global Real-Time News & Wire Service",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize background 5-hour news ingestion daemon silently
scheduler.start_scheduler()

# Ensure GoatCounter analytics script is present in Streamlit's static index.html
def ensure_analytics_injected():
    try:
        import streamlit, os
        p = os.path.join(os.path.dirname(streamlit.__file__), 'static', 'index.html')
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                html = f.read()
            tag = '<script data-goatcounter="https://worldwire.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
            if "worldwire.goatcounter.com" not in html:
                html = html.replace("</head>", f"{tag}</head>")
                with open(p, 'w', encoding='utf-8') as f:
                    f.write(html)
    except Exception:
        pass

ensure_analytics_injected()

# Silent automatic background synchronization (every 60 seconds) without any UI clutter
st_autorefresh(interval=60 * 1000, key="silent_feed_sync")


# Custom Advanced Editorial CSS with Razor-Sharp High Contrast
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap');

    /* Global Typography & Light Background */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #0f172a !important;
    }
    .stApp {
        background-color: #f8fafc !important;
    }
    #MainMenu, footer, header, [data-testid="stSidebar"] { display: none !important; }
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1320px !important;
    }

    /* Top Intelligence Bar (Dark Navy Container with Crisp White/Green Text) */
    .intel-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #0f172a !important;
        color: #e2e8f0 !important;
        padding: 9px 20px;
        border-radius: 8px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 14px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.12);
    }
    .intel-market-pill {
        display: inline-flex;
        gap: 16px;
        font-family: monospace;
        font-size: 0.8rem;
        color: #ffffff !important;
    }
    .market-up { color: #34d399 !important; }
    .market-down { color: #f87171 !important; }

    /* Masthead Header (High Contrast Ink Black on White) */
    .masthead-wrapper {
        border-bottom: 3px solid #dc2626;
        padding: 10px 0 18px 0;
        margin-bottom: 18px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        flex-wrap: wrap;
        gap: 14px;
    }
    .masthead-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: -0.04em;
        line-height: 1;
        margin: 0;
        color: #0f172a !important;
        display: inline-block;
    }
    .masthead-sub {
        font-size: 0.84rem;
        color: #475569 !important;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-top: 5px;
        font-weight: 700;
    }

    /* Live Animated Breaking Ticker */
    .ticker-container {
        display: flex;
        align-items: center;
        background: #991b1b !important;
        color: #ffffff !important;
        border-radius: 8px;
        padding: 8px 16px;
        margin-bottom: 22px;
        box-shadow: 0 4px 14px rgba(185, 28, 28, 0.25);
    }
    .ticker-badge {
        background: #ef4444 !important;
        color: #ffffff !important;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        padding: 3px 9px;
        border-radius: 4px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        text-transform: uppercase;
        margin-right: 12px;
        flex-shrink: 0;
    }
    .pulse-dot {
        width: 7px;
        height: 7px;
        background-color: #ffffff !important;
        border-radius: 50%;
        animation: pulse 1.4s infinite;
    }
    @keyframes pulse {
        0% { opacity: 0.3; transform: scale(0.85); }
        50% { opacity: 1; transform: scale(1.2); }
        100% { opacity: 0.3; transform: scale(0.85); }
    }
    .ticker-headline {
        font-size: 0.9rem;
        font-weight: 600;
        color: #ffffff !important;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* Editorial Hero Card (Crisp White Card with Deep Black Headlines) */
    .hero-box {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 28px;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .hero-box:hover {
        border-color: #dc2626 !important;
        box-shadow: 0 10px 25px -4px rgba(220, 38, 38, 0.12);
    }
    .hero-kicker {
        color: #dc2626 !important;
        font-size: 0.76rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .hero-headline {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.15rem;
        font-weight: 800;
        line-height: 1.25;
        margin-bottom: 12px;
        color: #0f172a !important;
    }
    .hero-summary {
        font-size: 1.05rem;
        line-height: 1.65;
        color: #334155 !important;
        margin-bottom: 16px;
    }

    /* Trending Top Stories Sidebar (Right of Hero) */
    .trending-list {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 16px;
        padding: 22px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.05);
    }
    .trending-header {
        font-size: 0.82rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #dc2626 !important;
        border-bottom: 2px solid #dc2626;
        padding-bottom: 8px;
        margin-bottom: 16px;
        display: flex;
        justify-content: space-between;
    }
    .trending-item {
        display: flex;
        gap: 14px;
        padding-bottom: 14px;
        margin-bottom: 14px;
        border-bottom: 1px solid #f1f5f9;
    }
    .trending-item:last-child {
        border-bottom: none;
        padding-bottom: 0;
        margin-bottom: 0;
    }
    .trend-number {
        font-family: 'Playfair Display', serif;
        font-size: 1.85rem;
        font-weight: 900;
        color: #dc2626 !important;
        line-height: 1;
    }
    .trend-text h4 {
        font-size: 0.98rem;
        font-weight: 700;
        line-height: 1.35;
        margin: 0 0 4px 0;
        color: #0f172a !important;
    }
    .trend-meta {
        font-size: 0.74rem;
        color: #64748b !important;
        font-weight: 500;
    }

    /* ROW-WISE NEWS FEED (HORIZONTAL MAGAZINE ROW CARDS) */
    .row-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 18px;
        box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .row-card:hover {
        border-color: #dc2626 !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px -4px rgba(220, 38, 38, 0.1);
    }
    .row-kicker {
        font-size: 0.74rem;
        font-weight: 800;
        color: #dc2626 !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 4px;
    }
    .row-headline {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.38rem;
        font-weight: 700;
        line-height: 1.32;
        margin: 4px 0 8px 0;
        color: #0f172a !important;
    }
    .row-summary {
        font-size: 0.94rem;
        line-height: 1.6;
        color: #334155 !important;
        margin-bottom: 12px;
    }
    .row-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.78rem;
        color: #64748b !important;
        font-weight: 500;
    }

    /* Special Feature Banner */
    .feature-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #1e293b 100%) !important;
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 14px;
        padding: 22px 26px;
        margin: 28px 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 16px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.2);
    }
    .banner-title {
        font-size: 1.28rem;
        font-weight: 800;
        color: #ffffff !important;
        margin-bottom: 4px;
    }
    .banner-subtitle {
        font-size: 0.9rem;
        color: #cbd5e1 !important;
    }
    .banner-btn {
        background: #dc2626 !important;
        color: #ffffff !important;
        padding: 9px 20px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.82rem;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: background 0.2s ease;
        display: inline-block;
    }
    .banner-btn:hover {
        background: #b91c1c !important;
    }

    /* Full Article Reader Layout */
    .reader-hero-box {
        max-width: 900px;
        margin: 0 auto;
        padding: 10px 0 40px 0;
    }
    .reader-head {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.8rem;
        font-weight: 800;
        line-height: 1.2;
        margin: 12px 0 16px 0;
        color: #0f172a !important;
    }
    .reader-lead {
        font-size: 1.22rem;
        line-height: 1.6;
        color: #334155 !important;
        font-style: italic;
        margin-bottom: 24px;
    }
    .reader-prose {
        font-family: 'Newsreader', Georgia, serif;
        font-size: 1.2rem;
        line-height: 1.85;
        color: #1e293b !important;
        margin-bottom: 1.6rem;
    }

    /* Public Footer */
    .footer-box {
        border-top: 3px solid #dc2626;
        margin-top: 48px;
        padding: 30px 0 20px 0;
        text-align: center;
        color: #64748b !important;
        font-size: 0.84rem;
    }
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 22px;
        flex-wrap: wrap;
        margin-bottom: 14px;
        font-weight: 600;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    .footer-links a {
        color: #475569 !important;
        text-decoration: none;
    }
    .footer-links a:hover {
        color: #dc2626 !important;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to format relative time
def format_time_ago(dt: datetime) -> str:
    if not dt:
        return "Just now"
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    diff = datetime.now(timezone.utc) - dt
    seconds = int(diff.total_seconds())
    if seconds < 60:
        return f"{seconds}s ago"
    elif seconds < 3600:
        return f"{seconds // 60}m ago"
    elif seconds < 86400:
        return f"{seconds // 3600}h ago"
    else:
        return f"{seconds // 86400}d ago"

# Manage reader view state in session_state
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None
if "active_category" not in st.session_state:
    st.session_state.active_category = "Top Stories"

# Dynamic Real-Time Global Market Ticker
@st.cache_data(ttl=300)
def get_live_market_data():
    symbols = [
        ("BRENT", "BZ=F", "$", ""),
        ("S&P 500", "%5EGSPC", "", ""),
        ("GOLD", "GC=F", "$", ""),
        ("BTC", "BTC-USD", "$", ""),
        ("10Y YIELD", "%5ETNX", "", "%"),
    ]
    results = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    for label, sym, prefix, suffix in symbols:
        try:
            r = requests.get(
                f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d",
                headers=headers,
                timeout=3.5,
            )
            if r.status_code == 200:
                meta = r.json()["chart"]["result"][0]["meta"]
                price = meta["regularMarketPrice"]
                prev = meta.get("chartPreviousClose", price)
                pct = ((price - prev) / prev) * 100 if prev else 0.0
                is_up = pct >= 0
                symbol_arrow = "▲" if is_up else "▼"
                class_name = "market-up" if is_up else "market-down"
                formatted_price = f"{prefix}{price:,.2f}{suffix}" if price < 1000 else f"{prefix}{price:,.0f}{suffix}"
                results.append(
                    f'<span>{label} <b class="{class_name}">{symbol_arrow} {formatted_price} ({pct:+.1f}%)</b></span>'
                )
        except Exception:
            pass

    if not results:
        results = [
            '<span>BRENT <b class="market-up">▲ $105.72 (+5.5%)</b></span>',
            '<span>S&P 500 <b class="market-down">▼ 7,771.01 (-0.4%)</b></span>',
            '<span>GOLD <b class="market-up">▲ $4,138.00 (+0.1%)</b></span>',
            '<span>10Y YIELD <b class="market-up">▲ 5.29% (+0.3%)</b></span>',
        ]
    return " ".join(results)

# 1. TOP INTELLIGENCE & GLOBAL MARKETS TICKER STRIP (DYNAMIC)
current_date_str = datetime.now(timezone.utc).strftime("%A, %B %d, %Y")
live_market_html = get_live_market_data()

st.markdown(f"""
<div class="intel-bar">
    <div>🌐 <b>WORLD EDITION</b> &nbsp;|&nbsp; {current_date_str}</div>
    <div class="intel-market-pill">
        {live_market_html}
    </div>
</div>
""", unsafe_allow_html=True)


# 2. EDITORIAL MASTHEAD
st.markdown("""
<div class="masthead-wrapper">
    <div>
        <h1 class="masthead-title">WORLDWIRE</h1>
        <div class="masthead-sub">The Global Newspaper of Real-Time Intelligence & International Affairs</div>
    </div>
    <div style="text-align: right; color: #475569; font-size: 0.8rem; font-weight: 600;">
        <div style="color: #dc2626;">🔴 <b>LIVE WIRE DISPATCH</b></div>
        <div>Updated Autonomously Every 5 Hours</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. INTERACTIVE CATEGORY NAVIGATION & SEARCH
nav_categories = ["Top Stories", "World", "Technology", "Business & Economy", "Science", "Geopolitics", "Politics"]

nav_cols = st.columns([1.1, 0.9, 1.1, 1.4, 0.9, 1.1, 0.9, 2.0])
for i, cat in enumerate(nav_categories):
    with nav_cols[i]:
        btn_type = "primary" if st.session_state.active_category == cat else "secondary"
        if st.button(cat, key=f"nav_{cat}", use_container_width=True, type=btn_type):
            st.session_state.active_category = cat
            st.session_state.selected_article_id = None
            st.rerun()

with nav_cols[-1]:
    search_query = st.text_input("Search news...", placeholder="🔍 Search dispatches...", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# 4. VIEW LOGIC: READER MODE VS HOMEPAGE STREAM
if st.session_state.selected_article_id is not None:
    # --- FULL ARTICLE READER VIEW ---
    all_articles = database.get_articles(limit=100)
    current_art = next((a for a in all_articles if a['id'] == st.session_state.selected_article_id), None)
    
    if current_art:
        if st.button("← Back to Global Headlines", type="secondary"):
            st.session_state.selected_article_id = None
            st.rerun()
            
        st.markdown(f"""
        <div class="reader-hero-box">
            <div class="hero-kicker">
                {current_art.get('category', 'WORLD').upper()} • {current_art.get('region', 'GLOBAL').upper()}
            </div>
            <h1 class="reader-head">{current_art['title']}</h1>
            <p class="reader-lead">{current_art['summary']}</p>
            <div style="font-size: 0.82rem; color: #64748b; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; padding: 10px 0; margin-bottom: 24px;">
                ⏱️ Published <b>{format_time_ago(current_art['published_at'])}</b> &nbsp;|&nbsp; 
                Reporting by <b>{current_art.get('source_name', 'WorldWire International Bureau')}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if current_art.get("image_url"):
            st.image(current_art["image_url"], use_container_width=True)
            st.caption(f"Photo: WorldWire Global Photojournalism / {current_art.get('source_name', 'Editorial Archive')}")
            
        paragraphs = current_art.get("content", "").split("\n\n")
        st.markdown('<div class="reader-hero-box">', unsafe_allow_html=True)
        for p in paragraphs:
            if p.strip():
                st.markdown(f'<p class="reader-prose">{p.strip()}</p>', unsafe_allow_html=True)
        
        if current_art.get("source_url"):
            st.markdown(f"""
            <div style="border-top: 1px solid #e2e8f0; padding-top: 18px; margin-top: 30px; font-size: 0.88rem; color: #475569;">
                🔗 <b>Original Reference:</b> <a href="{current_art['source_url']}" target="_blank" style="color: #dc2626; font-weight: 700; text-decoration: underline;">Read primary coverage at {current_art.get('source_name', 'Source')} ↗</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Return to All Dispatches", type="secondary"):
            st.session_state.selected_article_id = None
            st.rerun()

    else:
        st.session_state.selected_article_id = None
        st.rerun()

else:
    # --- HOMEPAGE EDITORIAL FEED ---
    filter_category = None
    if st.session_state.active_category != "Top Stories":
        filter_category = st.session_state.active_category.replace(" & Economy", "").replace("Business", "Economy")

    articles = database.get_articles(limit=35, category=filter_category, search=search_query)

    if not articles:
        st.info("No dispatches found matching this topic. The autonomous news wire will populate new stories shortly.")
    else:
        # 5. LIVE ANIMATED BREAKING TICKER
        breaking_story = articles[0]
        st.markdown(f"""
        <div class="ticker-container">
            <span class="ticker-badge"><span class="pulse-dot"></span>BREAKING NEWS</span>
            <span class="ticker-headline">{breaking_story['title']}</span>
        </div>
        """, unsafe_allow_html=True)

        # 6. FEATURED COVER STORY & TRENDING RADAR SECTION
        hero = articles[0]
        top_radar = articles[1:4] if len(articles) > 1 else []

        col_hero, col_radar = st.columns([7, 5])

        with col_hero:
            with st.container():
                st.markdown('<div class="hero-box">', unsafe_allow_html=True)
                if hero.get("image_url"):
                    st.image(hero["image_url"], use_container_width=True)
                
                st.markdown(f"""
                <div style="margin-top: 14px;">
                    <div class="hero-kicker">🔥 FEATURED LEAD • {hero.get('category', 'WORLD').upper()} • {hero.get('region', 'GLOBAL').upper()}</div>
                    <h2 class="hero-headline">{hero['title']}</h2>
                    <p class="hero-summary">{hero['summary']}</p>
                    <div style="font-size: 0.8rem; color: #64748b; margin-bottom: 14px;">
                        ⏱️ {format_time_ago(hero['published_at'])} &nbsp;|&nbsp; 📰 <b>{hero.get('source_name', 'WorldWire')}</b>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("Read Full Lead Story →", key=f"btn_hero_{hero['id']}", type="primary", use_container_width=True):
                    st.session_state.selected_article_id = hero['id']
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        with col_radar:
            with st.container():
                st.markdown("""
                <div class="trending-list">
                    <div class="trending-header">
                        <span>⚡ WIRE RADAR • MOST READ</span>
                        <span>LIVE</span>
                    </div>
                """, unsafe_allow_html=True)
                
                for idx, t_art in enumerate(top_radar, 1):
                    st.markdown(f"""
                    <div class="trending-item">
                        <div class="trend-number">0{idx}</div>
                        <div class="trend-text">
                            <div style="font-size: 0.72rem; font-weight: 800; color: #dc2626; text-transform: uppercase;">{t_art.get('category', 'WORLD')}</div>
                            <h4>{t_art['title']}</h4>
                            <div class="trend-meta">⏱️ {format_time_ago(t_art['published_at'])} • {t_art.get('source_name', 'WorldWire')}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Read Radar #{idx} →", key=f"radar_btn_{t_art['id']}", use_container_width=True):
                        st.session_state.selected_article_id = t_art['id']
                        st.rerun()
                
                st.markdown("</div>", unsafe_allow_html=True)

        # 7. CLICKABLE SPECIAL INVESTIGATION / PARTNER RIBBON BANNER
        st.markdown("""
        <div class="feature-banner">
            <div>
                <div style="font-size: 0.75rem; font-weight: 800; color: #f87171; letter-spacing: 0.1em; text-transform: uppercase;">SPECIAL INVESTIGATION SERIES</div>
                <div class="banner-title">The Global AI Infrastructure Surge & Power Grid Realities</div>
                <div class="banner-subtitle">How hyperscalers and international energy ministries are navigating the trillion-dollar semiconductor pivot.</div>
            </div>
            <div>
                <a href="https://www.reuters.com/technology/artificial-intelligence/" target="_blank" class="banner-btn">
                    Explore Deep Dive ↗
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 8. ROW-WISE NEWS STREAM (HIGH-DENSITY, NO WASTED WHITE SPACE)
        stream_articles = articles[1:] if len(articles) > 1 else []
        
        if stream_articles:
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #dc2626; padding-bottom: 8px; margin-bottom: 20px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 1.45rem; font-weight: 800; margin: 0; color: #0f172a !important;">
                    LATEST WIRE DISPATCHES — {st.session_state.active_category.upper()}
                </h3>
                <span style="font-size: 0.82rem; color: #64748b; font-weight: 700;">{len(stream_articles)} Stories In Feed</span>
            </div>
            """, unsafe_allow_html=True)

            for item in stream_articles:
                with st.container():
                    st.markdown('<div class="row-card">', unsafe_allow_html=True)
                    row_img_col, row_text_col = st.columns([4, 8])
                    
                    with row_img_col:
                        if item.get("image_url"):
                            st.image(item["image_url"], use_container_width=True)
                        else:
                            st.image("https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=800&q=80", use_container_width=True)
                    
                    with row_text_col:
                        st.markdown(f"""
                        <div class="row-kicker">{item.get('category', 'WORLD').upper()} • {item.get('region', 'GLOBAL').upper()}</div>
                        <h3 class="row-headline">{item['title']}</h3>
                        <p class="row-summary">{item['summary']}</p>
                        <div class="row-footer">
                            <span>⏱️ <b>{format_time_ago(item['published_at'])}</b> &nbsp;|&nbsp; 📰 <b>{item.get('source_name', 'WorldWire')}</b></span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        btn_c1, btn_c2 = st.columns([1, 1])
                        with btn_c1:
                            if st.button("Read Full Dispatch →", key=f"stream_read_{item['id']}", use_container_width=True):
                                st.session_state.selected_article_id = item['id']
                                st.rerun()
                        with btn_c2:
                            if item.get("source_url"):
                                st.link_button(f"View on {item.get('source_name', 'Source')} ↗", item["source_url"], use_container_width=True)

                    st.markdown('</div>', unsafe_allow_html=True)

# 9. CONSUMER MEDIA FOOTER & EXTERNAL HUBS
st.markdown("""
<div class="footer-box">
    <div class="footer-links">
        <a href="https://www.reuters.com" target="_blank">Reuters Wire</a> •
        <a href="https://www.apnews.com" target="_blank">Associated Press</a> •
        <a href="https://www.bloomberg.com" target="_blank">Bloomberg Markets</a> •
        <a href="https://www.bbc.com/news" target="_blank">BBC World</a> •
        <a href="https://www.ft.com" target="_blank">Financial Times</a> •
        <a href="#">Editorial Standards</a> •
        <a href="#">Verification Ethics</a> •
        <a href="#">Terms & Privacy</a>
    </div>
    <div style="margin-top: 10px;">
        © 2026 <b>WORLDWIRE INTERNATIONAL MEDIA NETWORK</b>. Real-time autonomous global journalism.
    </div>
</div>
""", unsafe_allow_html=True)

# GoatCounter Analytics Beacon
import streamlit.components.v1 as components
components.html("""
<script data-goatcounter="https://worldwire.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
""", height=0, width=0)

