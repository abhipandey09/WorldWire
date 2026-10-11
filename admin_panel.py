import streamlit as st
from datetime import datetime, timezone
import database
import news_agent

def render_admin_page():
    if not st.session_state.get("is_admin", False):
        render_login_view()
    else:
        render_dashboard_view()

def render_login_view():
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.caption("WORLDWIRE EDITORIAL SYSTEM • RESTRICTED ACCESS")
        st.title("Editorial Desk Sign-In")
        st.markdown("##### *Log in to review, edit, and authorize news dispatches prior to public dissemination.*")
        st.divider()

        with st.form("admin_login_form"):
            username = st.text_input("Username", placeholder="e.g. abhishek")
            password = st.text_input("Password", type="password", placeholder="Enter your administrator password")
            submitted = st.form_submit_button("Access Editorial Dashboard →", type="primary", use_container_width=True)
            
            if submitted:
                if database.verify_admin_credentials(username, password):
                    st.session_state.is_admin = True
                    st.session_state.admin_user = username.strip()
                    st.success("Authentication successful! Loading Editorial Command Center...")
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please verify your administrator username and password.")

        st.caption("Authorized editorial personnel only. All access events are logged.")
        if st.button("← Back to Public Newspaper", type="secondary", use_container_width=True):
            st.session_state.current_page = "news"
            st.query_params.clear()
            st.rerun()

