import os
import streamlit as st

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Norah | AI Co-op Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LINKS
# =========================================================

CYBER_DEMO = "https://cyberpynora-f2yqphkxw9ijsmyrgyzybp.streamlit.app/"
AWS_DEMO = "https://2jmaw5pf6jf43vqyyuc5rw.streamlit.app/"
FULL_CV_STREAMLIT = "https://noura-lil-cv.streamlit.app/" # رابط ستريملت الـ CV الموجود في الأسفل

# قراءة ملف الـ PDF الموجود في المشروع محلياً أو على GitHub (للبداية)
cv_file_path = "norahcv.pdf"
PDF_BYTES = None

if os.path.exists(cv_file_path):
    with open(cv_file_path, "rb") as pdf_file:
        PDF_BYTES = pdf_file.read()


# =========================================================
# CSS
# =========================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html {
    scroll-behavior: smooth;
}

.stApp {
    background: #08090d;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1150px;
    padding: 25px 35px 70px 35px;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* NAV */

.nav {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding: 15px 0 45px 0;
}

.status {
    padding: 9px 16px;
    border-radius: 30px;
    color: #c0a6ff;
    background: rgba(150, 110, 255, 0.08);
    border: 1px solid rgba(150, 110, 255, 0.4);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .5px;
}

/* HERO */

.hero {
    padding: 80px 0 30px 0;
}

.hero-title {
    font-size: clamp(50px, 8vw, 88px);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -5px;
    color: #ffffff;
    margin: 0;
}

.hero-title span {
    color: #a987ff;
}

.hero-text {
    max-width: 720px;
    margin-top: 28px;
    color: #999ca7;
    font-size: 19px;
    line-height: 1.8;
}

.hero-date {
    margin-top: 22px;
    color: #e6e6e8;
    font-size: 14px;
    font-weight: 600;
}

/* SECTION */

.section {
    padding-top: 85px;
    margin-bottom: 30px;
}

.section-number {
    color: #a486ff;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.section-title {
    color: #ffffff;
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 12px;
}

.section-text {
    max-width: 720px;
    color: #9295a0;
    font-size: 15px;
    line-height: 1.8;
}

/* PROJECT */

.project {
    background: linear-gradient(145deg, #171922, #0d0e13);
    border: 1px solid #292c36;
    border-radius: 22px;
    padding: 30px;
    min-height: 330px;
    transition: .25s ease;
}

.project:hover {
    border-color: #8f6ee8;
    transform: translateY(-4px);
}

.project-number {
    color: #9d7aff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

.project-title {
    color: #ffffff;
    font-size: 25px;
    font-weight: 750;
    margin-bottom: 15px;
}

.project-text {
    color: #9b9eaa;
    font-size: 14px;
    line-height: 1.85;
    min-height: 125px;
}

.tech {
    margin-top: 20px;
}

.tech span {
    display: inline-block;
    padding: 6px 10px;
    margin: 4px 4px 0 0;
    border-radius: 8px;
    background: #181a22;
    border: 1px solid #292c36;
    color: #c9cad1;
    font-size: 11px;
}

/* SKILLS */

.skill {
    background: #101219;
    border: 1px solid #282b35;
    border-radius: 18px;
    padding: 25px;
    min-height: 175px;
}

.skill-title {
    color: #a587ff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.skill-items {
    color: #dedfe4;
    font-size: 14px;
    line-height: 2;
}

/* EDUCATION */

.education {
    background: linear-gradient(135deg, #171922, #0d0e13);
    border: 1px solid #292c36;
    border-radius: 22px;
    padding: 30px;
}

.education-title {
    color: #ffffff;
    font-size: 23px;
    font-weight: 750;
}

.education-school {
    color: #a486ff;
    font-size: 15px;
    font-weight: 600;
    margin-top: 8px;
}

.education-info {
    color: #9c9fa9;
    font-size: 14px;
    margin-top: 20px;
}

/* LOOKING FOR */

.looking {
    background: radial-gradient(circle at top right, rgba(150, 110, 255, .13), transparent 45%), #101119;
    border: 1px solid rgba(150, 110, 255, .35);
    border-radius: 24px;
    padding: 40px;
}

.looking-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 750;
}

.looking-text {
    color: #a1a4ae;
    max-width: 800px;
    font-size: 15px;
    line-height: 1.9;
    margin-top: 15px;
}

.tag {
    display: inline-block;
    padding: 8px 12px;
    margin: 8px 5px 0 0;
    border-radius: 10px;
    background: #181a23;
    border: 1px solid #2c2f39;
    color: #d6d7dc;
    font-size: 12px;
}

/* CV */

.cv {
    text-align: center;
    padding: 110px 0 30px 0;
}

.cv-title {
    color: #ffffff;
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -1.5px;
}

.cv-text {
    color: #999ca7;
    max-width: 600px;
    margin: 16px auto 25px auto;
    line-height: 1.8;
}

/* BUTTONS */

div.stButton > button,
div[data-testid="stLinkButton"] a {
    border-radius: 12px !important;
    min-height: 48px !important;
    background: #11131a !important;
    border: 1px solid #292c36 !important;
    color: #ffffff !important;
    font-weight: 600 !important;
}

div.stButton > button:hover,
div[data-testid="stLinkButton"] a:hover {
    border-color: #9878ed !important;
}

/* FOOTER */

.footer {
    margin-top: 60px;
    padding-top: 25px;
    border-top: 1px solid #22252d;
    text-align: center;
    color: #626672;
    font-size: 12px;
}

@media (max-width: 700px) {
    .block-container { padding: 20px; }
    .hero-title { font-size: 55px; letter-spacing: -3px; }
    .section-title { font-size: 32px; }
    .cv-title { font-size: 32px; }
}

</style>
""")


# =========================================================
# NAVIGATION
# =========================================================

st.html("""
<div class="nav">
    <div class="status">OPEN TO CO-OP</div>
</div>
""")


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-title">
        Hi, I'm <span>Noura.</span>
    </div>

    <div class="hero-text">
        AI student passionate about Machine Learning, Deep Learning, and Intelligent Systems. Experienced
        in building interactive applications using Python and Streamlit. Interested in AI engineering, research,
        and developing practical AI solutions.
    </div>

    <div class="hero-date">
        📅 Available for Cooperative Training — November 2026
    </div>

</div>
""")


# =========================================================
# HERO BUTTON (ملف الـ PDF للتحميل في البداية)
# =========================================================

col_btn1, _ = st.columns([1.5, 3])

with col_btn1:
    if PDF_BYTES:
        st.download_button(
            label="📄 Download Full CV (PDF)",
            data=PDF_BYTES,
            file_name="Noura_Mubark_CV.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("الرجاء رفع ملف norahcv.pdf في مجلد المشروع.")


# =========================================================
# FEATURED PROJECTS
# =========================================================

st.html("""
<div class="section" id="featured-projects">

    <div class="section-number">
        01 — FEATURED PROJECTS
    </div>

    <div class="section-title">
        Projects I've Built
    </div>

    <div class="section-text">
        A selection of practical projects I've developed while
        studying Artificial Intelligence and exploring real-world
        applications.
    </div>

</div>
""")

project1, project2 = st.columns(2, gap="large")

with project1:
    st.html("""
    <div class="project">
        <div class="project-number">PROJECT 01</div>
        <div class="project-title">🕵🏻 AI Cyber Detective</div>
        <div class="project-text">
            An interactive cybersecurity awareness experience
            featuring realistic security scenarios and challenges.
            Users analyze situations and learn to identify
            potentially unsafe behavior and common security risks.
        </div>
        <div class="tech">
            <span>Python</span>
            <span>Streamlit</span>
            <span>Cybersecurity</span>
            <span>Interactive Learning</span>
        </div>
    </div>
    """)
    st.write("")
    demo1, _ = st.columns(2)
    with demo1:
        st.link_button("🚀 Live Demo", CYBER_DEMO, use_container_width=True)

with project2:
    st.html("""
    <div class="project">
        <div class="project-number">PROJECT 02</div>
        <div class="project-title">☁️ AWS AI Services Platform</div>
        <div class="project-text">
            An interactive platform exploring practical applications
            of AWS AI services. The project demonstrates how cloud
            based AI tools can be integrated into useful applications,
            including text and sentiment analysis.
        </div>
        <div class="tech">
            <span>Python</span>
            <span>Streamlit</span>
            <span>AWS</span>
            <span>Amazon Comprehend</span>
        </div>
    </div>
    """)
    st.write("")
    st.link_button("🚀 Live Demo", AWS_DEMO, use_container_width=True)


# =========================================================
# SKILLS
# =========================================================

st.html("""
<div class="section">
    <div class="section-number">02 — SKILLS</div>
    <div class="section-title">What I Work With</div>
    <div class="section-text">
        Technologies and areas I've been learning and applying
        through coursework and practical projects.
    </div>
</div>
""")

skill1, skill2, skill3 = st.columns(3, gap="medium")

with skill1:
    st.html("""
    <div class="skill">
        <div class="skill-title">Programming</div>
        <div class="skill-items">Python<br>SQL<br>C++</div>
    </div>
    """)

with skill2:
    st.html("""
    <div class="skill">
        <div class="skill-title">Artificial Intelligence</div>
        <div class="skill-items">Machine Learning<br>Deep Learning<br>Computer Vision<br>Reinforcement Learning</div>
    </div>
    """)

with skill3:
    st.html("""
    <div class="skill">
        <div class="skill-title">Tools & Technology</div>
        <div class="skill-items">Streamlit<br>GitHub<br>VS Code<br>Jupyter Notebook</div>
    </div>
    """)


# =========================================================
# EDUCATION
# =========================================================

st.html("""
<div class="section">
    <div class="section-number">03 — EDUCATION</div>
    <div class="section-title">My Education</div>
</div>
""")

st.html("""
<div class="education">
    <div class="education-title">Diploma in Artificial Intelligence</div>
    <div class="education-school">Academy Of Learning</div>
    <div class="education-info"><strong>Expected Graduation:</strong> 2027</div>
</div>
""")


# =========================================================
# WHAT I'M LOOKING FOR
# =========================================================

st.html("""
<div class="section">
    <div class="section-number">04 — WHAT I'M LOOKING FOR</div>
    <div class="section-title">Let's Build Something Together</div>
</div>
""")

st.html("""
<div class="looking">
    <div class="looking-title">🎯 Cooperative Training Opportunity</div>
    <div class="looking-text">
        I'm currently looking for a cooperative training opportunity
        where I can apply my Artificial Intelligence knowledge, work
        on real-world projects, learn from an experienced team,
        and contribute to a professional environment.
        <br><br>
        <strong style="color:#ffffff;">Available starting November 2026</strong>
        <br><br>
        <span class="tag">Artificial Intelligence</span>
        <span class="tag">Machine Learning</span>
        <span class="tag">Data</span>
        <span class="tag">Cloud</span>
        <span class="tag">Technology</span>
    </div>
</div>
""")


# =========================================================
# FULL CV (موقع الستريملت في الأسفل)
# =========================================================

st.html("""
<div class="cv">
    <div class="cv-title">Want to know more about me?</div>
    <div class="cv-text">
        Explore my full interactive CV and portfolio to learn more about
        my background, skills, education, and projects.
    </div>
</div>
""")

col_cv_bottom, _ = st.columns([1.5, 3])

with col_cv_bottom:
    st.link_button(
        "📄 View Interactive CV App",
        FULL_CV_STREAMLIT,
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">
    Built with Python & Streamlit · Noura Mubarak · 2026
</div>
""")
