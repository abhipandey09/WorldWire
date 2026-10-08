import os
from datetime import datetime, timezone
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from dotenv import load_dotenv

import database
import scheduler

load_dotenv()

# Streamlit Page Config - Consumer Media Site
st.set_page_config(
    page_title="WorldWire | Latest World News & Breaking Headlines",
    page_icon="🗞️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize background 5-hour news ingestion daemon silently in background
scheduler.start_scheduler()

# Silent automatic background synchronization (every 60 seconds) without any UI clutter
st_autorefresh(interval=60 * 1000, key="silent_feed_sync")

# Custom CSS for a BBC News / Reuters-style Editorial Experience
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400&family=Inter:wght@400;500;600;700&display=swap');

    /* Global Typography */
    body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hide Streamlit default chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1280px !important;
    }

    /* Masthead Navigation */
    .top-edition-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        padding-bottom: 8px;
        margin-bottom: 16px;
        font-size: 0.8rem;
        color: #888888;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .masthead-title-container {
        text-align: center;
        padding: 8px 0 20px 0;
        border-bottom: 3px solid #b91c1c;
        margin-bottom: 20px;
    }
    .masthead-brand {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 3.2rem;
        font-weight: 900;
        letter-spacing: -0.03em;
        line-height: 1;
        margin: 0;
        color: var(--text-color);
        display: inline-block;
    }
    .masthead-tagline {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        color: #71717a;
        margin-top: 6px;
    }

    /* Live Ticker */
    .ticker-bar {
        background-color: #b91c1c;
        color: white;
        padding: 8px 16px;
        border-radius: 4px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 0.85rem;
        margin-bottom: 24px;
    }
    .ticker-label {
        font-weight: 800;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        background: #991b1b;
        padding: 2px 8px;
        border-radius: 2px;
        font-size: 0.75rem;
    }
    .ticker-text {
        font-weight: 500;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* Category Tag */
    .cat-kicker {
        color: #b91c1c;
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 6px;
    }
    .meta-byline {
        font-size: 0.78rem;
        color: #71717a;
        margin-top: 8px;
        margin-bottom: 12px;
    }

    /* Lead Story Styling */
    .lead-headline {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 2.1rem;
        font-weight: 700;
        line-height: 1.25;
        margin-top: 4px;
        margin-bottom: 12px;
        color: var(--text-color);
    }
    .lead-summary {
        font-size: 1.05rem;
        line-height: 1.6;
        color: #52525b;
        margin-bottom: 16px;
    }

    /* Secondary Card Styling */
    .news-card-box {
        border-top: 2px solid rgba(128, 128, 128, 0.2);
        padding-top: 14px;
        margin-bottom: 24px;
    }
    .story-headline {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 1.25rem;
        font-weight: 700;
        line-height: 1.35;
        margin-top: 4px;
        margin-bottom: 8px;
        color: var(--text-color);
    }
    .story-summary {
        font-size: 0.88rem;
        line-height: 1.5;
        color: #71717a;
        margin-bottom: 10px;
    }

    /* Article Full Reader Mode */
    .reader-container {
        max-width: 860px;
        margin: 0 auto;
        padding: 20px 0;
    }
    .reader-headline {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 2.5rem;
        font-weight: 900;
        line-height: 1.2;
        margin: 12px 0 16px 0;
    }
    .reader-subhead {
        font-size: 1.2rem;
        color: #52525b;
        line-height: 1.5;
        font-style: italic;
        margin-bottom: 20px;
    }
    .reader-paragraph {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 1.12rem;
        line-height: 1.85;
        margin-bottom: 1.5rem;
    }

    /* Public Footer */
    .media-footer {
        border-top: 3px solid #b91c1c;
        margin-top: 48px;
        padding-top: 24px;
        padding-bottom: 24px;
        text-align: center;
        color: #71717a;
        font-size: 0.82rem;
    }
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 12px;
        font-weight: 500;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 0.05em;
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
        return f"{seconds // 60} mins ago"
    elif seconds < 86400:
        return f"{seconds // 3600} hrs ago"
    else:
        return f"{seconds // 86400} days ago"

# Manage Reading View State in session_state
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None

# TOP EDITION & DATE BAR
current_date_str = datetime.now(timezone.utc).strftime("%A, %B %d, %Y")
st.markdown(f"""
<div class="top-edition-bar">
    <div><b>World Edition</b> &nbsp;|&nbsp; {current_date_str}</div>
    <div>24/7 Global Wire • Live Updates</div>
</div>
""", unsafe_allow_html=True)

# MASTHEAD
st.markdown("""
<div class="masthead-title-container">
    <h1 class="masthead-brand">WORLDWIRE</h1>
    <div class="masthead-tagline">The International Journal of Global Events & Breaking Intelligence</div>
</div>
""", unsafe_allow_html=True)

# CATEGORY NAVIGATION BAR (BBC / Reuters Style)
nav_categories = ["Top Stories", "World", "Technology", "Business & Economy", "Science", "Geopolitics", "Politics"]
if "active_category" not in st.session_state:
    st.session_state.active_category = "Top Stories"

cols = st.columns(len(nav_categories) + 1)
for i, cat in enumerate(nav_categories):
    with cols[i]:
        btn_type = "primary" if st.session_state.active_category == cat else "secondary"
        if st.button(cat, key=f"nav_{cat}", use_container_width=True, type=btn_type):
            st.session_state.active_category = cat
            st.session_state.selected_article_id = None
            st.rerun()

with cols[-1]:
    search_query = st.text_input("🔍", placeholder="Search news...", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# Check if user is in Full Article Reader View
if st.session_state.selected_article_id is not None:
    # Full Article Reader Mode
    all_articles = database.get_articles(limit=100)
    current_art = next((a for a in all_articles if a['id'] == st.session_state.selected_article_id), None)
    
    if current_art:
        if st.button("← Back to Top Stories", type="secondary"):
            st.session_state.selected_article_id = None
            st.rerun()
            
        st.markdown(f"""
        <div class="reader-container">
            <div class="cat-kicker">{current_art.get('category', 'WORLD')} &nbsp;•&nbsp; {current_art.get('region', 'GLOBAL')}</div>
            <h1 class="reader-headline">{current_art['title']}</h1>
            <p class="reader-subhead">{current_art['summary']}</p>
            <div class="meta-byline">
                Published <b>{format_time_ago(current_art['published_at'])}</b> &nbsp;|&nbsp; 
                Reporting by <b>{current_art.get('source_name', 'WorldWire International Desk')}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if current_art.get("image_url"):
            st.image(current_art["image_url"], use_container_width=True)
            st.caption(f"Photo: Editorial Wire / {current_art.get('source_name', 'WorldWire')}")
            
        paragraphs = current_art.get("content", "").split("\n\n")
        st.markdown('<div class="reader-container">', unsafe_allow_html=True)
        for p in paragraphs:
            if p.strip():
                st.markdown(f'<p class="reader-paragraph">{p.strip()}</p>', unsafe_allow_html=True)
        
        if current_art.get("source_url"):
            st.markdown(f"""
            <div style="border-top: 1px solid rgba(128,128,128,0.2); padding-top: 16px; margin-top: 24px; font-size: 0.85rem; color: #71717a;">
                Original press wire reference: <a href="{current_art['source_url']}" target="_blank" style="color: #b91c1c; text-decoration: underline;">{current_art.get('source_name', 'Source')}</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        if st.button("← Return to All Stories", type="secondary"):
            st.session_state.selected_article_id = None
            st.rerun()

    else:
        st.session_state.selected_article_id = None
        st.rerun()

else:
    # MAIN HOMEPAGE / CATEGORY FEED
    filter_category = None
    if st.session_state.active_category != "Top Stories":
        filter_category = st.session_state.active_category.replace(" & Economy", "").replace("Business", "Economy")

    articles = database.get_articles(limit=30, category=filter_category, search=search_query)

    if not articles:
        st.info("No articles currently found in this section. Please check back shortly as news is continuously gathered.")
    else:
        # LIVE TICKER BAR (Showing latest breaking headline)
        latest_story = articles[0]
        st.markdown(f"""
        <div class="ticker-bar">
            <span class="ticker-label">BREAKING</span>
            <span class="ticker-text">{latest_story['title']}</span>
        </div>
        """, unsafe_allow_html=True)

        # --- LEAD STORY / SPLASH SECTION ---
        hero = articles[0]
        t_ago = format_time_ago(hero['published_at'])
        
        col_img, col_text = st.columns([7, 5])
        with col_img:
            if hero.get("image_url"):
                st.image(hero["image_url"], use_container_width=True)
        with col_text:
            st.markdown(f"""
            <div class="cat-kicker">{hero.get('category', 'WORLD').upper()} • {hero.get('region', 'GLOBAL').upper()}</div>
            <h2 class="lead-headline">{hero['title']}</h2>
            <p class="lead-summary">{hero['summary']}</p>
            <div class="meta-byline">
                ⏱️ {t_ago} &nbsp;|&nbsp; <b>{hero.get('source_name', 'WorldWire Desk')}</b>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Read Full Story →", key=f"read_hero_{hero['id']}", type="primary"):
                st.session_state.selected_article_id = hero['id']
                st.rerun()

        st.markdown("<br><hr style='border: none; border-top: 1px solid rgba(128,128,128,0.2);'><br>", unsafe_allow_html=True)

        # --- SECONDARY & MORE TOP STORIES GRID ---
        remaining = articles[1:] if len(articles) > 1 else []
        if remaining:
            st.markdown("### LATEST DISPATCHES")
            
            # 3-Column Editorial Layout
            cols = st.columns(3)
            for i, item in enumerate(remaining):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div class="news-card-box">
                        <div class="cat-kicker">{item.get('category', 'WORLD').upper()}</div>
                        <div class="story-headline">{item['title']}</div>
                        <div class="story-summary">{item['summary']}</div>
                        <div class="meta-byline">⏱️ {format_time_ago(item['published_at'])} • {item.get('source_name', 'WorldWire')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if item.get("image_url"):
                        st.image(item["image_url"], use_container_width=True)
                        
                    if st.button("Read Article", key=f"read_grid_{item['id']}", use_container_width=True):
                        st.session_state.selected_article_id = item['id']
                        st.rerun()
                    
                    st.markdown("<br>", unsafe_allow_html=True)

# PUBLIC MEDIA FOOTER
st.markdown("""
<div class="media-footer">
    <div class="footer-links">
        <span>World</span> •
        <span>Business</span> •
        <span>Technology</span> •
        <span>Science</span> •
        <span>Editorial Guidelines</span> •
        <span>Terms of Service</span> •
        <span>Privacy Policy</span>
    </div>
    <div>© 2026 WORLDWIRE MEDIA GROUP. All rights reserved. The International News Service.</div>
</div>
""", unsafe_allow_html=True)
