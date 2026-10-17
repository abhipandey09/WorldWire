import streamlit as st
from streamlit_autorefresh import st_autorefresh
import scheduler
from job_store import get_approved_jobs, get_job_by_id, get_job_stats
import admin_panel
from pages_content import ABOUT_PAGE_MD, CONTACT_PAGE_MD, PRIVACY_PAGE_MD, TERMS_PAGE_MD
from ai_matcher import match_candidate_jobs

# Streamlit Page Configuration
st.set_page_config(
    page_title="WORKWIRE | Verified Tech & AI Careers India & US",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Start background 12-hour job scraping daemon
scheduler.start_scheduler()

# Ensure static site pre-rendering, sitemap, legal pages, and AdSense tags are synchronized
def ensure_static_assets():
    try:
        from prerender import generate_all_static_pages
        generate_all_static_pages()
    except Exception:
        pass

ensure_static_assets()

# Helper to render clean HTML blocks
def html_block(content: str):
    cleaned = "\n".join(line.strip() for line in content.strip().splitlines())
    st.markdown(cleaned, unsafe_allow_html=True)

# Custom High-Tech Styling for WorkWire
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #0f172a;
    }

    /* Top Announcement Intel Bar */
    .ww-top-bar {
        background: #090d16;
        color: #94a3b8;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.04em;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .ww-top-badge {
        background: #1e293b;
        color: #38bdf8;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 700;
        margin-right: 8px;
        text-transform: uppercase;
    }
    
    /* Brand Masthead */
    .ww-masthead {
        border-bottom: 2px solid #0f172a;
        padding-bottom: 16px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        flex-wrap: wrap;
        gap: 16px;
    }
    .ww-brand-title {
        font-size: 36px;
        font-weight: 900;
        color: #0f172a;
        letter-spacing: -0.04em;
        line-height: 1;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .ww-brand-badge {
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
        color: #ffffff;
        font-size: 11px;
        font-weight: 800;
        padding: 4px 10px;
        border-radius: 9999px;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    .ww-brand-sub {
        font-size: 14px;
        color: #475569;
        font-weight: 600;
        margin-top: 6px;
    }
    
    /* Navigation Bar */
    .ww-nav-bar {
        display: flex;
        gap: 12px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 12px;
        margin-bottom: 24px;
        overflow-x: auto;
        white-space: nowrap;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
    }
    .ww-nav-bar a {
        color: #334155;
        text-decoration: none;
        padding: 6px 12px;
        border-radius: 6px;
        transition: all 0.15s ease;
    }
    .ww-nav-bar a:hover {
        background: #f1f5f9;
        color: #0f172a;
    }
    .ww-nav-bar a.active {
        background: #0f172a;
        color: #ffffff;
    }

    /* Hero Tech Banner */
    .ww-hero {
        background: linear-gradient(135deg, #090d16 0%, #111827 50%, #1e1b4b 100%);
        color: #ffffff;
        padding: 36px 32px;
        border-radius: 12px;
        margin-bottom: 28px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    .ww-hero-pill {
        display: inline-block;
        background: rgba(37, 99, 235, 0.25);
        border: 1px solid rgba(96, 165, 250, 0.4);
        color: #93c5fd;
        font-size: 11px;
        font-weight: 800;
        padding: 4px 12px;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 12px;
    }
    .ww-hero-title {
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.2;
        margin-bottom: 12px;
    }
    .ww-hero-desc {
        font-size: 15px;
        color: #cbd5e1;
        line-height: 1.6;
        max-width: 820px;
    }

    /* Metric Badges */
    .ww-stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 12px;
        margin-bottom: 24px;
    }
    .ww-stat-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px 18px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    }
    .ww-stat-label {
        font-size: 11px;
        text-transform: uppercase;
        font-weight: 700;
        color: #64748b;
        letter-spacing: 0.05em;
    }
    .ww-stat-val {
        font-size: 22px;
        font-weight: 800;
        color: #0f172a;
        margin-top: 2px;
    }

    /* Job Card Styling */
    .ww-job-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 22px 24px;
        margin-bottom: 16px;
        transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.03);
    }
    .ww-job-card:hover {
        border-color: #93c5fd;
        box-shadow: 0 8px 20px -4px rgba(37, 99, 235, 0.1);
        transform: translateY(-1px);
    }
    .ww-card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 12px;
    }
    .ww-company-flex {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .ww-company-logo {
        width: 44px;
        height: 44px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        background: #f8fafc;
        object-fit: contain;
        padding: 4px;
    }
    .ww-job-title {
        font-size: 20px;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.02em;
        line-height: 1.3;
        margin: 4px 0 2px 0;
    }
    .ww-req-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 600;
        color: #1e40af;
        background: #dbeafe;
        padding: 2px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    .ww-ats-badge {
        font-size: 11px;
        font-weight: 700;
        color: #475569;
        background: #f1f5f9;
        padding: 2px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    .ww-salary-badge {
        font-size: 13px;
        font-weight: 800;
        color: #065f46;
        background: #d1fae5;
        border: 1px solid #a7f3d0;
        padding: 4px 10px;
        border-radius: 6px;
        display: inline-block;
    }
    .ww-tag-chip {
        display: inline-block;
        background: #f1f5f9;
        color: #334155;
        font-size: 11px;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 4px;
        margin-right: 6px;
        margin-top: 6px;
    }
    .ww-match-score-badge {
        font-size: 16px;
        font-weight: 900;
        color: #ffffff;
        background: linear-gradient(135deg, #16a34a 0%, #15803d 100%);
        padding: 6px 14px;
        border-radius: 9999px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        box-shadow: 0 2px 8px rgba(22, 163, 74, 0.3);
    }

    /* Footer */
    .ww-footer {
        border-top: 3px solid #2563eb;
        margin-top: 48px;
        padding: 32px 16px 24px 16px;
        text-align: center;
        color: #64748b;
        font-size: 13px;
        background: #ffffff;
        border-radius: 12px;
    }
    .ww-footer a {
        margin: 0 10px;
        font-weight: 600;
        color: #0f172a;
        text-decoration: none;
    }
    .ww-footer a:hover {
        color: #2563eb;
    }
</style>
""", unsafe_allow_html=True)

# Top Bar Header Component
def render_header():
    html_block("""
    <div class="ww-top-bar">
        <div>
            <span class="ww-top-badge">OFFICIAL VERIFIED FEED</span>
            <b>WORKWIRE CAREER DESK</b> &nbsp;•&nbsp; DIRECT ATS VACANCIES IN INDIA 🇮🇳 &amp; UNITED STATES 🇺🇸
        </div>
        <div>
            <span style="color: #38bdf8;">●</span> PUBLISHED AT <b>MYTOMBOY360.COM</b>
        </div>
    </div>
    <div class="ww-masthead">
        <div>
            <div class="ww-brand-title">
                <a href="/" style="color: #0f172a; text-decoration: none;">WORKWIRE</a>
                <span class="ww-brand-badge">⚡ 100% HUMAN VETTED</span>
            </div>
            <div class="ww-brand-sub">Curated High-Impact Software Engineering, AI &amp; Cloud Infrastructure Opportunities</div>
        </div>
        <div style="text-align: right; font-size: 12px; color: #64748b; font-weight: 600;">
            <div style="color: #2563eb; font-weight: 800;">VERIFIED BY EDITORIAL DESK</div>
            <div>Publisher: Abhishek Pandey (TechSnapZone)</div>
        </div>
    </div>
    <div class="ww-nav-bar">
        <a href="/">💼 Browse All Positions</a>
        <a href="/about.html">About Bureau</a>
        <a href="/contact.html">Contact Us</a>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms &amp; Safety</a>
        <a href="/?page=admin">Editorial Staff 🔒</a>
    </div>
    """)

# Footer Component
def render_footer():
    html_block("""
    <div class="ww-footer">
        <div style="margin-bottom: 14px;">
            <a href="/">All Opportunities</a> |
            <a href="/about.html">About Us</a> |
            <a href="/contact.html">Contact Bureau</a> |
            <a href="/privacy.html">Privacy Policy</a> |
            <a href="/terms.html">Terms of Service</a> |
            <a href="/?page=admin">Editorial Staff 🔒</a>
        </div>
        <p>© 2026 <b>WORKWIRE CAREER NETWORK</b> • Published at <b>mytomboy360.com</b> by Abhishek Pandey (TechSnapZone).</p>
        <p style="margin-top: 6px; font-size: 12px; color: #94a3b8;">
            Direct corporate ATS integration: Workday, Greenhouse, Lever, Ashby. Candidate fee: ₹0 / $0 Free.<br>
            Editorial disclosures &amp; AdSense compliance: <a href="mailto:techsnapzone@gmail.com" style="color: #2563eb; font-weight: 700; text-decoration: none;">techsnapzone@gmail.com</a>
        </p>
    </div>
    """)

# ROUTING LOGIC BASED ON QUERY PARAMS
current_page = st.query_params.get("page", "")

# 1. Admin Route: /?page=admin
if current_page == "admin":
    admin_panel.render_admin()

# 2. Informational & Legal Pages
elif current_page == "about":
    render_header()
    st.markdown(ABOUT_PAGE_MD)
    render_footer()

elif current_page == "contact":
    render_header()
    st.markdown(CONTACT_PAGE_MD)
    render_footer()

elif current_page == "privacy":
    render_header()
    st.markdown(PRIVACY_PAGE_MD)
    render_footer()

elif current_page == "terms":
    render_header()
    st.markdown(TERMS_PAGE_MD)
    render_footer()

# 3. Dedicated Job Detail View (if ?job=job-101 or ?job=NV-JR1982731)
elif "job" in st.query_params:
    render_header()
    job_param = st.query_params.get("job")
    job = get_job_by_id(job_param)
    if not job:
        st.error(f"Position `{job_param}` not found or has been archived.")
        st.link_button("← Return to All Opportunities", "/")
    else:
        country_flag = "🇮🇳" if job.get("country") == "India" else "🇺🇸"
        
        st.markdown(f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 28px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(15,23,42,0.05);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
                <div style="display: flex; align-items: center; gap: 14px;">
                    <img src="{job.get('company_logo', 'https://www.google.com/s2/favicons?domain=google.com&sz=128')}" alt="{job['company']}" style="width: 48px; height: 48px; border-radius: 8px; border: 1px solid #e2e8f0; object-fit: contain; padding: 4px; background: #f8fafc;" onerror="this.src='https://www.google.com/s2/favicons?domain=google.com&sz=128'">
                    <div>
                        <div style="font-size: 12px; font-weight: 800; color: #2563eb; text-transform: uppercase;">
                            {country_flag} {job.get('country', 'GLOBAL').upper()} • {job.get('department', 'ENGINEERING').upper()}
                        </div>
                        <h1 style="font-size: 26px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">{job['title']}</h1>
                        <div style="font-size: 15px; font-weight: 600; color: #475569;">
                            🏢 {job['company']} &nbsp;•&nbsp; 📍 {job['location']}
                        </div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 15px; font-weight: 800; color: #065f46; background: #d1fae5; border: 1px solid #a7f3d0; padding: 6px 14px; border-radius: 6px;">
                        💰 {job.get('salary_range', 'Competitive Market Rate')}
                    </div>
                    <div style="margin-top: 6px; font-size: 12px; color: #64748b;">
                        Requisition: <code style="font-family: monospace; font-weight: 700; color: #1e40af;">#{job.get('req_id', job['id'])}</code>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        c_act1, c_act2 = st.columns([2, 5])
        with c_act1:
            st.link_button(f"🚀 Apply on {job['company']} ATS ↗", job['apply_url'], type="primary", use_container_width=True)
        with c_act2:
            st.link_button("← Back to All Opportunities", "/", use_container_width=False)
        
        st.markdown("---")
        st.markdown(job.get("description", ""))
    render_footer()

# 4. Main Job Directory Homepage & AI Copilot
else:
    render_header()

    # Tech Hero Section
    html_block("""
    <div class="ww-hero">
        <div style="position: relative; z-index: 2;">
            <div class="ww-hero-pill">⚡ VERIFIED OPPORTUNITIES DESK</div>
            <div class="ww-hero-title">Curated Technology &amp; Leadership Opportunities in India &amp; United States</div>
            <div class="ww-hero-desc">
                Every position is reviewed by <b>Abhishek Pandey (TechSnapZone)</b>. We filter out speculative ghost postings, verify official ATS requisition endpoints, and showcase verified compensation ranges across top tech hubs.
            </div>
        </div>
    </div>
    """)

    # Key Metrics Highlights
    stats = get_job_stats()
    html_block(f"""
    <div class="ww-stats-grid">
        <div class="ww-stat-card">
            <div class="ww-stat-label">Active Verified Openings</div>
            <div class="ww-stat-val">🟢 {stats['total_approved']}</div>
        </div>
        <div class="ww-stat-card">
            <div class="ww-stat-label">India Tech Hubs</div>
            <div class="ww-stat-val">🇮🇳 {stats['india_jobs']}</div>
        </div>
        <div class="ww-stat-card">
            <div class="ww-stat-label">US Tech Corridors</div>
            <div class="ww-stat-val">🇺🇸 {stats['us_jobs']}</div>
        </div>
        <div class="ww-stat-card">
            <div class="ww-stat-label">Candidate Fee</div>
            <div class="ww-stat-val">₹0 / $0 Free</div>
        </div>
    </div>
    """)

    # Primary Navigation Tabs
    tab_browse, tab_ai_copilot = st.tabs([
        f"💼 Browse Verified Opportunities ({stats['total_approved']})",
        "🤖 AI Career Copilot & Matcher"
    ])

    # ==========================================
    # TAB 1: BROWSE JOBS WITH REACTIVE FILTERS
    # ==========================================
    with tab_browse:
        # Initialize filter state
        if "f_search" not in st.session_state:
            st.session_state["f_search"] = ""
        if "f_country" not in st.session_state:
            st.session_state["f_country"] = "All Locations"
        if "f_dept" not in st.session_state:
            st.session_state["f_dept"] = "All Categories"

        # Quick preset pills
        st.write("##### Quick Filters:")
        qp1, qp2, qp3, qp4, qp5, qp6, qp7 = st.columns(7)
        with qp1:
            if st.button("🌐 All Roles", use_container_width=True):
                st.session_state["f_search"] = ""
                st.session_state["f_country"] = "All Locations"
                st.session_state["f_dept"] = "All Categories"
                st.rerun()
        with qp2:
            if st.button("🇮🇳 India Hubs", use_container_width=True):
                st.session_state["f_country"] = "India"
                st.session_state["f_search"] = ""
                st.rerun()
        with qp3:
            if st.button("🇺🇸 US Corridors", use_container_width=True):
                st.session_state["f_country"] = "United States"
                st.session_state["f_search"] = ""
                st.rerun()
        with qp4:
            if st.button("🤖 AI / GenAI", use_container_width=True):
                st.session_state["f_dept"] = "AI & Machine Learning"
                st.session_state["f_search"] = ""
                st.rerun()
        with qp5:
            if st.button("☁️ Cloud & SRE", use_container_width=True):
                st.session_state["f_dept"] = "DevOps & Cloud"
                st.session_state["f_search"] = ""
                st.rerun()
        with qp6:
            if st.button("💻 Software Eng", use_container_width=True):
                st.session_state["f_dept"] = "Software Engineering"
                st.session_state["f_search"] = ""
                st.rerun()
        with qp7:
            if st.button("🔄 Reset All", use_container_width=True):
                st.session_state["f_search"] = ""
                st.session_state["f_country"] = "All Locations"
                st.session_state["f_dept"] = "All Categories"
                st.rerun()

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        # Reactive Input Controls
        col_search, col_country, col_dept = st.columns([3, 1.5, 2])
        with col_search:
            search_query = st.text_input(
                "🔍 Search by Title, Company, Skills, or Requisition ID",
                value=st.session_state["f_search"],
                placeholder="e.g. Python, NVIDIA, AWS, Slurm, NV-JR1982731, Kubernetes...",
                key="input_search_box"
            )
            st.session_state["f_search"] = search_query

        with col_country:
            country_options = ["All Locations", "India", "United States"]
            country_idx = country_options.index(st.session_state["f_country"]) if st.session_state["f_country"] in country_options else 0
            selected_country = st.selectbox(
                "📍 Region Filter",
                country_options,
                index=country_idx,
                key="select_country_box"
            )
            st.session_state["f_country"] = selected_country

        with col_dept:
            dept_options = [
                "All Categories",
                "Software Engineering",
                "AI & Machine Learning",
                "DevOps & Cloud",
                "Data & Analytics",
                "Product & Design",
                "Security & Trust",
                "Finance & Analytics"
            ]
            dept_idx = dept_options.index(st.session_state["f_dept"]) if st.session_state["f_dept"] in dept_options else 0
            selected_dept = st.selectbox(
                "💼 Department Filter",
                dept_options,
                index=dept_idx,
                key="select_dept_box"
            )
            st.session_state["f_dept"] = selected_dept

        # Fetch Live Filtered Jobs
        jobs = get_approved_jobs(
            category=st.session_state["f_dept"],
            country=st.session_state["f_country"],
            search=st.session_state["f_search"]
        )

        # Result Summary Bar
        active_filters = []
        if st.session_state["f_country"] != "All Locations":
            active_filters.append(f"Region: {st.session_state['f_country']}")
        if st.session_state["f_dept"] != "All Categories":
            active_filters.append(f"Category: {st.session_state['f_dept']}")
        if st.session_state["f_search"]:
            active_filters.append(f"Keyword: \"{st.session_state['f_search']}\"")

        filter_desc = f" ({', '.join(active_filters)})" if active_filters else ""
        st.markdown(f"**Showing {len(jobs)} of {stats['total_approved']} verified positions**{filter_desc}:")

        if not jobs:
            st.warning("No positions match your selected filter criteria. Try clearing search keywords or selecting 'All Locations'.")
            if st.button("Click here to Reset All Filters"):
                st.session_state["f_search"] = ""
                st.session_state["f_country"] = "All Locations"
                st.session_state["f_dept"] = "All Categories"
                st.rerun()
        else:
            for job in jobs:
                clean_id = job["id"].replace("job-", "")
                country_flag = "🇮🇳" if job.get("country") == "India" else "🇺🇸"
                logo_url = job.get("company_logo") or f"https://www.google.com/s2/favicons?domain={job.get('company_domain', 'google.com')}&sz=128"
                req_id = job.get("req_id") or job["id"]
                ats_platform = job.get("ats_platform") or "Direct ATS"
                tags_html = " ".join([f"<span class='ww-tag-chip'>{t}</span>" for t in job.get("tags", [])])

                with st.container():
                    st.markdown(f"""
                    <div class="ww-job-card">
                        <div class="ww-card-top">
                            <div class="ww-company-flex">
                                <img src="{logo_url}" alt="{job['company']}" class="ww-company-logo" onerror="this.src='https://www.google.com/s2/favicons?domain=google.com&sz=128'">
                                <div>
                                    <div style="font-size: 11px; font-weight: 800; color: #2563eb; text-transform: uppercase;">
                                        {country_flag} {job.get('country', 'GLOBAL').upper()} • {job.get('department', 'ENGINEERING').upper()} • {job.get('work_mode', 'Hybrid').upper()}
                                    </div>
                                    <div class="ww-job-title">{job['title']}</div>
                                    <div style="font-size: 14px; font-weight: 600; color: #475569;">
                                        🏢 <b>{job['company']}</b> &nbsp;•&nbsp; 📍 {job['location']}
                                    </div>
                                </div>
                            </div>
                            <div style="text-align: right;">
                                <div class="ww-salary-badge">💰 {job.get('salary_range', 'Competitive')}</div>
                                <div style="margin-top: 6px;">
                                    <span class="ww-req-badge">REQ #{req_id}</span>
                                    <span class="ww-ats-badge">{ats_platform}</span>
                                </div>
                            </div>
                        </div>
                        <div style="font-size: 14px; color: #334155; line-height: 1.5; margin: 10px 0 12px 0;">
                            {job.get('summary', '')}
                        </div>
                        <div style="margin-bottom: 14px;">
                            {tags_html}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    c_act1, c_act2, c_spacer = st.columns([2.5, 2, 4.5])
                    with c_act1:
                        st.link_button(f"🚀 Apply on {ats_platform} ↗", job.get("apply_url"), type="primary", use_container_width=True)
                    with c_act2:
                        with st.popover("📋 View Role Details", use_container_width=True):
                            st.markdown(f"### {job['title']} at {job['company']}")
                            st.caption(f"Requisition ID: `{req_id}` | ATS Platform: `{ats_platform}` | Region: {job.get('country')}")
                            st.markdown(f"**Compensation:** `{job.get('salary_range')}`")
                            st.markdown("---")
                            st.markdown(job.get("description", ""))
                            st.link_button(f"Direct Application Link ({ats_platform}) ↗", job.get("apply_url"), type="primary")

                    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

    # ==========================================
    # TAB 2: AI CAREER COPILOT & MATCHER
    # ==========================================
    with tab_ai_copilot:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e293b 100%); color: #ffffff; padding: 28px 24px; border-radius: 12px; margin-bottom: 24px; border: 1px solid rgba(255,255,255,0.1);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <span style="font-size: 28px;">🤖</span>
                <div>
                    <h2 style="font-size: 24px; font-weight: 800; color: #ffffff; margin: 0;">WorkWire AI Career Copilot &amp; Requisition Matcher</h2>
                    <p style="color: #cbd5e1; font-size: 14px; margin-top: 4px;">
                        Powered by Google Gemini AI • Match your technical background directly with verified India &amp; US positions.
                    </p>
                </div>
            </div>
            <p style="font-size: 13px; color: #94a3b8; line-height: 1.5; margin: 0;">
                Tell us your core tech stack, experience level, and preferred region. Our Gemini model analyzes the full technical requirements of our 24+ active requisitions, computes authentic Match Scores, and delivers employer-specific interview tips.
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("ai_matcher_form"):
            col_ai_1, col_ai_2 = st.columns(2)
            with col_ai_1:
                cand_skills = st.text_input(
                    "Primary Skills & Tech Stack *",
                    placeholder="e.g. Python, PyTorch, CUDA, Kubernetes, Distributed Systems, Go, AWS"
                )
                cand_region = st.selectbox(
                    "Target Region Preference",
                    ["Any Region / Remote", "India (Bengaluru, Hyderabad, Pune, etc.)", "United States (SF, Seattle, NYC, etc.)"]
                )
            with col_ai_2:
                cand_exp = st.selectbox(
                    "Your Experience Level",
                    ["Senior Level (5-8 yrs)", "Staff / Principal (8+ yrs)", "Mid Level (3-5 yrs)", "Entry Level (0-2 yrs)"]
                )
                cand_role = st.text_input(
                    "Current or Target Job Title",
                    placeholder="e.g. Senior AI Infrastructure Engineer / Full Stack Lead"
                )

            cand_bio = st.text_area(
                "Candidate Background, Key Achievements, or Resume Snippet",
                height=110,
                placeholder="Share a brief overview of your projects, systems scale, high-concurrency experience, or what you want to work on next..."
            )

            submit_match = st.form_submit_button("✨ Match My Profile to Verified Positions →", use_container_width=True)

        if submit_match:
            if not cand_skills.strip() and not cand_bio.strip():
                st.error("Please provide at least your technical skills or background snippet so our AI can evaluate matches.")
            else:
                with st.spinner("🤖 Evaluating candidate profile against verified live requisitions with Gemini AI..."):
                    all_jobs = get_approved_jobs(limit=50)
                    country_filter_val = "India" if "India" in cand_region else ("United States" if "United States" in cand_region else "Any Location")
                    matched_results = match_candidate_jobs(
                        candidate_skills=cand_skills,
                        candidate_exp=cand_exp,
                        candidate_country=country_filter_val,
                        candidate_bio=cand_bio,
                        jobs=all_jobs
                    )

                if not matched_results:
                    st.warning("No high-confidence matches found. Try broadening your technical skills or selecting 'Any Region'.")
                else:
                    st.success(f"🎯 Found **{len(matched_results)}** optimal verified matches for your profile!")

                    for match in matched_results:
                        score = match.get("match_score", 90)
                        score_color = "#16a34a" if score >= 85 else "#2563eb"
                        country_flag = "🇮🇳" if match.get("country") == "India" else "🇺🇸"

                        strengths_html = " ".join([f"<span style='background: #dcfce7; color: #15803d; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; display: inline-block; margin: 2px;'>{s}</span>" for s in match.get("key_matching_skills", [])])
                        gaps_html = " ".join([f"<span style='background: #fef3c7; color: #b45309; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; display: inline-block; margin: 2px;'>{g}</span>" for g in match.get("skill_gaps_to_learn", [])])

                        with st.container():
                            st.markdown(f"""
                            <div style="background: #ffffff; border: 2px solid {score_color}30; border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(15,23,42,0.04);">
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 12px;">
                                    <div>
                                        <div style="font-size: 11px; font-weight: 800; color: #2563eb; text-transform: uppercase;">
                                            {country_flag} {match.get('country', 'GLOBAL').upper()} • OFFICIAL REQUISITION
                                        </div>
                                        <div style="font-size: 22px; font-weight: 800; color: #0f172a; margin-top: 2px;">
                                            {match['title']}
                                        </div>
                                        <div style="font-size: 15px; font-weight: 600; color: #475569; margin-top: 2px;">
                                            🏢 <b>{match['company']}</b> &nbsp;•&nbsp; 📍 {match['location']}
                                        </div>
                                    </div>
                                    <div style="text-align: right;">
                                        <div class="ww-match-score-badge">
                                            🔥 {score}% Match
                                        </div>
                                        <div style="margin-top: 6px;">
                                            <span class="ww-req-badge">REQ #{match.get('req_id')}</span>
                                        </div>
                                    </div>
                                </div>

                                <!-- AI Rationale Callout -->
                                <div style="background: #f8fafc; border-left: 4px solid #2563eb; padding: 14px 16px; border-radius: 0 8px 8px 0; margin: 12px 0; font-size: 14px; color: #1e293b; line-height: 1.6;">
                                    <b>💡 AI Match Rationale:</b> {match.get('match_reason')}
                                </div>

                                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; margin: 14px 0;">
                                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px;">
                                        <div style="font-size: 11px; font-weight: 800; color: #166534; text-transform: uppercase;">✅ Key Matching Strengths</div>
                                        <div style="margin-top: 6px;">
                                            {strengths_html}
                                        </div>
                                    </div>
                                    <div style="background: #fffbeb; border: 1px solid #fde68a; padding: 12px; border-radius: 8px;">
                                        <div style="font-size: 11px; font-weight: 800; color: #92400e; text-transform: uppercase;">⚠️ Recommended Prep / Skills Gaps</div>
                                        <div style="margin-top: 6px;">
                                            {gaps_html}
                                        </div>
                                    </div>
                                </div>

                                <div style="background: #f1f5f9; padding: 12px 16px; border-radius: 8px; font-size: 13px; color: #334155; margin-bottom: 16px;">
                                    <b>🎯 Technical Interview Tip for {match['company']}:</b> {match.get('interview_tip')}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

                            c_m_apply, c_m_spacer = st.columns([3, 6])
                            with c_m_apply:
                                st.link_button(
                                    f"🚀 Apply Directly on {match['company']} ATS ↗",
                                    match.get("apply_url"),
                                    type="primary",
                                    use_container_width=True
                                )
                            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    render_footer()
