from pathlib import Path
import urllib.parse

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Akshay | Data Science Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PERSONAL DETAILS
# ============================================================

NAME = "K. Dimbu Venkata Akshay"
ROLE = "Data Science Engineer"

EMAIL = "karumujjidimbuvenkataakshay@gmail.com"
PHONE = "7995440068"
LOCATION = "Vijayawada, Andhra Pradesh, India"

# IMPORTANT:
# Replace these with your actual profiles.
GITHUB_URL = "https://github.com/YOUR_USERNAME"
LINKEDIN_URL = "https://www.linkedin.com/in/YOUR_USERNAME/"

BASE_DIR = Path(__file__).resolve().parent

RESUME_PATH = (
    BASE_DIR
    / "assets"
    / "K_Dimbu_Venkata_Akshay_Resume.pdf"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0e1117;
    }

    [data-testid="stSidebar"] {
        background-color: #151a24;
        border-right: 1px solid #273449;
    }

    .hero {
        padding: 45px 35px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #172554,
            #164e63
        );
        border: 1px solid #334155;
        margin-bottom: 30px;
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
        font-size: 30px;
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
        min-height: 210px;
        margin-bottom: 20px;
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
        padding: 18px;
        margin-bottom: 15px;
    }

    .skill-card h4 {
        color: #7dd3fc;
        margin-top: 0;
    }

    .info-card {
        background-color: #171e2b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        padding: 25px 0 10px 0;
        border-top: 1px solid #334155;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("📊 Akshay's Portfolio")

    st.caption(
        "Data Science • Data Engineering • Machine Learning"
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "👨‍💻 About Me",
            "🛠️ Skills",
            "📂 Projects",
            "🎓 Education",
            "📜 Certificates",
            "📄 Resume",
            "📬 Contact",
        ],
    )

    st.divider()

    st.markdown("### Connect With Me")

    st.link_button(
        "GitHub ↗",
        GITHUB_URL,
        use_container_width=True,
    )

    st.link_button(
        "LinkedIn ↗",
        LINKEDIN_URL,
        use_container_width=True,
    )

    st.divider()

    st.caption("Built with Python + Streamlit")


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        f"""
        <div class="hero">

            <h1>Hi, I'm {NAME} 👋</h1>

            <h3>{ROLE}</h3>

            <p>
                I am passionate about Python, data analysis,
                data engineering, and machine learning.
                I enjoy transforming raw data into useful
                insights and building practical data-driven
                projects.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Portfolio Overview</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Core Skills", "10+")

    with col2:
        st.metric("Projects", "7+")

    with col3:
        st.metric("Primary Language", "Python")

    with col4:
        st.metric("Career Focus", "Data")


    st.divider()

    st.markdown("### What I Do")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="info-card">

            <h3>📈 Data Analysis</h3>

            <p>
            Analyze datasets, discover trends and create
            visualizations using Python, Pandas, NumPy
            and Matplotlib.
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
            Work with SQL, PySpark and Apache Airflow
            to understand ETL pipelines and data
            processing workflows.
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
            Work with data preprocessing, machine
            learning concepts, model training and
            evaluation.
            </p>

            </div>
            """,
            unsafe_allow_html=True,
        )


    st.divider()

    st.markdown("### Quick Links")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.link_button(
            "📄 View Resume",
            "#",
            use_container_width=True,
        )

    with col2:

        st.link_button(
            "💻 GitHub",
            GITHUB_URL,
            use_container_width=True,
        )

    with col3:

        st.link_button(
            "🔗 LinkedIn",
            LINKEDIN_URL,
            use_container_width=True,
        )


# ============================================================
# ABOUT ME
# ============================================================

elif page == "👨‍💻 About Me":

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
        workflow orchestration and machine learning.
        """
    )

    st.markdown("### Career Interests")

    st.markdown(
        """
        - 📊 Data Analyst
        - 🧑‍💻 Data Science Engineer
        - ⚙️ Data Engineer
        - 🤖 Machine Learning
        """
    )

    st.markdown("### Personal Details")

    st.write(f"📍 **Location:** {LOCATION}")
    st.write(f"📧 **Email:** {EMAIL}")
    st.write(f"📱 **Phone:** {PHONE}")


# ============================================================
# SKILLS
# ============================================================

elif page == "🛠️ Skills":

    st.markdown(
        '<div class="section-title">Technical Skills</div>',
        unsafe_allow_html=True,
    )

    skill_groups = {

        "🐍 Programming": [
            "Python",
            "Core Python",
            "Data Structures",
            "Algorithms",
        ],

        "📊 Data Analysis & Visualization": [
            "NumPy",
            "Pandas",
            "Matplotlib",
            "Excel",
        ],

        "🗄️ Database": [
            "SQL",
        ],

        "⚙️ Data Engineering": [
            "PySpark",
            "Apache Airflow",
            "ETL",
            "Data Pipelines",
        ],

        "🤖 Machine Learning": [
            "Machine Learning",
            "Data Preprocessing",
            "Model Evaluation",
        ],

    }


    for category, skills in skill_groups.items():

        st.markdown(
            f"""
            <div class="skill-card">

            <h4>{category}</h4>

            <p>
            {" • ".join(skills)}
            </p>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# PROJECTS
# ============================================================