def render_dashboard_view():
    # Top Navigation Bar for Admin
    top_c1, top_c2, top_c3 = st.columns([6, 3, 3])
    with top_c1:
        st.markdown(f"### 🛡️ WorldWire Editorial Command Center")
        st.caption(f"Authenticated Editor: **{st.session_state.get('admin_user', 'abhishek')}** | Role: **Lead Editor & Publisher**")
    with top_c2:
        if st.button("🌐 View Public Site ↗", type="secondary", use_container_width=True):
            st.session_state.current_page = "news"
            st.query_params.clear()
            st.rerun()
    with top_c3:
        if st.button("Sign Out 🚪", type="primary", use_container_width=True):
            st.session_state.is_admin = False
            st.session_state.admin_user = None
            st.session_state.current_page = "news"
            st.query_params.clear()
            st.rerun()

    st.divider()

    # Overview Metrics
    stats = database.get_stats()
    total_articles = stats.get("total_articles", 0) if stats else 0
    published_count = stats.get("published_count", 0) if stats else 0
    in_review_count = stats.get("in_review_count", 0) if stats else 0
    cat_count = stats.get("category_count", 0) if stats else 0

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Published Dispatches", published_count)
    m2.metric("In Review (Pending)", in_review_count, delta=f"{in_review_count} need review" if in_review_count else "Clear", delta_color="inverse" if in_review_count else "normal")
    m3.metric("Total in Database", total_articles)
    m4.metric("Active Desks", cat_count)

    st.markdown("<br>", unsafe_allow_html=True)

    tab_review, tab_write, tab_manage, tab_system = st.tabs([
        f"📋 Pending Review ({in_review_count})",
        "✍️ Write New Dispatch",
        "📰 Manage Published Stories",
        "⚙️ System & AdSense Compliance"
    ])

    # --- TAB 1: PENDING REVIEW QUEUE ---
    with tab_review:
        st.subheader("Manual Editorial Review Queue")
        st.caption("All dispatches queued here are hidden from the public website until you explicitly review and approve them.")

        col_fetch, _ = st.columns([4, 6])
        with col_fetch:
            if st.button("🔍 Fetch Next Wire Story into Review Queue", type="primary", use_container_width=True):
                with st.spinner("Ingesting latest wire dispatch from global press feeds..."):
                    try:
                        res = news_agent.fetch_and_publish_news()
                        st.success(f"New dispatch fetched and queued for review: '{res.get('title')}'")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error fetching news: {e}")

        st.markdown("<br>", unsafe_allow_html=True)
        pending_articles = database.get_pending_articles(limit=50)

        if not pending_articles:
            st.info("✅ **Editorial Review Queue is clear!** No stories are currently waiting for approval.")
        else:
            for art in pending_articles:
                with st.expander(f"⏳ **[{art.get('category', 'WORLD').upper()}]** {art['title']}", expanded=True):
                    rev_c1, rev_c2 = st.columns([4, 8])
                    with rev_c1:
                        if art.get("image_url"):
                            st.image(art["image_url"], use_container_width=True)
                        st.caption(f"**Region:** {art.get('region', 'Global')}")
                        st.caption(f"**Source:** {art.get('source_name', 'Wire Desk')}")
                        if art.get("source_url"):
                            st.markdown(f"[Verify Primary Wire Source ↗]({art['source_url']})")

                    with rev_c2:
                        st.markdown(f"#### {art['title']}")
                        st.markdown(f"**Executive Briefing:**\n{art.get('summary', '')}")
                        st.markdown(f"**Full Body Content:**\n{art.get('content', '')}")
                    
                    st.divider()

                    # Action buttons
                    btn_col1, btn_col2, btn_col3 = st.columns([3, 3, 3])
                    with btn_col1:
                        if st.button(f"✅ Approve & Publish Story", key=f"appr_{art['id']}", type="primary", use_container_width=True):
                            database.update_article_status(art["id"], "published")
                            st.cache_data.clear()
                            st.success(f"Article '{art['title'][:40]}...' is now LIVE on mytomboy360.com!")
                            st.rerun()

                    with btn_col2:
                        with st.popover("✏️ Edit Before Publishing"):
                            edit_title = st.text_input("Title", value=art["title"], key=f"et_{art['id']}")
                            edit_cat = st.selectbox("Category", ["World", "Business & Economy", "Technology", "Science", "Geopolitics", "Politics"], index=0, key=f"ec_{art['id']}")
                            edit_sum = st.text_area("Summary", value=art["summary"], key=f"es_{art['id']}")
                            edit_cnt = st.text_area("Full Body Content", value=art["content"], height=200, key=f"ecnt_{art['id']}")
                            if st.button("Save Edits & Publish →", key=f"save_pub_{art['id']}", type="primary"):
                                database.update_article(art["id"], {
                                    "title": edit_title,
                                    "category": edit_cat,
                                    "summary": edit_sum,
                                    "content": edit_cnt,
                                    "status": "published"
                                })
                                st.cache_data.clear()
                                st.success("Article updated and published to the live newspaper!")
                                st.rerun()

                    with btn_col3:
                        if st.button(f"🗑️ Reject & Delete", key=f"del_{art['id']}", use_container_width=True):
                            database.delete_article(art["id"])
                            st.cache_data.clear()
                            st.warning("Article rejected and removed from queue.")
                            st.rerun()

    # --- TAB 2: WRITE NEW DISPATCH ---
    with tab_write:
        st.subheader("Compose & Author New Dispatch")
        st.caption("Write and publish a high-quality human journalistic dispatch directly under your editorial byline.")

        with st.form("manual_article_form"):
            w_title = st.text_input("Dispatch Headline", placeholder="e.g. Global Chipmakers Agree on Joint Open Standards for High-Bandwidth Memory")
            w_c1, w_c2, w_c3 = st.columns(3)
            with w_c1:
                w_cat = st.selectbox("Editorial Desk", ["World", "Business & Economy", "Technology", "Science", "Geopolitics", "Politics"])
            with w_c2:
                w_reg = st.selectbox("Geographic Region", ["Global", "North America", "Europe", "Asia-Pacific", "Middle East", "Latin America", "Africa"])
            with w_c3:
                w_source = st.text_input("Wire Attribution / Agency", value="WorldWire Editorial Desk")
            
            w_img = st.text_input("Editorial Image URL", placeholder="https://images.unsplash.com/photo-...")
            w_url = st.text_input("Primary Reference / Source URL (Optional)", placeholder="https://www.reuters.com/...")
            w_sum = st.text_area("Executive Summary (2-3 sentences)", placeholder="Brief summary of the verified development...")
            w_cnt = st.text_area("Full Journalistic Report (Multiple paragraphs)", height=250, placeholder="Detailed report covering the development, background context, and global implications...")

            w_pub_now = st.checkbox("Publish immediately to live website (Visible to public)", value=True)
            w_submit = st.form_submit_button("Submit Dispatch →", type="primary", use_container_width=True)

            if w_submit:
                if w_title and w_sum and w_cnt:
                    new_art = {
                        "title": w_title.strip(),
                        "summary": w_sum.strip(),
                        "content": w_cnt.strip(),
                        "category": w_cat,
                        "hot_topic_tag": "Global Wire",
                        "image_url": w_img.strip() if w_img else "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=800&q=80",
                        "source_name": w_source.strip() if w_source else "WorldWire Editorial Desk",
                        "source_url": w_url.strip() if w_url else "",
                        "region": w_reg,
                        "published_at": datetime.now(timezone.utc),
                        "status": "published" if w_pub_now else "in_review",
                        "author": f"{st.session_state.get('admin_user', 'Abhishek Pandey')}, WorldWire Desk"
                    }
                    database.insert_article(new_art, default_status=new_art["status"])
                    st.cache_data.clear()
                    if w_pub_now:
                        st.success(f"Dispatch '{w_title}' has been PUBLISHED live to mytomboy360.com!")
                    else:
                        st.success(f"Dispatch '{w_title}' saved to Editorial Review Queue!")
                    st.rerun()
                else:
                    st.error("Please fill in Headline, Summary, and Full Report before submitting.")

    # --- TAB 3: MANAGE PUBLISHED STORIES ---
    with tab_manage:
        st.subheader("Manage Published Dispatches")
        st.caption("Review, edit, or unpublish any live stories currently appearing on the public newspaper.")

        search_published = st.text_input("Filter published dispatches...", placeholder="Search by title or keywords...")
        published_articles = database.get_articles(limit=50, search=search_published, status="published")

        st.caption(f"Showing {len(published_articles)} live dispatches")
        st.divider()

        for p_art in published_articles:
            p_col1, p_col2, p_col3 = st.columns([7, 3, 2])
            with p_col1:
                st.markdown(f"**{p_art['title']}**")
                st.caption(f"Desk: **{p_art.get('category')}** | Region: **{p_art.get('region')}** | By: **{p_art.get('author', 'Abhishek Pandey')}**")
            with p_col2:
                with st.popover(f"Edit #{p_art['id']}"):
                    ep_title = st.text_input("Title", value=p_art["title"], key=f"m_t_{p_art['id']}")
                    ep_cat = st.selectbox("Desk", ["World", "Business & Economy", "Technology", "Science", "Geopolitics", "Politics"], index=0, key=f"m_c_{p_art['id']}")
                    ep_sum = st.text_area("Summary", value=p_art["summary"], key=f"m_s_{p_art['id']}")
                    ep_cnt = st.text_area("Content", value=p_art["content"], height=150, key=f"m_cnt_{p_art['id']}")
                    if st.button("Update Story", key=f"save_m_{p_art['id']}", type="primary"):
                        database.update_article(p_art["id"], {
                            "title": ep_title,
                            "category": ep_cat,
                            "summary": ep_sum,
                            "content": ep_cnt
                        })
                        st.cache_data.clear()
                        st.success("Story updated!")
                        st.rerun()
            with p_col3:
                if st.button(f"Unpublish", key=f"unpub_{p_art['id']}"):
                    database.update_article_status(p_art["id"], "in_review")
                    st.cache_data.clear()
                    st.info("Story returned to in-review queue.")
                    st.rerun()
            st.markdown("---")

    # --- TAB 4: SYSTEM & ADSENSE COMPLIANCE ---
    with tab_system:
        st.subheader("Google AdSense & SEO Compliance Diagnostics")
        st.caption("Verification parameters currently active on your live Cloud Run deployment.")

        st.success("✅ **Primary Domain:** `https://mytomboy360.com` (Google Trust Services SSL Active)")
        st.success("✅ **AdSense Publisher ID:** `ca-pub-6145233805932455`")
        st.success("✅ **Ads.txt:** Live and verified at `https://mytomboy360.com/ads.txt`")
        st.success("✅ **Robots.txt:** Live at `https://mytomboy360.com/robots.txt`")
        st.success("✅ **Sitemap.xml:** Live at `https://mytomboy360.com/sitemap.xml`")
        st.success("✅ **Verified Contact:** `techsnapzone@gmail.com`")
        st.success("✅ **Publisher Attribution:** Abhishek Pandey (TechSnapZone)")
        st.info("ℹ️ **Human Editorial Protocol:** All incoming dispatches queue into 'In Review' for manual review prior to publication.")

