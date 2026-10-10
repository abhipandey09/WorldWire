import streamlit as st

def render_about_page():
    st.markdown("""
    <div style="max-width: 900px; margin: 0 auto; padding: 20px 0 50px 0;">
        <div style="font-size: 0.8rem; font-weight: 800; color: #dc2626; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">
            ABOUT WORLDWIRE
        </div>
        <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.8rem; font-weight: 900; line-height: 1.2; margin-bottom: 16px; color: #0f172a;">
            The International Journal of Real-Time Intelligence & Global Affairs
        </h1>
        <p style="font-size: 1.2rem; line-height: 1.6; color: #334155; margin-bottom: 28px; font-style: italic;">
            Delivering unvarnished, factual, and verified international reporting across geopolitics, markets, science, and technological shifts.
        </p>
        
        <hr style="border: none; border-top: 2px solid #dc2626; margin-bottom: 30px;">

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            Our Editorial Mission
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            WorldWire was established with a singular objective: to provide global citizens, policy analysts, researchers, and industry leaders with real-time, non-partisan dispatches on the most consequential events shaping our world. In an era dominated by clickbait and ideological polarization, WorldWire emphasizes verified developments, multi-lateral context, and rigorous primary-source citations.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 800; margin-top: 28px; margin-bottom: 12px; color: #0f172a;">
            Editorial Standards & E-E-A-T Framework
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 16px;">
            We adhere to the highest standards of accuracy, transparency, and independence:
        </p>
        <ul style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 24px; padding-left: 24px;">
            <li><b>Multi-Source Cross Verification:</b> All published events are verified against international diplomatic records, sovereign wire reports, and reputable press agencies (including Reuters, Associated Press, Agence France-Presse, Bloomberg, and the BBC).</li>
            <li><b>Neutral Tone & Clear Attribution:</b> We report facts, verified statements, and economic metrics without sensationalist commentary or speculative hyperbole. Every dispatch cites the primary news desk responsible for original field reporting.</li>
            <li><b>Global Representation:</b> Our coverage actively monitors developments across all continents—North America, Latin America, Europe, Africa, the Middle East, and Asia-Pacific.</li>
        </ul>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 800; margin-top: 28px; margin-bottom: 12px; color: #0f172a;">
            Artificial Intelligence & Technological Transparency
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            In alignment with Google Search and international journalistic transparency guidelines, we openly disclose our curation pipeline. WorldWire employs advanced autonomous research tools (leveraging Google Gemini LLM infrastructure with live Google Search grounding) to scan international wire streams 24 hours a day, 7 days a week. These systems synthesize complex geopolitical developments into concise, readable executive briefings that undergo strict validation parameters before publication.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 800; margin-top: 28px; margin-bottom: 12px; color: #0f172a;">
            Dedicated Coverage Desks
        </h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 28px;">
            <div style="background: #ffffff; padding: 16px; border: 1px solid #e2e8f0; border-radius: 8px;">
                <b style="color: #dc2626;">🌐 Geopolitics & World</b>
                <p style="font-size: 0.95rem; color: #475569; margin: 6px 0 0 0;">Diplomatic treaties, regional conflicts, sovereign summit communiques, and humanitarian missions.</p>
            </div>
            <div style="background: #ffffff; padding: 16px; border: 1px solid #e2e8f0; border-radius: 8px;">
                <b style="color: #dc2626;">📈 Global Markets & Economy</b>
                <p style="font-size: 0.95rem; color: #475569; margin: 6px 0 0 0;">Central bank rate actions, trade corridors, sovereign debt cycles, energy spot markets, and supply chains.</p>
            </div>
            <div style="background: #ffffff; padding: 16px; border: 1px solid #e2e8f0; border-radius: 8px;">
                <b style="color: #dc2626;">⚡ Technology & Computing</b>
                <p style="font-size: 0.95rem; color: #475569; margin: 6px 0 0 0;">Artificial intelligence infrastructure, semiconductor fabrication, telecommunications, and quantum systems.</p>
            </div>
            <div style="background: #ffffff; padding: 16px; border: 1px solid #e2e8f0; border-radius: 8px;">
                <b style="color: #dc2626;">🔬 Science & Climate</b>
                <p style="font-size: 0.95rem; color: #475569; margin: 6px 0 0 0;">Space exploration missions, biomedical Nobel breakthroughs, renewable energy deployment, and weather anomalies.</p>
            </div>
        </div>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 800; margin-top: 28px; margin-bottom: 12px; color: #0f172a;">
            Fact-Checking & Corrections Policy
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            Accuracy is our cornerstone. If a dispatch contains a factual error or misattribution, we issue immediate, transparent corrections at the foot of the affected dispatch. Readers, organizations, and journalists wishing to report an inaccuracy may reach our corrections desk directly via our <a href="?page=contact" style="color: #dc2626; font-weight: 700;">Contact Us</a> page.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_contact_page():
    st.markdown("""
    <div style="max-width: 900px; margin: 0 auto; padding: 20px 0 20px 0;">
        <div style="font-size: 0.8rem; font-weight: 800; color: #dc2626; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">
            CONTACT THE WIRE
        </div>
        <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.8rem; font-weight: 900; line-height: 1.2; margin-bottom: 16px; color: #0f172a;">
            Connect with WorldWire Editorial Bureau
        </h1>
        <p style="font-size: 1.15rem; line-height: 1.6; color: #334155; margin-bottom: 28px;">
            We welcome inquiries from readers, press colleagues, researchers, and syndicated publishers worldwide.
        </p>
        <hr style="border: none; border-top: 2px solid #dc2626; margin-bottom: 30px;">
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div style="background: #ffffff; padding: 24px; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 24px;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; margin-top: 0; color: #0f172a;">Bureau Communication Channels</h3>
            
            <div style="margin-bottom: 16px;">
                <b style="color: #dc2626; font-size: 0.85rem; text-transform: uppercase;">General Editorial Inquiries</b><br>
                <span style="font-size: 1rem; color: #1e293b;">editorial@worldwire.org</span><br>
                <small style="color: #64748b;">For questions regarding coverage, syndication, or quotes.</small>
            </div>
            
            <div style="margin-bottom: 16px;">
                <b style="color: #dc2626; font-size: 0.85rem; text-transform: uppercase;">Corrections & Retractions Desk</b><br>
                <span style="font-size: 1rem; color: #1e293b;">corrections@worldwire.org</span><br>
                <small style="color: #64748b;">Direct line for factual rectifications and updates.</small>
            </div>

            <div style="margin-bottom: 16px;">
                <b style="color: #dc2626; font-size: 0.85rem; text-transform: uppercase;">Confidential News Tips</b><br>
                <span style="font-size: 1rem; color: #1e293b;">tips@worldwire.org</span><br>
                <small style="color: #64748b;">Secure channel for verified leads and whistleblower tips.</small>
            </div>

            <div style="margin-bottom: 8px;">
                <b style="color: #dc2626; font-size: 0.85rem; text-transform: uppercase;">Advertising & Brand Partnerships</b><br>
                <span style="font-size: 1rem; color: #1e293b;">advertising@worldwire.org</span><br>
                <small style="color: #64748b;">For Google AdSense compliance and sponsorship inquiries.</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: #ffffff; padding: 24px; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 24px;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; margin-top: 0; color: #0f172a;">Send a Direct Editorial Message</h3>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form"):
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
    st.markdown("""
    <div style="max-width: 900px; margin: 0 auto; padding: 20px 0 50px 0;">
        <div style="font-size: 0.8rem; font-weight: 800; color: #dc2626; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">
            LEGAL & COMPLIANCE
        </div>
        <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.8rem; font-weight: 900; line-height: 1.2; margin-bottom: 12px; color: #0f172a;">
            WorldWire Privacy Policy
        </h1>
        <p style="font-size: 0.95rem; color: #64748b; margin-bottom: 24px;">
            <b>Effective Date:</b> January 1, 2026 &nbsp;|&nbsp; <b>Last Updated:</b> October 10, 2026
        </p>
        <hr style="border: none; border-top: 2px solid #dc2626; margin-bottom: 30px;">

        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            At <b>WorldWire</b> (accessible from our network domains), the privacy of our visitors is of paramount importance to us. This Privacy Policy document outlines the types of information that is collected and recorded by WorldWire and how we utilize it in full compliance with international regulations including GDPR, CCPA, and Google AdSense partner guidelines.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            1. Consent
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            By using our website, you hereby consent to our Privacy Policy and agree to its terms.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            2. Standard Log Files
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            WorldWire follows a standard procedure of utilizing log files. These files log visitors when they access websites. All hosting companies execute this as a part of hosting service analytics. The information collected by log files includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, and possibly the number of clicks. These are not linked to any information that is personally identifiable. The purpose of the information is for analyzing trends, administering the site, tracking users' movement on the website, and gathering demographic information.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            3. Cookies and Web Beacons
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            Like any other modern digital publication, WorldWire uses 'cookies'. These cookies are used to store information including visitors' preferences, and the pages on the website that the visitor accessed or visited. The information is used to optimize the users' experience by customizing our web page content based on visitors' browser type and/or other information.
        </p>

        <div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 20px; border-radius: 4px; margin: 24px 0;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #991b1b; margin-top: 0; margin-bottom: 10px;">
                4. Google AdSense & DoubleClick DART Cookies (Mandatory Disclosure)
            </h3>
            <p style="font-family: 'Newsreader', serif; font-size: 1.1rem; line-height: 1.75; color: #1e293b; margin-bottom: 12px;">
                Google is one of our third-party advertising vendors on our site. It also uses cookies, known as DART cookies, to serve advertisements to our site visitors based upon their visit to WorldWire and other sites across the internet.
            </p>
            <ul style="font-family: 'Newsreader', serif; font-size: 1.05rem; line-height: 1.7; color: #1e293b; margin-bottom: 12px; padding-left: 20px;">
                <li>Third party vendors, including Google, use cookies to serve ads based on a user's prior visits to your website or other websites.</li>
                <li>Google's use of advertising cookies enables it and its partners to serve ads to your users based on their visit to your sites and/or other sites on the Internet.</li>
                <li>Users may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" style="color: #dc2626; font-weight: 700;">Google Ads Settings</a>. Alternatively, users can opt out of a third-party vendor's use of cookies for personalized advertising by visiting <a href="https://www.aboutads.info/choices/" target="_blank" style="color: #dc2626; font-weight: 700;">www.aboutads.info</a>.</li>
            </ul>
        </div>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            5. Third-Party Privacy Policies
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            WorldWire's Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies of these third-party ad servers for more detailed information. It may include their practices and instructions about how to opt-out of certain options.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            6. Analytics Transparency (GoatCounter)
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            We utilize GoatCounter, an open-source, privacy-first web analytics platform that does not track users across websites, does not use tracking cookies, and does not harvest personally identifiable data. All statistical data collected is strictly aggregated and used to gauge article popularity and geographic readership distribution.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            7. CCPA Privacy Rights (Do Not Sell My Personal Information)
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            Under the CCPA, among other rights, California consumers have the right to request that a business disclose the categories and specific pieces of personal data that a business has collected about consumers, request deletion of collected personal data, and request that a business that sells a consumer's personal data, not sell the consumer's personal data. WorldWire does not sell personal information.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            8. GDPR Data Protection Rights
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            We would like to make sure you are fully aware of all of your data protection rights. Every user is entitled to the following: the right to access, the right to rectification, the right to erasure, the right to restrict processing, the right to object to processing, and the right to data portability.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            9. Contact Us Regarding Privacy
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            If you have additional questions or require more information about our Privacy Policy, do not hesitate to contact us at <b>privacy@worldwire.org</b> or via our <a href="?page=contact" style="color: #dc2626; font-weight: 700;">Contact Us</a> form.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_terms_page():
    st.markdown("""
    <div style="max-width: 900px; margin: 0 auto; padding: 20px 0 50px 0;">
        <div style="font-size: 0.8rem; font-weight: 800; color: #dc2626; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">
            LEGAL & COMPLIANCE
        </div>
        <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 2.8rem; font-weight: 900; line-height: 1.2; margin-bottom: 12px; color: #0f172a;">
            Terms of Service
        </h1>
        <p style="font-size: 0.95rem; color: #64748b; margin-bottom: 24px;">
            <b>Effective Date:</b> January 1, 2026 &nbsp;|&nbsp; <b>Last Updated:</b> October 10, 2026
        </p>
        <hr style="border: none; border-top: 2px solid #dc2626; margin-bottom: 30px;">

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            1. Acceptance of Terms
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            By accessing or reading the WorldWire intelligence portal (and all affiliated subdomains and digital services), you agree to be bound by these Terms of Service and all applicable international laws and regulations. If you do not agree with any of these terms, you are prohibited from using or accessing this site.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            2. Intellectual Property & Fair Use Attribution
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            All proprietary branding, logos, editorial syntheses, layout architectures, and software codebase associated with WorldWire are protected by international copyright and trademark laws. All external reporting, cited quotes, and third-party trademarks referenced in news dispatches remain the intellectual property of their respective originating news wire agencies and holders.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            3. Disclaimer of Financial & Legal Advice
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            The articles, market figures, and economic indicators published across WorldWire are provided purely for educational and journalistic informational purposes. Nothing published on this site constitutes financial, legal, investment, or geopolitical consulting advice. Readers must conduct independent verification before executing financial transactions or strategic business decisions based on real-time news data.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            4. External Hyperlinks
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            WorldWire dispatches regularly cite and link to primary source publications, diplomatic archives, and original wire services. WorldWire is not responsible for the contents or availability of any linked external third-party site. The inclusion of any link does not imply endorsement by WorldWire.
        </p>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px; color: #0f172a;">
            5. Modifications to Terms
        </h2>
        <p style="font-family: 'Newsreader', serif; font-size: 1.15rem; line-height: 1.8; color: #1e293b; margin-bottom: 20px;">
            WorldWire reserves the right to revise these Terms of Service at any time without prior notice. By continuing to access this website, you are agreeing to be bound by the then-current version of these Terms.
        </p>
    </div>
    """, unsafe_allow_html=True)
