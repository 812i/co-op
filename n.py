import streamlit as st
import textwrap

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Nora | AI Co-op",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LINKS
# =========================================================

CYBER_DEMO = "https://cyberpynora-f2yqphkxw9ijsmyrgyzybp.streamlit.app/"
CYBER_GITHUB = "https://github.com/812i/cyber.py"

AWS_DEMO = "https://2jmaw5pf6jf43vqyyuc5rw.streamlit.app/"

FULL_CV = "https://noura-lil-cv.streamlit.app/"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    textwrap.dedent("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html {
        scroll-behavior: smooth;
    }

    .stApp {
        background: #08090d;
        color: #f5f5f7;
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* NAV */

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0 35px 0;
    }

    .nav-logo {
        font-size: 21px;
        font-weight: 800;
        color: white;
        letter-spacing: -0.5px;
    }

    .nav-status {
        font-size: 12px;
        font-weight: 600;
        color: #bda7ff;
        background: rgba(155, 110, 255, 0.10);
        border: 1px solid rgba(155, 110, 255, 0.28);
        padding: 8px 14px;
        border-radius: 30px;
    }

    /* HERO */

    .hero {
        padding: 70px 0 75px 0;
    }

    .hero-label {
        display: inline-block;
        color: #bda7ff;
        background: rgba(155, 110, 255, 0.10);
        border: 1px solid rgba(155, 110, 255, 0.25);
        padding: 8px 15px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 25px;
        letter-spacing: 0.5px;
    }

    .hero-title {
        font-size: clamp(48px, 7vw, 82px);
        line-height: 1.02;
        letter-spacing: -4px;
        font-weight: 800;
        color: #ffffff;
        margin: 0;
    }

    .hero-title span {
        color: #b79aff;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #a7a9b3;
        margin-top: 25px;
        max-width: 700px;
        line-height: 1.8;
    }

    .hero-date {
        margin-top: 20px;
        color: #eeeeef;
        font-weight: 600;
        font-size: 14px;
    }

    /* BUTTONS */

    div.stButton > button,
    .stLinkButton > a {
        border-radius: 12px !important;
        min-height: 46px !important;
        font-weight: 600 !important;
        border: 1px solid #292c36 !important;
        background: #11131a !important;
        color: white !important;
        transition: 0.2s ease !important;
    }

    div.stButton > button:hover,
    .stLinkButton > a:hover {
        border-color: #9d7aff !important;
        transform: translateY(-2px);
    }

    /* SECTION */

    .section {
        padding: 75px 0 25px 0;
    }

    .section-number {
        color: #9e7cff;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }

    .section-title {
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #ffffff;
        margin-bottom: 10px;
    }

    .section-description {
        max-width: 680px;
        color: #9295a0;
        line-height: 1.8;
        margin-bottom: 35px;
    }

    /* PROJECT CARD */

    .project-card {
        background: linear-gradient(
            145deg,
            rgba(24, 26, 34, 0.96),
            rgba(13, 14, 19, 0.96)
        );
        border: 1px solid #272a34;
        border-radius: 22px;
        padding: 30px;
        min-height: 350px;
        transition: 0.25s ease;
    }

    .project-card:hover {
        border-color: rgba(163, 128, 255, 0.65);
        transform: translateY(-4px);
    }

    .project-number {
        color: #9f80ff;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 18px;
    }

    .project-title {
        font-size: 25px;
        font-weight: 750;
        color: #ffffff;
        margin-bottom: 14px;
    }

    .project-description {
        color: #9ea1ac;
        font-size: 14px;
        line-height: 1.8;
        min-height: 125px;
    }

    .tech {
        margin-top: 20px;
    }

    .tech span {
        display: inline-block;
        background: #171922;
        border: 1px solid #292c36;
        color: #c7c9d2;
        padding: 6px 10px;
        border-radius: 8px;
        font-size: 11px;
        margin: 4px 4px 0 0;
    }

    /* SKILLS */

    .skill-card {
        background: #101219;
        border: 1px solid #272a34;
        border-radius: 17px;
        padding: 23px;
        min-height: 175px;
    }

    .skill-category {
        color: #a487ff;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    .skill-list {
        color: #e4e5e9;
        font-size: 14px;
        line-height: 2;
    }

    /* EDUCATION */

    .education-card {
        background: linear-gradient(
            135deg,
            rgba(25, 26, 35, 0.95),
            rgba(13, 14, 19, 0.95)
        );
        border: 1px solid #292c36;
        border-radius: 22px;
        padding: 30px;
    }

    .edu-title {
        font-size: 23px;
        font-weight: 700;
        color: white;
    }

    .edu-school {
        color: #a487ff;
        margin-top: 8px;
        font-weight: 600;
    }

    .edu-meta {
        margin-top: 22px;
        color: #a2a4ae;
        font-size: 14px;
    }

    /* OPPORTUNITY */

    .opportunity {
        margin-top: 25px;
        padding: 40px;
        border-radius: 24px;
        border: 1px solid rgba(160, 125, 255, 0.35);
        background:
            radial-gradient(
                circle at top right,
                rgba(150, 110, 255, 0.12),
                transparent 40%
            ),
            #101119;
    }

    .opportunity-title {
        font-size: 29px;
        font-weight: 750;
        color: white;
    }

    .opportunity-text {
        color: #a5a7b1;
        max-width: 760px;
        line-height: 1.9;
        margin-top: 15px;
    }

    .tag {
        display: inline-block;
        padding: 8px 12px;
        margin: 6px 5px 0 0;
        background: #181a23;
        border: 1px solid #2b2e39;
        color: #d5d6dc;
        border-radius: 10px;
        font-size: 12px;
    }

    /* CV */

    .cv-section {
        text-align: center;
        padding: 95px 0 30px 0;
    }

    .cv-title {
        font-size: 40px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #ffffff;
    }

    .cv-text {
        color: #999ca7;
        margin: 15px auto 28px auto;
        max-width: 540px;
        line-height: 1.8;
    }

    /* FOOTER */

    .footer {
        border-top: 1px solid #22252e;
        padding: 30px 0 10px 0;
        margin-top: 50px;
        color: #666a76;
        font-size: 12px;
        text-align: center;
    }

    /* MOBILE */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1.1rem;
            padding-right: 1.1rem;
        }

        .hero {
            padding: 45px 0 60px 0;
        }

        .hero-title {
            font-size: 52px;
            letter-spacing: -3px;
        }

        .hero-subtitle {
            font-size: 17px;
        }

        .section {
            padding-top: 55px;
        }

        .section-title {
            font-size: 31px;
        }

        .project-card {
            margin-bottom: 18px;
        }

        .opportunity {
            padding: 27px;
        }

        .cv-title {
            font-size: 32px;
        }

    }

    </style>
    """),
    unsafe_allow_html=True
)


# =========================================================
# NAV
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="nav">
        <div class="nav-logo">NORA.</div>
        <div class="nav-status">OPEN TO CO-OP</div>
    </div>
    """),
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="hero">

        <div class="hero-label">
            🤖 ARTIFICIAL INTELLIGENCE STUDENT
        </div>

        <div class="hero-title">
            Hi, I'm <span>Nora.</span>
        </div>

        <div class="hero-subtitle">
            I'm an Artificial Intelligence student currently looking
            for a cooperative training opportunity where I can learn,
            build, and contribute to real-world technology projects.
        </div>

        <div class="hero-date">
            📅 Available for Cooperative Training — November 2026
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


