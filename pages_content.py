import streamlit as st

def render_about_page():
    st.caption("ABOUT WORLDWIRE • PUBLISHED AT MYTOMBOY360.COM")
    st.title("The Autonomous International Journal of Global Affairs & Wire Intelligence")
    st.markdown("##### *Delivering unvarnished, factual, and verified international reporting across geopolitics, markets, science, and technological shifts.*")
    st.divider()

    st.subheader("Our Mission & Publishing Entity")
    st.write(
        "**WorldWire** is a digital news and geopolitical wire publication operated on **mytomboy360.com** "
        "by **Abhishek Pandey (TechSnapZone)**. Founded to provide global readers, researchers, policy observers, "
        "and technology professionals with real-time, non-partisan dispatches, WorldWire synthesizes verified international "
        "events into comprehensive briefings with clear, primary-source attribution."
    )

    st.subheader("Editorial Standards & E-E-A-T Framework")
    st.write("We adhere to rigorous standards of accuracy, transparency, and accountability:")
    st.markdown("""
- **Multi-Source Cross Verification:** All published events are verified against international diplomatic records, sovereign wire reports, and reputable press agencies (including Reuters, Associated Press, Agence France-Presse, Bloomberg, and the BBC).
- **Neutral Tone & Strict Attribution:** We report facts, verified statements, and economic metrics without sensationalist commentary or speculative hyperbole. Every dispatch cites the primary news desk responsible for original field reporting.
- **Global Breadth:** Our coverage actively monitors developments across North America, Latin America, Europe, Africa, the Middle East, and Asia-Pacific.
- **Human Accountability & Ownership:** WorldWire is owned and operated by Abhishek Pandey. All editorial corrections, reader inquiries, and partnership requests are handled directly via verified email **techsnapzone@gmail.com**.
""")

    st.subheader("Technology & Autonomous Research Transparency")
    st.write(
        "In alignment with Google Search and international journalistic transparency guidelines, we openly disclose our workflow. "
        "WorldWire utilizes autonomous research pipelines powered by Google Gemini infrastructure with live web grounding "
        "to continuously scan global news feeds 24/7. These systems summarize complex multilingual developments into readable executive briefings "
        "under strict validation and deduplication rules before publication."
    )

    st.subheader("Dedicated Coverage Desks")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**🌐 Geopolitics & World**\n\nDiplomatic treaties, regional conflicts, sovereign summit communiques, and humanitarian missions.")
        st.info("**📈 Global Markets & Economy**\n\nCentral bank rate actions, trade corridors, sovereign debt cycles, energy spot markets, and supply chains.")
    with col2:
        st.info("**⚡ Technology & Computing**\n\nArtificial intelligence infrastructure, semiconductor fabrication, telecommunications, and quantum systems.")
        st.info("**🔬 Science & Climate**\n\nSpace exploration missions, biomedical Nobel breakthroughs, renewable energy deployment, and weather anomalies.")

    st.subheader("Fact-Checking & Corrections Policy")
    st.write(
        "Accuracy is our cornerstone. If a dispatch contains a factual error or misattribution, we issue immediate, transparent corrections. "
        "Readers and journalists wishing to report an inaccuracy may reach our corrections desk directly at **techsnapzone@gmail.com**."
    )


def render_contact_page():
    st.caption("CONTACT THE WIRE • EDITORIAL & INQUIRIES BUREAU")
    st.title("Connect with WorldWire Bureau")
    st.markdown("##### *We welcome inquiries from readers, press colleagues, researchers, and partners worldwide.*")
    st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Official Communication Channels")
        st.markdown("""
**Primary Verified Contact**  
📧 **techsnapzone@gmail.com**  
*Direct inbox monitored daily for all editorial, syndication, and partnership inquiries.*

---

**Editorial & Content Desk**  
📧 `techsnapzone@gmail.com` *(Subject: [Editorial Inquiry])*  
*For questions regarding story coverage, press quotes, and syndication.*

---

**Corrections & Fact-Checking Desk**  
📧 `techsnapzone@gmail.com` *(Subject: [Correction Request])*  
*Direct priority line for factual rectifications, source attribution, and updates.*

---

**Advertising, Sponsorship & AdSense Compliance**  
📧 `techsnapzone@gmail.com` *(Subject: [Advertising / Compliance])*  
*For Google AdSense policy coordination, sponsorship, and commercial inquiries.*

---

**Publishing Domain:** `https://mytomboy360.com`  
**Publisher:** Abhishek Pandey (TechSnapZone)
""")

    with col2:
        st.subheader("Send a Message Directly")
        with st.form("contact_direct_form"):
            c_name = st.text_input("Your Full Name", placeholder="e.g. Jane Smith")
            c_email = st.text_input("Your Email Address", placeholder="name@example.com")
            c_topic = st.selectbox("Subject Category", [
                "General Editorial Question",
                "Factual Correction / Retraction Request",
                "News Tip / Lead",
                "Advertising & Monetization Inquiry",
                "Technical / Bug Report"
            ])
            c_msg = st.text_area("Your Message", placeholder="Please provide clear details regarding your inquiry...")
            submitted = st.form_submit_button("Send Transmission →", type="primary", use_container_width=True)
            if submitted:
                if c_name and c_email and c_msg:
                    st.success(
                        f"Thank you, {c_name}! Your message regarding '{c_topic}' has been logged. "
                        f"You may also reach us directly at **techsnapzone@gmail.com**."
                    )
                else:
                    st.error("Please fill in your name, email address, and message before sending.")


