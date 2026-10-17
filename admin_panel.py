import streamlit as st
from datetime import datetime, timezone
from job_store import (
    load_jobs_data,
    get_approved_jobs,
    get_pending_jobs,
    approve_job,
    reject_job,
    add_custom_job,
    get_job_stats
)
from job_scraper import run_job_scraping_cycle

ADMIN_USER = "abhishek"
ADMIN_PASS = "Admin@1998"

def trigger_static_sync():
    """Trigger static HTML and sitemap sync whenever jobs are updated."""
    try:
        from prerender import generate_all_static_pages
        generate_all_static_pages()
    except Exception as e:
        st.warning(f"Static sync note: {e}")

def render_admin():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 24px; border-radius: 8px; margin-bottom: 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <h1 style="color: #ffffff; font-family: 'Playfair Display', Georgia, serif; font-size: 28px; margin: 0;">🔒 WorkWire Editorial Admin Desk</h1>
                <p style="color: #94a3b8; font-size: 14px; margin-top: 4px;">Human Curation, Quality Verification & Job Board Oversight Bureau</p>
            </div>
            <div>
                <span style="background: #22c55e; color: #052e16; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase;">VERIFIED HUMAN EDITOR</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Session State Authentication Check
    if not st.session_state.get("admin_logged_in"):
        st.markdown("""
        <div style="max-width: 440px; margin: 40px auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 28px; box-shadow: 0 4px 12px rgba(15,23,42,0.06);">
            <h3 style="font-size: 20px; font-weight: 700; color: #0f172a; margin-bottom: 8px; text-align: center;">Editor Authentication</h3>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 20px; text-align: center;">Enter your authorized publisher credentials to manage and approve daily job dispatches.</p>
        </div>
        """, unsafe_allow_html=True)

        col_left, col_mid, col_right = st.columns([1, 2, 1])
        with col_mid:
            with st.form("admin_login_form"):
                user_input = st.text_input("Username", placeholder="e.g. abhishek")
                pass_input = st.text_input("Password", type="password", placeholder="Enter admin password")
                login_btn = st.form_submit_button("Authenticate into Admin Bureau →", use_container_width=True)

                if login_btn:
                    if user_input.strip() == ADMIN_USER and pass_input.strip() == ADMIN_PASS:
                        st.session_state["admin_logged_in"] = True
                        st.session_state["admin_user"] = ADMIN_USER
                        st.success("Authentication successful! Welcome, Abhishek.")
                        st.rerun()
                    else:
                        st.error("Invalid credentials. Please verify your username and password.")
            
            st.markdown("""
            <div style="text-align: center; margin-top: 16px;">
                <a href="/" style="color: #64748b; font-size: 13px; text-decoration: none;">← Return to Public Job Directory</a>
            </div>
            """, unsafe_allow_html=True)
        return

    # Authenticated Admin View
    stats = get_job_stats()
    
    # Top Action Bar with Stats
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.metric("Live Approved Jobs", stats["total_approved"])
    with c2:
        st.metric("Pending Review Queue", stats["total_pending"], delta=f"{stats['total_pending']} to verify" if stats["total_pending"] else "Queue Clear")
    with c3:
        st.metric("India Tech Jobs", stats["india_jobs"])
    with c4:
        st.metric("US Tech Jobs", stats["us_jobs"])
    with c5:
        if st.button("🚪 Logout Editor", use_container_width=True):
            st.session_state["admin_logged_in"] = False
            st.session_state.pop("admin_user", None)
            st.rerun()

    st.markdown("---")

    # Quick Scraping Trigger & Navigation Tabs
    tab_review, tab_add, tab_manage = st.tabs([
        f"📥 Review Pending Jobs ({stats['total_pending']})",
        "➕ Post New Verified Job",
        f"📋 Manage Live Directory ({stats['total_approved']})"
    ])

    # TAB 1: REVIEW PENDING SCRAPED JOBS
    with tab_review:
        col_t1, col_t2 = st.columns([3, 1])
        with col_t1:
            st.subheader(f"Unapproved Scraped Postings ({stats['total_pending']} awaiting human verification)")
            st.caption("Review job descriptions and application links before approving them live to ensure zero scam/ghost jobs on the public portal.")
        with col_t2:
            if st.button("🔄 Fetch Fresh Jobs from Web Now", use_container_width=True):
                with st.spinner("Scraping public job feeds across India & US..."):
                    new_count = run_job_scraping_cycle()
                    trigger_static_sync()
                    st.success(f"Scraper ran successfully! {new_count} new postings queued for review.")
                    st.rerun()

        pending_jobs = get_pending_jobs()
        if not pending_jobs:
            st.info("🎉 Pending review queue is completely empty! All scraped positions have been processed.")
        else:
            for job in pending_jobs:
                with st.expander(f"📌 {job['title']} at **{job['company']}** — {job['location']} ({job['country']})", expanded=False):
                    c_info1, c_info2 = st.columns([2, 1])
                    with c_info1:
                        st.markdown(f"**Department:** `{job.get('department', 'Software Engineering')}` | **Experience:** `{job.get('experience_level', 'Mid Level')}`")
                        st.markdown(f"**Estimated Compensation:** `{job.get('salary_range', 'Competitive')}`")
                        st.markdown(f"**Key Skills / Tech:** `{'`, `'.join(job.get('tags', []))}`")
                        st.markdown(f"**Application URL:** [{job.get('apply_url')}]({job.get('apply_url')})")
                        st.markdown(f"**Executive Brief:** {job.get('summary')}")
                        st.markdown(f"**Full Scraped Details:**\n\n{job.get('description', '')}")
                    with c_info2:
                        st.markdown("### Editorial Decision")
                        if st.button(f"✅ Approve & Publish Live", key=f"app_{job['id']}", use_container_width=True):
                            if approve_job(job['id']):
                                trigger_static_sync()
                                st.success(f"Job {job['id']} published to live portal!")
                                st.rerun()
                        
                        if st.button(f"❌ Reject / Discard", key=f"rej_{job['id']}", use_container_width=True):
                            if reject_job(job['id']):
                                st.warning(f"Job {job['id']} discarded.")
                                st.rerun()

    # TAB 2: MANUAL JOB POSTING FORM
    with tab_add:
        st.subheader("Publish a Custom Verified Job")
        st.caption("Manually enter an authentic tech vacancy directly vetted by the editorial desk.")

        with st.form("manual_job_form"):
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                title = st.text_input("Job Title / Designation *", placeholder="e.g. Senior Cloud Architect")
                company = st.text_input("Company Name *", placeholder="e.g. Google India")
                country = st.selectbox("Primary Region *", ["India", "United States", "Global Remote"])
                location = st.text_input("Detailed Location *", placeholder="e.g. Bengaluru, Karnataka, India (Hybrid)")
                department = st.selectbox("Department / Category *", [
                    "Software Engineering",
                    "AI & Machine Learning",
                    "DevOps & Cloud",
                    "Data & Analytics",
                    "Product & Design",
                    "Security & Trust",
                    "Finance & Analytics"
                ])
            with col_m2:
                experience = st.selectbox("Experience Level", [
                    "Entry Level (0-2 yrs)",
                    "Mid Level (2-5 yrs)",
                    "Senior Level (5-8 yrs)",
                    "Staff Level (7-11 yrs)",
                    "Principal / Director (10+ yrs)"
                ])
                salary = st.text_input("Salary Range", placeholder="e.g. ₹35,00,000 - ₹50,00,000 INR or $160,000 - $210,000 USD")
                apply_url = st.text_input("Official Direct Apply Link *", placeholder="https://careers.google.com/...")
                tags_str = st.text_input("Key Tags / Skills (comma separated)", placeholder="Python, AWS, Kubernetes, Distributed Systems")
                summary = st.text_area("Executive Summary (1-2 sentences)", placeholder="Brief role summary for job card...")

            description = st.text_area("Full Job Description & Requirements (Markdown)", height=240, placeholder="### About Company\n...\n### Key Responsibilities\n- ...\n### Candidate Requirements\n- ...")

            submitted = st.form_submit_button("🚀 Publish Job to Live Directory →", use_container_width=True)
            if submitted:
                if not title.strip() or not company.strip() or not apply_url.strip():
                    st.error("Please fill in all required fields marked with *.")
                else:
                    tags = [t.strip() for t in tags_str.split(",") if t.strip()] if tags_str else [department]
                    new_job = {
                        "title": title.strip(),
                        "company": company.strip(),
                        "company_logo": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=120&q=80",
                        "location": location.strip(),
                        "country": country,
                        "department": department,
                        "employment_type": "Full-time",
                        "experience_level": experience,
                        "salary_range": salary.strip() or "Competitive Market Rate",
                        "apply_url": apply_url.strip(),
                        "tags": tags,
                        "summary": summary.strip() or f"Authentic career opportunity at {company} for a qualified {title}.",
                        "description": description.strip() or f"Full role details available directly on {company}'s verified careers website."
                    }
                    job_id = add_custom_job(new_job)
                    trigger_static_sync()
                    st.success(f"Successfully published {job_id}: {title} at {company}!")
                    st.rerun()

    # TAB 3: MANAGE LIVE APPROVED JOBS
    with tab_manage:
        st.subheader("Manage Published Directory")
        st.caption("Search, review, or archive expired listings from the active portal.")

        search_q = st.text_input("Search live positions by title, company, or skill", "")
        approved_jobs = get_approved_jobs(search=search_q)

        st.write(f"Showing {len(approved_jobs)} active positions:")
        for job in approved_jobs:
            c_j1, c_j2, c_j3 = st.columns([4, 2, 1])
            with c_j1:
                st.markdown(f"**{job['title']}** at **{job['company']}** — {job['location']}")
                st.caption(f"ID: `{job['id']}` | Compensation: `{job.get('salary_range')}` | Posted: {job.get('posted_at', '')[:10]}")
            with c_j2:
                st.markdown(f"[{job.get('apply_url')[:30]}...]({job.get('apply_url')})")
            with c_j3:
                st.link_button("View Permalink", f"/job-{job['id'].replace('job-', '')}.html", use_container_width=True)

    st.markdown("""
    <div style="margin-top: 36px; padding-top: 16px; border-top: 1px solid #e2e8f0; font-size: 13px; color: #64748b; text-align: center;">
        WorkWire Editorial Desk • Publisher: Abhishek Pandey (TechSnapZone) • Contact: techsnapzone@gmail.com
    </div>
    """, unsafe_allow_html=True)
