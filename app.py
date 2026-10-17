import streamlit as st
from streamlit_autorefresh import st_autorefresh
import scheduler
from job_store import get_approved_jobs, get_job_by_id, get_job_stats
import admin_panel
from pages_content import ABOUT_PAGE_MD, CONTACT_PAGE_MD, PRIVACY_PAGE_MD, TERMS_PAGE_MD

# Streamlit Page Configuration
st.set_page_config(
    page_title="WORKWIRE | Verified Tech Careers India & US",
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

# Custom High-Contrast Professional Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;0,900;1,700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #0f172a;
    }
    
    /* Top Header Bar */
    .top-bar {
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
        margin-bottom: 14px;
    }
    
    /* Brand Masthead */
    .brand-masthead {
        border-bottom: 2px solid #0f172a;
        padding-bottom: 14px;
        margin-bottom: 22px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        flex-wrap: wrap;
        gap: 12px;
    }
    .brand-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 38px;
        font-weight: 900;
        color: #0f172a;
        line-height: 1;
        letter-spacing: -0.5px;
    }
    .brand-sub {
        font-size: 13px;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 700;
        margin-top: 6px;
    }
    
    /* Navigation Bar */
    .nav-bar {
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
    }
    .nav-bar a {
        color: #334155;
        text-decoration: none;
        padding: 4px 8px;
        border-radius: 4px;
    }
    .nav-bar a:hover {
        background: #e2e8f0;
        color: #0f172a;
    }

    /* Footer */
    .footer-container {
        border-top: 3px solid #2563eb;
        margin-top: 48px;
        padding: 32px 16px 24px 16px;
        text-align: center;
        color: #64748b;
        font-size: 13px;
        background: #ffffff;
        border-radius: 8px;
    }
    .footer-links a {
        margin: 0 10px;
        font-weight: 600;
        color: #0f172a;
        text-decoration: none;
    }
    .footer-links a:hover {
        color: #2563eb;
    }