def render_privacy_page():
    st.caption("LEGAL & COMPLIANCE • PRIVACY POLICY")
    st.title("WorldWire Privacy Policy")
    st.caption("Effective Date: January 1, 2026 | Last Updated: October 11, 2026 | Domain: mytomboy360.com")
    st.divider()

    st.write(
        "At **WorldWire (mytomboy360.com)**, the privacy of our visitors is of paramount importance to us. "
        "This Privacy Policy document outlines the types of information collected and recorded by WorldWire "
        "and how we utilize it in full compliance with international regulations including GDPR, CCPA, and Google AdSense partner guidelines."
    )

    st.subheader("1. Consent")
    st.write("By using our website, you hereby consent to our Privacy Policy and agree to its terms.")

    st.subheader("2. Standard Log Files")
    st.write(
        "WorldWire follows a standard procedure of utilizing log files. These files log visitors when they access websites. "
        "The information collected by log files includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), "
        "date and time stamp, referring/exit pages, and number of clicks. These are not linked to any information that is personally identifiable. "
        "The purpose is for analyzing trends, administering the site, and gathering demographic information."
    )

    st.subheader("3. Cookies and Web Beacons")
    st.write(
        "Like any other digital publication, WorldWire uses 'cookies' to store information including visitors' preferences "
        "and the pages on the website that the visitor accessed. The information is used to optimize user experience."
    )

    st.info("""
### 4. Google AdSense & DoubleClick DART Cookies (Mandatory Disclosure)

Google is one of our third-party advertising vendors on our site (`mytomboy360.com`). It uses cookies, known as DART cookies, to serve advertisements to our site visitors based upon their visit to WorldWire and other sites across the internet.

- Third party vendors, including Google, use cookies to serve ads based on a user's prior visits to your website or other websites.
- Google's use of advertising cookies enables it and its partners to serve ads to users based on their visit to our sites and/or other sites on the Internet.
- Users may opt out of personalized advertising by visiting [Google Ads Settings](https://www.google.com/settings/ads). Alternatively, users can opt out of a third-party vendor's use of cookies for personalized advertising by visiting [www.aboutads.info](https://www.aboutads.info/choices/).
""")

    st.subheader("5. Third-Party Privacy Policies")
    st.write(
        "WorldWire's Privacy Policy does not apply to other advertisers or websites. Thus, we advise you to consult the respective Privacy Policies "
        "of these third-party ad servers for more detailed information. It may include their practices and instructions about how to opt-out of certain options."
    )

    st.subheader("6. Privacy-First Analytics (GoatCounter)")
    st.write(
        "We utilize GoatCounter, an open-source, privacy-first web analytics platform that does not track users across websites, "
        "does not use tracking cookies, and does not harvest personally identifiable data. All statistical data collected is strictly aggregated "
        "to gauge readership popularity and geographic distribution."
    )

    st.subheader("7. CCPA Privacy Rights (Do Not Sell My Personal Information)")
    st.write(
        "Under the California Consumer Privacy Act (CCPA), consumers have the right to request disclosure or deletion of collected personal data, "
        "and to request that a business not sell their personal data. WorldWire does not sell personal information."
    )

    st.subheader("8. GDPR Data Protection Rights")
    st.write(
        "Every user is entitled to data access, rectification, erasure, restriction of processing, objection to processing, "
        "and data portability under the General Data Protection Regulation (GDPR)."
    )

    st.subheader("9. Contact Us Regarding Privacy")
    st.write("If you have questions or require more information about our Privacy Policy, contact our Data Protection Administrator directly at **techsnapzone@gmail.com**.")


def render_terms_page():
    st.caption("LEGAL & COMPLIANCE • TERMS OF SERVICE")
    st.title("WorldWire Terms of Service")
    st.caption("Effective Date: January 1, 2026 | Last Updated: October 11, 2026 | Domain: mytomboy360.com")
    st.divider()

    st.subheader("1. Acceptance of Terms")
    st.write(
        "By accessing or reading the WorldWire intelligence portal at **mytomboy360.com** (and all affiliated subdomains and digital services), "
        "you agree to be bound by these Terms of Service and all applicable international laws and regulations. "
        "If you do not agree with any of these terms, you are prohibited from using or accessing this site."
    )

    st.subheader("2. Intellectual Property & Fair Use Attribution")
    st.write(
        "All original editorial syntheses, branding, layout architectures, and software codebase associated with WorldWire "
        "are protected by copyright. External reporting, cited quotes, and third-party trademarks "
        "referenced in news dispatches remain the intellectual property of their respective originating news wire agencies (Reuters, AP, Bloomberg, BBC, etc.)."
    )

    st.subheader("3. Disclaimer of Financial & Legal Advice")
    st.write(
        "Articles, market figures, and economic indicators published across WorldWire are provided purely for educational and journalistic "
        "informational purposes. Nothing published on this site constitutes financial, legal, investment, or geopolitical consulting advice. "
        "Readers must conduct independent verification before executing financial transactions based on real-time news data."
    )

    st.subheader("4. External Hyperlinks")
    st.write(
        "WorldWire dispatches cite and link to primary source publications, diplomatic archives, and original wire services. "
        "WorldWire is not responsible for the contents or availability of any linked external third-party site."
    )

    st.subheader("5. Modifications to Terms")
    st.write(
        "WorldWire reserves the right to revise these Terms of Service at any time without prior notice. "
        "By continuing to access this website, you agree to be bound by the then-current version of these Terms."
    )

    st.subheader("6. Contact Information")
    st.write("For legal, copyright, or terms inquiries, contact the publisher at **techsnapzone@gmail.com**.")
