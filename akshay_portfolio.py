import base64
from pathlib import Path

import streamlit as st


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Akshay | Data Science Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# PERSONAL DETAILS
# --------------------------------------------------

NAME = "K. Dimbu Venkata Akshay"
ROLE = "Data Science Engineer"

EMAIL = "karumujjidimbuvenkataakshay@gmail.com"
PHONE = "7995440068"
LOCATION = "Vijayawada, Andhra Pradesh, India"

# Replace these with your actual profile URLs
GITHUB_URL = "https://github.com/YOUR_USERNAME"
LINKEDIN_URL = "https://www.linkedin.com/in/YOUR_USERNAME/"

BASE_DIR = Path(__file__).parent
RESUME_PATH = BASE_DIR / "assets" / "K_Dimbu_Venkata_Akshay_Resume.pdf"


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }

    [data-testid="stSidebar"] {
        background-color: #151a24;
        border-right: 1px solid #273449;
    }

    .hero {
        padding: 42px 30px;
        border-radius: 20px;
        background: linear-gradient(135deg, #172554, #164e63);
        border: 1px solid #334155;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 8px;
        color: white;
    }

    .hero h3 {
        color: #bae6fd;
        font-weight: 500;
    }

    .hero p {
        color: #e2e8f0;
        font-size: 17px;
        line-height: 1.7;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 20px;
        color: #7dd3fc;
    }

    .project-card {
        background-color: #171e2b;
        border: 1px solid #334155;
        padding: 22px;
        border-radius: 14px;
        min-height: 220px;
        margin-bottom: 12px;
    }

    .project-card h3 {
        color: #7dd3fc;
        margin-top: 0;
    }

    .project-card p {
        color: #cbd5e1;
        line-height: 1.6;
    }

    .skill-card {
        background-color: #171e2b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .skill-card h4 {
        color: #7dd3fc;
        margin-top: 0;
    }

    .info-card {
        background-color: #171e2b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 12px;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        padding: 25px 0 10px 0;
        border-top: 1px solid #334155;
        margin-top: 35px;
    }

    a {
        color: #7dd3fc !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

with st.sidebar:
    st.title("📊 Akshay's Portfolio")
    st.caption("Data Science • Data Engineering")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Home",
            "About Me",
            "Skills",
            "Projects",
            "Education",
            "Certificates",
            "Resume",
            "Contact",
        ],
    )

    st.divider()

    st.markdown("### Connect with me")

    st.link_button("GitHub ↗", GITHUB_URL, use_container_width=True)
    st.link_button("LinkedIn ↗", LINKEDIN_URL, use_container_width=True)

    st.caption("Built with Python and Streamlit")


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "Home":

    st.markdown(
        f"""
        <div class="hero">
            <h1>Hi, I'm {NAME} 👋</h1>
            <h3>{ROLE}</h3>
            <p>
                I am passionate about Python, data analysis,
                data engineering, and machine learning.
                I enjoy transforming raw data into meaningful
                insights and building practical data-driven projects.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">Portfolio Overview</div>',
                unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Core Skills", "10+")
    col2.metric("Project Areas", "7")
    col3.metric("Primary Language", "Python")
    col4.metric("Career Focus", "Data")

    st.divider()

    st.markdown("### What I Do")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>📈 Data Analysis</h3>
                <p>
                    Explore datasets, analyze trends,
                    and communicate insights using Python,
                    Pandas, NumPy, and Matplotlib.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>⚙️ Data Engineering</h3>
                <p>
                    Work with SQL, PySpark, and Apache Airflow
                    to process data and understand ETL workflows.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="info-card">
                <h3>🤖 Machine Learning</h3>
                <p>
                    Learn data preprocessing, model building,
                    and machine learning concepts.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("### Explore My Portfolio")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("View My Skills", use_container_width=True):
            st.info("Select 'Skills' from the sidebar.")

    with col2:
        if st.button("Explore Projects", use_container_width=True):
            st.info("Select 'Projects' from the sidebar.")

    with col3:
        if st.button("View Resume", use_container_width=True):
            st.info("Select 'Resume' from the sidebar.")


# --------------------------------------------------
# ABOUT ME
# --------------------------------------------------

elif page == "About Me":

    st.markdown(
        '<div class="section-title">About Me</div>',
        unsafe_allow_html=True,
    )

    st.write(
        f"""
        Hello! I'm **{NAME}**, a Data Science Engineer
        interested in data analysis, data engineering,
        and machine learning.

        I enjoy solving problems using Python and working
        with data tools to extract useful information.

        My technical interests include data processing,
        data visualization, SQL, distributed data processing,
        workflow orchestration, and machine learning.
        """
    )

    st.markdown("### Career Interests")

    st.markdown(
        """
        - Data Analyst
        - Data Science Engineer
        - Data Engineer
        - Machine Learning
        """
    )

    st.markdown("### Personal Details")

    st.write(f"📍 **Location:** {LOCATION}")
    st.write(f"📧 **Email:** {EMAIL}")
    st.write(f"📱 **Phone:** {PHONE}")


# --------------------------------------------------
# SKILLS
# --------------------------------------------------

elif page == "Skills":

    st.markdown(
        '<div class="section-title">Technical Skills</div>',
        unsafe_allow_html=True,
    )

    skill_groups = {
        "Programming": [
            "Python",
            "Data Structures & Algorithms",
        ],
        "Data Analysis": [
            "NumPy",
            "Pandas",
            "Matplotlib",
            "Excel",
        ],
        "Databases": [
            "SQL",
        ],
        "Data Engineering": [
            "PySpark",
            "Apache Airflow",
        ],
        "Machine Learning": [
            "Machine Learning",
        ],
    }

    for category, skills in skill_groups.items():

        st.markdown(
            f"""
            <div class="skill-card">
                <h4>{category}</h4>
                <p>{" &nbsp; • &nbsp; ".join(skills)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info(
        "These are the skills listed in your portfolio. "
        "You can add or remove skills as you gain experience."
    )


# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

elif page == "Projects":

    st.markdown(
        '<div class="section-title">My Projects</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "A collection of data analysis, data engineering, "
        "and machine learning project areas."
    )

    projects = [
        {
            "name": "📊 Student Performance Analysis",
            "description": (
                "Analyze student scores and compare math, "
                "reading, and writing performance using "
                "Python, Pandas, Matplotlib, and Streamlit."
            ),
            "tech": "Python • Pandas • Matplotlib • Streamlit",
        },
        {
            "name": "🦠 COVID-19 Data Analysis",
            "description": (
                "Explore COVID-19 datasets, identify trends, "
                "and visualize changes over time."
            ),
            "tech": "Python • Pandas • Matplotlib",
        },
        {
            "name": "🎬 Movie Rating Analysis",
            "description": (
                "Explore movie ratings and summarize "
                "patterns in movie-related datasets."
            ),
            "tech": "Python • Pandas • Data Visualization",
        },
        {
            "name": "📈 Stock Price Trend Analysis",
            "description": (
                "Analyze historical stock price data "
                "and visualize price movements."
            ),
            "tech": "Python • Pandas • Matplotlib",
        },
        {
            "name": "⚡ PySpark Data Processing",
            "description": (
                "Practice distributed data processing, "
                "DataFrame transformations, aggregations, "
                "and analytical operations."
            ),
            "tech": "Python • PySpark • SQL",
        },
        {
            "name": "🔄 Airflow ETL Pipeline",
            "description": (
                "Explore workflow orchestration with DAGs, "
                "tasks, operators, and dependencies."
            ),
            "tech": "Python • Apache Airflow",
        },
        {
            "name": "🤖 Machine Learning Project",
            "description": (
                "Practice data preprocessing, feature "
                "preparation, model training, and evaluation."
            ),
            "tech": "Python • Pandas • Machine Learning",
        },
    ]

    for i in range(0, len(projects), 2):

        col1, col2 = st.columns(2)

        for col, project in zip(
            [col1, col2],
            projects[i:i + 2],
        ):

            with col:
                st.markdown(
                    f"""
                    <div class="project-card">
                        <h3>{project["name"]}</h3>
                        <p>{project["description"]}</p>
                        <p><b>Technologies:</b><br>
                        {project["tech"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.caption(
        "Add a GitHub repository link to each project "
        once the code is available in your GitHub account."
    )


# --------------------------------------------------
# EDUCATION
# --------------------------------------------------

elif page == "Education":

    st.markdown(
        '<div class="section-title">Education</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
            <h3>🎓 Bachelor of Technology — Data Science</h3>
            <p><b>NRI Institute of Technology</b></p>
            <p>2024 – 2028</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Areas of Learning")

    st.markdown(
        """
        - Python programming
        - Data structures and algorithms
        - Data analysis and visualization
        - SQL and databases
        - Data engineering
        - Machine learning
        """
    )


# --------------------------------------------------
# CERTIFICATES
# --------------------------------------------------

elif page == "Certificates":

    st.markdown(
        '<div class="section-title">Certificates</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Use this section to showcase your completed "
        "courses, certifications, and achievements."
    )

    st.info(
        "No certificate files have been added yet. "
        "You can add your certificates below."
    )

    certificate = st.file_uploader(
        "Upload a certificate (PDF or image)",
        type=["pdf", "png", "jpg", "jpeg"],
        key="certificate_upload",
    )

    if certificate is not None:

        st.success(f"Uploaded: {certificate.name}")

        st.download_button(
            label="Download Certificate",
            data=certificate.getvalue(),
            file_name=certificate.name,
            mime=certificate.type,
        )

    st.caption(
        "Uploaded certificates are available in this session. "
        "To display them permanently, add them to your project "
        "and deploy the updated app."
    )


# --------------------------------------------------
# RESUME
# --------------------------------------------------

elif page == "Resume":

    st.markdown(
        '<div class="section-title">My Resume</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Upload a PDF resume to make it available "
        "for download during this session."
    )

    uploaded_resume = st.file_uploader(
        "Upload your resume (PDF)",
        type=["pdf"],
        key="resume_upload",
    )

    if uploaded_resume is not None:

        st.success("Resume uploaded successfully!")

        st.download_button(
            label="⬇️ Download Uploaded Resume",
            data=uploaded_resume.getvalue(),
            file_name=uploaded_resume.name,
            mime="application/pdf",
            use_container_width=True,
        )

    elif RESUME_PATH.exists():

        with open(RESUME_PATH, "rb") as resume_file:
            resume_data = resume_file.read()

        st.success("Your saved resume is available.")

        st.download_button(
            label="⬇️ Download My Resume",
            data=resume_data,
            file_name="Akshay_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    else:

        st.warning(
            "No saved resume was found. Upload your PDF above, "
            "or place your resume in the assets folder."
        )

    st.markdown("### Resume Details")

    st.write(f"**Name:** {NAME}")
    st.write(f"**Role:** {ROLE}")
    st.write(f"**Email:** {EMAIL}")
    st.write(f"**Location:** {LOCATION}")


# --------------------------------------------------
# CONTACT
# --------------------------------------------------

elif page == "Contact":

    st.markdown(
        '<div class="section-title">Contact Me</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Feel free to connect with me about opportunities, "
        "projects, or professional collaboration."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="info-card">
                <h3>📧 Email</h3>
                <p>{EMAIL}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="info-card">
                <h3>📍 Location</h3>
                <p>{LOCATION}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Send a Message")

    with st.form("contact_form"):

        sender_name = st.text_input("Your Name")
        sender_email = st.text_input("Your Email")
        subject = st.text_input("Subject")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button(
            "Prepare Email",
            use_container_width=True,
        )

    if submitted:

        if not sender_name or not sender_email or not message:
            st.error(
                "Please enter your name, email, and message."
            )

        else:

            email_subject = (
                f"{subject or 'Portfolio Contact'} "
                f"- from {sender_name}"
            )

            email_body = (
                f"Name: {sender_name}\n"
                f"Email: {sender_email}\n\n"
                f"Message:\n{message}"
            )

            import urllib.parse

            mailto_url = (
                f"mailto:{EMAIL}"
                f"?subject={urllib.parse.quote(email_subject)}"
                f"&body={urllib.parse.quote(email_body)}"
            )

            st.success(
                "Your email draft is ready. "
                "Open it using the button below."
            )

            st.link_button(
                "Open Email App",
                mailto_url,
                use_container_width=True,
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        <p>Designed and built with Python and Streamlit</p>
        <p>© 2026 Akshay. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