</style>
""", unsafe_allow_html=True)

# Top Bar Header Component
def render_header():
    html_block("""
    <div class="top-bar">
        <div>💼 <b>WORKWIRE CAREER DESK</b> &nbsp;|&nbsp; VERIFIED INDIA &amp; US TECH ROLES</div>
        <div>PUBLISHED AT MYTOMBOY360.COM</div>
    </div>
    <div class="brand-masthead">
        <div>
            <div class="brand-title"><a href="/" style="color: #0f172a; text-decoration: none;">WORKWIRE</a></div>
            <div class="brand-sub">Curated Engineering, AI &amp; Tech Opportunities in India &amp; United States</div>
        </div>
        <div style="text-align: right; font-size: 12px; color: #64748b; font-weight: 600;">
            <div style="color: #2563eb; font-weight: 800;">🛡️ 100% HUMAN VETTED POSITIONS</div>
            <div>Publisher: Abhishek Pandey (TechSnapZone)</div>
        </div>
    </div>
    <div class="nav-bar">
        <a href="/">All Opportunities</a>
        <a href="/about.html">About Bureau</a>
        <a href="/contact.html">Contact Us</a>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms &amp; Safety</a>
    </div>
    """)

# Footer Component
def render_footer():
    html_block("""
    <div class="footer-container">
        <div class="footer-links" style="margin-bottom: 12px;">
            <a href="/">All Opportunities</a> |
            <a href="/about.html">About Us</a> |
            <a href="/contact.html">Contact Bureau</a> |
            <a href="/privacy.html">Privacy Policy</a> |
            <a href="/terms.html">Terms of Service</a> |
            <a href="/?page=admin">Editorial Staff 🔒</a>
        </div>
        <p>© 2026 <b>WORKWIRE CAREER NETWORK</b> • Published at <b>mytomboy360.com</b> by Abhishek Pandey (TechSnapZone).</p>
        <p style="margin-top: 6px;">Verified Editorial, Employer Disclosures &amp; AdSense Compliance: <a href="mailto:techsnapzone@gmail.com" style="color: #2563eb; font-weight: 700; text-decoration: none;">techsnapzone@gmail.com</a></p>
    </div>
    """)

# ROUTING LOGIC BASED ON QUERY PARAMS
current_page = st.query_params.get("page", "")

# 1. Admin Route: /?page=admin or /admin
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

# 3. Dedicated Job Detail View (if ?job=job-101)
elif "job" in st.query_params:
    render_header()
    job_param = st.query_params.get("job")
    job = get_job_by_id(job_param)
    if not job:
        st.error(f"Position `{job_param}` not found or has been archived.")
        st.link_button("← Return to All Opportunities", "/")
    else:
        st.markdown(f"### {job['title']} at **{job['company']}**")
        st.caption(f"📍 {job['location']} ({job['country']}) | 💰 Compensation: {job.get('salary_range')} | Experience: {job.get('experience_level')}")
        
        c_act1, c_act2 = st.columns([1, 4])
        with c_act1:
            st.link_button("🚀 Apply on Employer Site ↗", job['apply_url'], type="primary", use_container_width=True)
        with c_act2:
            st.link_button("← Back to All Vacancies", "/", use_container_width=False)
        
        st.markdown("---")
        st.markdown(job.get("description", ""))
    render_footer()

# 4. Main Job Directory Homepage
else:
    render_header()

    # Editorial Hero Section
    html_block("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 32px 28px; border-radius: 8px; margin-bottom: 28px; box-shadow: 0 4px 12px rgba(15,23,42,0.08);">
        <div style="max-width: 840px;">
            <span style="background: #2563eb; color: #ffffff; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">VERIFIED OPPORTUNITIES DESK</span>
            <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 32px; font-weight: 800; margin: 12px 0 8px 0; line-height: 1.2;">Curated Technology &amp; Leadership Opportunities in India &amp; United States</h1>
            <p style="font-size: 15px; color: #cbd5e1; line-height: 1.6;">
                Every role listed on WorkWire is reviewed by <b>Abhishek Pandey (TechSnapZone)</b>. We eliminate ghost postings and verify official direct application links across India and US tech hubs with transparent salary disclosures.
            </p>
        </div>
    </div>
    """)

    # Top Search & Multi-Filters
    col_search, col_country, col_dept = st.columns([3, 2, 2])
    with col_search:
        search_query = st.text_input("🔍 Search positions, companies, or skills", placeholder="e.g. Python, NVIDIA, AWS, Machine Learning...")
    with col_country:
        selected_country = st.selectbox("📍 Region Filter", ["All Locations", "India", "United States"])
    with col_dept:
        selected_dept = st.selectbox("💼 Department Filter", [
            "All Categories",
            "Software Engineering",
            "AI & Machine Learning",
            "DevOps & Cloud",
            "Data & Analytics",
            "Product & Design",
            "Security & Trust",
            "Finance & Analytics"
        ])

    # Key Metrics Highlights
    stats = get_job_stats()
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total Active Positions", stats["total_approved"])
    with m2:
        st.metric("India Tech Hubs", stats["india_jobs"])
    with m3:
        st.metric("US Tech Corridors", stats["us_jobs"])
    with m4:
        st.metric("Candidate Fee", "₹0 / $0 Free")

    st.markdown("---")

    # Fetch Filtered Jobs
    jobs = get_approved_jobs(
        category=selected_dept,
        country=selected_country,
        search=search_query
    )

    if not jobs:
        st.warning("No positions match your selected filter criteria. Try broadening your search or selecting 'All Locations'.")
    else:
        st.write(f"Showing **{len(jobs)}** verified opportunities:")
        for job in jobs:
            clean_id = job["id"].replace("job-", "")
            country_flag = "🇮🇳" if job.get("country") == "India" else "🇺🇸"

            with st.container():
                st.markdown(f"""
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px 24px; margin-bottom: 16px; box-shadow: 0 1px 4px rgba(15,23,42,0.04);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px;">
                        <div>
                            <div style="font-size: 11px; font-weight: 800; color: #2563eb; text-transform: uppercase;">
                                {country_flag} {job.get('country', 'GLOBAL').upper()} • {job.get('department', 'ENGINEERING').upper()}
                            </div>
                            <div style="font-size: 20px; font-weight: 700; color: #0f172a; margin-top: 2px;">
                                {job['title']}
                            </div>
                            <div style="font-size: 14px; font-weight: 600; color: #475569; margin-top: 2px;">
                                🏢 {job['company']} &nbsp;•&nbsp; 📍 {job['location']}
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div style="font-size: 13px; font-weight: 800; color: #059669; background: #ecfdf5; padding: 4px 10px; border-radius: 4px;">
                                💰 {job.get('salary_range', 'Competitive')}
                            </div>
                            <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">
                                {job.get('experience_level', 'Mid Level')}
                            </div>
                        </div>
                    </div>
                    <div style="font-size: 14px; color: #334155; line-height: 1.5; margin: 12px 0;">
                        {job.get('summary', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                c_btns1, c_btns2, c_space = st.columns([1.5, 2, 4])
                with c_btns1:
                    if st.button("📄 View Full Role", key=f"btn_det_{job['id']}", use_container_width=True):
                        st.query_params["job"] = job["id"]
                        st.rerun()
                with c_btns2:
                    st.link_button("🚀 Apply on Company Site ↗", job.get("apply_url"), use_container_width=True)

    render_footer()
