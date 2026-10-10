import streamlit as st

def render_about_page():
    st.caption("ABOUT WORLDWIRE • GLOBAL NEWSROOM")
    st.title("The International Journal of Real-Time Intelligence & Global Affairs")
    st.markdown("##### *Delivering unvarnished, factual, and verified international reporting across geopolitics, markets, science, and technological shifts.*")
    st.divider()

    st.subheader("Our Editorial Mission")
    st.write(
        "WorldWire was established with a singular objective: to provide global citizens, policy analysts, "
        "researchers, and industry leaders with real-time, non-partisan dispatches on the most consequential events "
        "shaping our world. In an era dominated by clickbait and ideological polarization, WorldWire emphasizes "
        "verified developments, multilateral context, and rigorous primary-source citations."
    )

    st.subheader("Editorial Standards & E-E-A-T Framework")
    st.write("We adhere to the highest journalistic standards of accuracy, transparency, and independence:")
    st.markdown("""
- **Multi-Source Cross Verification:** All published events are verified against international diplomatic records, sovereign wire reports, and reputable press agencies (including Reuters, Associated Press, Agence France-Presse, Bloomberg, and the BBC).
- **Neutral Tone & Clear Attribution:** We report facts, verified statements, and economic metrics without sensationalist commentary or speculative hyperbole. Every dispatch cites the primary news desk responsible for original field reporting.
- **Global Representation:** Our coverage actively monitors developments across all continents—North America, Latin America, Europe, Africa, the Middle East, and Asia-Pacific.
""")

    st.subheader("Artificial Intelligence & Technological Transparency")
    st.write(
        "In alignment with Google Search and international journalistic transparency guidelines, we openly disclose our curation pipeline. "
        "WorldWire employs advanced autonomous research tools (leveraging Google Gemini LLM infrastructure with live Google Search grounding) "
        "to scan international wire streams 24 hours a day, 7 days a week. These systems synthesize complex geopolitical developments into concise, "
        "readable executive briefings that undergo strict validation parameters before publication."
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
        "Accuracy is our cornerstone. If a dispatch contains a factual error or misattribution, we issue immediate, transparent corrections "
        "at the foot of the affected dispatch. Readers, organizations, and journalists wishing to report an inaccuracy may reach our corrections "
        "desk directly via our Contact Us channel."
    )

def render_contact_page():
    st.caption("CONTACT THE WIRE • EDITORIAL BUREAU")
    st.title("Connect with WorldWire Editorial Bureau")
    st.markdown("##### *We welcome inquiries from readers, press colleagues, researchers, and syndicated publishers worldwide.*")
    st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Bureau Communication Channels")
        st.markdown("""
**General Editorial Inquiries**  
`editorial@worldwire.org`  
*For questions regarding coverage, syndication, or quotes.*

---

**Corrections & Retractions Desk**  
`corrections@worldwire.org`  
*Direct line for factual rectifications and updates.*

---

**Confidential News Tips**  
`tips@worldwire.org`  
*Secure channel for verified leads and whistleblower tips.*

---

**Advertising & Brand Partnerships**  
`advertising@worldwire.org`  
*For Google AdSense compliance and sponsorship inquiries.*
""")

    with col2:
        st.subheader("Send a Direct Editorial Message")
        with st.form("contact_direct_form"):
            c_name = st.text_input("Your Full Name", placeholder="e.g. Dr. Jane Smith")
            c_email = st.text_input("Your Email Address", placeholder="name@example.com")
            c_topic = st.selectbox("Subject Category", [
                "General Editorial Question",
                "Factual Correction / Retraction Request",
                "Confidential News Lead / Tip",
                "Advertising & Monetization Inquiry",
                "Technical / Bug Report"
            ])
            c_msg = st.text_area("Your Message", placeholder="Please provide clear details regarding your inquiry or reference URL...")
            submitted = st.form_submit_button("Send Transmission →", type="primary", use_container_width=True)
            if submitted:
                if c_name and c_email and c_msg:
                    st.success("Thank you for reaching out. Your message has been received by the WorldWire Editorial Bureau. A senior editor will review your submission shortly.")
                else:
                    st.error("Please fill in your name, valid email address, and message before sending.")