hero_col1, hero_col2, hero_space = st.columns([1.35, 1.35, 4])

with hero_col1:
    st.link_button(
        "Explore My Projects ↓",
        "#featured-projects",
        use_container_width=True
    )

with hero_col2:
    st.link_button(
        "View Full CV →",
        FULL_CV,
        use_container_width=True
    )


# =========================================================
# FEATURED PROJECTS
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="section" id="featured-projects">

        <div class="section-number">
            01 — FEATURED WORK
        </div>

        <div class="section-title">
            Projects I've Built
        </div>

        <div class="section-description">
            A selection of practical projects I've developed while
            studying Artificial Intelligence and exploring real-world
            applications.
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


project1, project2 = st.columns(2, gap="large")


# =========================================================
# PROJECT 1
# =========================================================

with project1:

    st.markdown(
        textwrap.dedent("""
        <div class="project-card">

            <div class="project-number">
                PROJECT 01
            </div>

            <div class="project-title">
                🕵🏻 AI Cyber Detective
            </div>

            <div class="project-description">
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
        """),
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        st.link_button(
            "🚀 Live Demo",
            CYBER_DEMO,
            use_container_width=True
        )

    with c2:
        st.link_button(
            "💻 GitHub",
            CYBER_GITHUB,
            use_container_width=True
        )


# =========================================================
# PROJECT 2
# =========================================================

with project2:

    st.markdown(
        textwrap.dedent("""
        <div class="project-card">

            <div class="project-number">
                PROJECT 02
            </div>

            <div class="project-title">
                ☁️ AWS AI Services Platform
            </div>

            <div class="project-description">
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
        """),
        unsafe_allow_html=True
    )

    st.write("")

    st.link_button(
        "🚀 Live Demo",
        AWS_DEMO,
        use_container_width=True
    )


# =========================================================
# SKILLS
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="section">

        <div class="section-number">
            02 — SKILLS
        </div>

        <div class="section-title">
            What I Work With
        </div>

        <div class="section-description">
            Technologies and areas I've been learning and applying
            through coursework and practical projects.
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


skill1, skill2, skill3 = st.columns(3, gap="medium")


with skill1:

    st.markdown(
        textwrap.dedent("""
        <div class="skill-card">

            <div class="skill-category">
                Programming
            </div>

            <div class="skill-list">
                Python<br>
                SQL<br>
                C++<br>
                PHP
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


with skill2:

    st.markdown(
        textwrap.dedent("""
        <div class="skill-card">

            <div class="skill-category">
                Artificial Intelligence
            </div>

            <div class="skill-list">
                Artificial Intelligence<br>
                Machine Learning<br>
                Deep Learning<br>
                AI Applications
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


with skill3:

    st.markdown(
        textwrap.dedent("""
        <div class="skill-card">

            <div class="skill-category">
                Tools & Technology
            </div>

            <div class="skill-list">
                Streamlit<br>
                AWS<br>
                GitHub<br>
                Microsoft 365
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


# =========================================================
# EDUCATION
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="section">

        <div class="section-number">
            03 — EDUCATION
        </div>

        <div class="section-title">
            My Education
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


st.markdown(
    textwrap.dedent("""
    <div class="education-card">

        <div class="edu-title">
            Diploma in Artificial Intelligence
        </div>

        <div class="edu-school">
            Academy of Learning
        </div>

        <div class="edu-meta">
            <strong>GPA:</strong> 4.90 / 5.00
            &nbsp;&nbsp; • &nbsp;&nbsp;
            <strong>Expected Graduation:</strong> 2027
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


# =========================================================
# WHAT I'M LOOKING FOR
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="section">

        <div class="section-number">
            04 — CO-OP
        </div>

        <div class="section-title">
            What I'm Looking For
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


st.markdown(
    textwrap.dedent("""
    <div class="opportunity">

        <div class="opportunity-title">
            🎯 Cooperative Training Opportunity
        </div>

        <div class="opportunity-text">

            I'm currently looking for a cooperative training opportunity
            where I can apply my AI knowledge, work on real-world projects,
            learn from an experienced team, and contribute to a professional
            environment.

            <br><br>

            <strong style="color:white;">
                Available starting November 2026
            </strong>

            <br><br>

            <span class="tag">Artificial Intelligence</span>
            <span class="tag">Machine Learning</span>
            <span class="tag">Data</span>
            <span class="tag">Technology</span>
            <span class="tag">Cloud</span>

        </div>

    </div>
    """),
    unsafe_allow_html=True
)


# =========================================================
# FULL CV
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="cv-section">

        <div class="cv-title">
            Want to know more about me?
        </div>

        <div class="cv-text">
            Explore my full CV and portfolio to learn more about
            my background, experience, skills, and other work.
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


st.link_button(
    "📄 View Full CV & Portfolio",
    FULL_CV
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="footer">
        Built with Python & Streamlit · Nora Mubarak · 2026
    </div>
    """),
    unsafe_allow_html=True
)