elif page == "📂 Projects":

    st.markdown(
        '<div class="section-title">My Projects</div>',
        unsafe_allow_html=True,
    )

    projects = [

        {
            "name": "📊 Student Performance Analysis",
            "description":
                "Interactive dashboard for analyzing student "
                "math, reading and writing scores.",
            "tech":
                "Python • Pandas • Matplotlib • Streamlit",
        },

        {
            "name": "🦠 COVID-19 Data Analysis",
            "description":
                "Analysis and visualization of COVID-19 "
                "data and trends.",
            "tech":
                "Python • Pandas • Matplotlib",
        },

        {
            "name": "🎬 Movie Rating Analysis",
            "description":
                "Analyze movie ratings and discover patterns "
                "in movie datasets.",
            "tech":
                "Python • Pandas • Data Visualization",
        },

        {
            "name": "📈 Stock Price Trend Analysis",
            "description":
                "Analyze historical stock price data and "
                "visualize price trends.",
            "tech":
                "Python • Pandas • Matplotlib",
        },

        {
            "name": "⚡ PySpark Data Processing",
            "description":
                "Practice distributed data processing using "
                "PySpark DataFrames, transformations and "
                "aggregations.",
            "tech":
                "Python • PySpark • SQL",
        },

        {
            "name": "🔄 Airflow ETL Pipeline",
            "description":
                "Build and understand ETL workflows using "
                "Apache Airflow DAGs, operators and dependencies.",
            "tech":
                "Python • Apache Airflow",
        },

        {
            "name": "🤖 Machine Learning Project",
            "description":
                "Practice data preprocessing, model training "
                "and model evaluation.",
            "tech":
                "Python • Pandas • Machine Learning",
        },

    ]


    for i in range(0, len(projects), 2):

        col1, col2 = st.columns(2)

        current_projects = projects[i:i + 2]

        for col, project in zip(
            [col1, col2],
            current_projects,
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="project-card">

                    <h3>{project["name"]}</h3>

                    <p>
                    {project["description"]}
                    </p>

                    <p>
                    <b>Technologies:</b><br>
                    {project["tech"]}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )


# ============================================================
# EDUCATION
# ============================================================

elif page == "🎓 Education":

    st.markdown(
        '<div class="section-title">Education</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">

        <h3>🎓 Bachelor of Technology — Data Science</h3>

        <p>
        <b>NRI Institute of Technology</b>
        </p>

        <p>
        2024 – 2028
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Areas of Learning")

    st.markdown(
        """
        - Python Programming
        - Data Structures & Algorithms
        - Data Analysis
        - Data Visualization
        - SQL
        - PySpark
        - Apache Airflow
        - Machine Learning
        """
    )


# ============================================================
# CERTIFICATES
# ============================================================

elif page == "📜 Certificates":

    st.markdown(
        '<div class="section-title">Certificates</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Upload certificates to view and download them "
        "during the current session."
    )

    certificate = st.file_uploader(
        "Upload Certificate",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg",
        ],
        key="certificate_upload",
    )

    if certificate:

        st.success(
            f"Uploaded: {certificate.name}"
        )

        st.download_button(
            label="⬇️ Download Certificate",
            data=certificate.getvalue(),
            file_name=certificate.name,
            mime=certificate.type,
            use_container_width=True,
        )


# ============================================================
# RESUME
# ============================================================

elif page == "📄 Resume":

    st.markdown(
        '<div class="section-title">My Resume</div>',
        unsafe_allow_html=True,
    )

    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        key="resume_upload",
    )


    if uploaded_resume:

        st.success(
            f"Resume uploaded: {uploaded_resume.name}"
        )

        st.download_button(
            label="⬇️ Download Uploaded Resume",
            data=uploaded_resume.getvalue(),
            file_name=uploaded_resume.name,
            mime="application/pdf",
            use_container_width=True,
        )


    elif RESUME_PATH.exists():

        with open(RESUME_PATH, "rb") as file:

            resume_data = file.read()

        st.success("Resume is available.")

        st.download_button(
            label="⬇️ Download My Resume",
            data=resume_data,
            file_name="Akshay_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )


    else:

        st.warning(
            "Resume PDF was not found."
        )

        st.info(
            "Place your resume here:\n\n"
            "assets/K_Dimbu_Venkata_Akshay_Resume.pdf"
        )


    st.markdown("### Resume Information")

    st.write(f"**Name:** {NAME}")
    st.write(f"**Role:** {ROLE}")
    st.write(f"**Email:** {EMAIL}")
    st.write(f"**Location:** {LOCATION}")


# ============================================================
# CONTACT
# ============================================================

elif page == "📬 Contact":

    st.markdown(
        '<div class="section-title">Contact Me</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Feel free to contact me regarding opportunities, "
        "projects or professional collaboration."
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


    st.markdown("### Send Me a Message")

    with st.form("contact_form"):

        sender_name = st.text_input(
            "Your Name"
        )

        sender_email = st.text_input(
            "Your Email"
        )

        subject = st.text_input(
            "Subject"
        )

        message = st.text_area(
            "Your Message"
        )

        submitted = st.form_submit_button(
            "Prepare Email",
            use_container_width=True,
        )


    if submitted:

        if (
            not sender_name
            or not sender_email
            or not message
        ):

            st.error(
                "Please fill in your name, email and message."
            )

        else:

            email_subject = (
                subject
                if subject
                else "Portfolio Contact"
            )

            email_body = (
                f"Name: {sender_name}\n"
                f"Email: {sender_email}\n\n"
                f"Message:\n{message}"
            )

            mailto_url = (
                f"mailto:{EMAIL}"
                f"?subject="
                f"{urllib.parse.quote(email_subject)}"
                f"&body="
                f"{urllib.parse.quote(email_body)}"
            )

            st.success(
                "Your email draft is ready."
            )

            st.link_button(
                "📧 Open Email App",
                mailto_url,
                use_container_width=True,
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <p>
        Designed and built with Python and Streamlit 🚀
        </p>

        <p>
        © 2026 K. Dimbu Venkata Akshay
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)