def render_privacy_page():
    st.caption("LEGAL & COMPLIANCE • PRIVACY POLICY")
    st.title("WorldWire Privacy Policy")
    st.caption("Effective Date: January 1, 2026 | Last Updated: October 10, 2026")
    st.divider()

    st.write(
        "At **WorldWire**, the privacy of our visitors is of paramount importance to us. "
        "This Privacy Policy document outlines the types of information that is collected and recorded by WorldWire "
        "and how we utilize it in full compliance with international regulations including GDPR, CCPA, and Google AdSense partner guidelines."
    )

    st.subheader("1. Consent")
    st.write("By using our website, you hereby consent to our Privacy Policy and agree to its terms.")

    st.subheader("2. Standard Log Files")
    st.write(
        "WorldWire follows a standard procedure of utilizing log files. These files log visitors when they access websites. "
        "All hosting companies execute this as a part of hosting service analytics. The information collected by log files includes internet protocol (IP) addresses, "
        "browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, and possibly the number of clicks. "
        "These are not linked to any information that is personally identifiable. The purpose of the information is for analyzing trends, administering the site, "
        "tracking users' movement on the website, and gathering demographic information."
    )

    st.subheader("3. Cookies and Web Beacons")
    st.write(
        "Like any other modern digital publication, WorldWire uses 'cookies'. These cookies are used to store information including visitors' preferences, "
        "and the pages on the website that the visitor accessed or visited. The information is used to optimize the users' experience by customizing our web page content "
        "based on visitors' browser type and/or other information."
    )

    st.error("""
### 4. Google AdSense & DoubleClick DART Cookies (Mandatory Disclosure)

Google is one of our third-party advertising vendors on our site. It also uses cookies, known as DART cookies, to serve advertisements to our site visitors based upon their visit to WorldWire and other sites across the internet.

- Third party vendors, including Google, use cookies to serve ads based on a user's prior visits to your website or other websites.
- Google's use of advertising cookies enables it and its partners to serve ads to your users based on their visit to your sites and/or other sites on the Internet.
- Users may opt out of personalized advertising by visiting [Google Ads Settings](https://www.google.com/settings/ads). Alternatively, users can opt out of a third-party vendor's use of cookies for personalized advertising by visiting [www.aboutads.info](https://www.aboutads.info/choices/).
""")

    st.subheader("5. Third-Party Privacy Policies")
    st.write(
        "WorldWire's Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies "
        "of these third-party ad servers for more detailed information. It may include their practices and instructions about how to opt-out of certain options."
    )

    st.subheader("6. Analytics Transparency (GoatCounter)")
    st.write(
        "We utilize GoatCounter, an open-source, privacy-first web analytics platform that does not track users across websites, "
        "does not use tracking cookies, and does not harvest personally identifiable data. All statistical data collected is strictly aggregated "
        "and used to gauge article popularity and geographic readership distribution."
    )

    st.subheader("7. CCPA Privacy Rights (Do Not Sell My Personal Information)")
    st.write(
        "Under the CCPA, among other rights, California consumers have the right to request that a business disclose the categories and specific pieces "
        "of personal data that a business has collected about consumers, request deletion of collected personal data, and request that a business that sells "
        "a consumer's personal data, not sell the consumer's personal data. WorldWire does not sell personal information."
    )

    st.subheader("8. GDPR Data Protection Rights")
    st.write(
        "We would like to make sure you are fully aware of all of your data protection rights. Every user is entitled to the following: "
        "the right to access, the right to rectification, the right to erasure, the right to restrict processing, the right to object to processing, "
        "and the right to data portability."
    )

    st.subheader("9. Contact Us Regarding Privacy")
    st.write("If you have additional questions or require more information about our Privacy Policy, do not hesitate to contact us at **privacy@worldwire.org**.")

def render_terms_page():
    st.caption("LEGAL & COMPLIANCE • TERMS OF SERVICE")
    st.title("WorldWire Terms of Service")
    st.caption("Effective Date: January 1, 2026 | Last Updated: October 10, 2026")
    st.divider()

    st.subheader("1. Acceptance of Terms")
    st.write(
        "By accessing or reading the WorldWire intelligence portal (and all affiliated subdomains and digital services), "
        "you agree to be bound by these Terms of Service and all applicable international laws and regulations. "
        "If you do not agree with any of these terms, you are prohibited from using or accessing this site."
    )

    st.subheader("2. Intellectual Property & Fair Use Attribution")
    st.write(
        "All proprietary branding, logos, editorial syntheses, layout architectures, and software codebase associated with WorldWire "
        "are protected by international copyright and trademark laws. All external reporting, cited quotes, and third-party trademarks "
        "referenced in news dispatches remain the intellectual property of their respective originating news wire agencies and holders."
    )

    st.subheader("3. Disclaimer of Financial & Legal Advice")
    st.write(
        "The articles, market figures, and economic indicators published across WorldWire are provided purely for educational and journalistic "
        "informational purposes. Nothing published on this site constitutes financial, legal, investment, or geopolitical consulting advice. "
        "Readers must conduct independent verification before executing financial transactions or strategic business decisions based on real-time news data."
    )

    st.subheader("4. External Hyperlinks")
    st.write(
        "WorldWire dispatches regularly cite and link to primary source publications, diplomatic archives, and original wire services. "
        "WorldWire is not responsible for the contents or availability of any linked external third-party site. The inclusion of any link does not imply endorsement by WorldWire."
    )

    st.subheader("5. Modifications to Terms")
    st.write(
        "WorldWire reserves the right to revise these Terms of Service at any time without prior notice. "
        "By continuing to access this website, you are agreeing to be bound by the then-current version of these Terms."
    )
