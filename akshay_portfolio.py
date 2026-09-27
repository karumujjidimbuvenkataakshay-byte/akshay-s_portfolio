import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Akshay | Data Science Engineer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1150px;}
    .hero {padding: 45px 0 25px 0;}
    .hero h1 {font-size: 3.2rem; margin-bottom: 0.2rem;}
    .hero h3 {font-weight: 500; margin-top: 0;}
    .muted {color: #777; font-size: 1.05rem;}
    .card {
        padding: 22px; border: 1px solid rgba(128,128,128,.25);
        border-radius: 14px; min-height: 185px; margin-bottom: 18px;
    }
    .tag {
        display:inline-block; padding:5px 10px; margin:3px;
        border-radius:15px; border:1px solid rgba(128,128,128,.3);
        font-size:.85rem;
    }
    .section-title {margin-top: 2.5rem; margin-bottom: 1rem;}
    a {text-decoration:none;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Hi, I'm Akshay 👋</h1>
    <h3>Data Science Engineer | Python | Data Engineering | Machine Learning</h3>
    <p class="muted">
        I build data analysis, data engineering and machine learning projects
        using Python and modern data tools.
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/")
with c2:
    st.link_button("🐙 GitHub", "https://github.com/")
with c3:
    st.link_button("📧 Email Me", "mailto:karumujjidimbuvenkataakshay@gmail.com")

st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
st.write(
    "I am a Data Science Engineer with strong analytical and technical skills "
    "in Python, PySpark, SQL, data structures and data engineering tools. "
    "I enjoy turning data into useful insights and building practical projects."
)

st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)
skills = [
    "Python", "NumPy", "Pandas", "Matplotlib", "SQL",
    "PySpark", "DSA", "Apache Airflow", "Machine Learning", "Excel"
]
st.markdown(" ".join(f'<span class="tag">{s}</span>' for s in skills),
            unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)

projects = [
    ("📊 Student Performance Analysis",
     "Interactive analysis of student scores using Python, Pandas and Matplotlib.",
     "Python • Pandas • Matplotlib • Streamlit"),
    ("🦠 COVID-19 Data Analysis",
     "Analyze COVID-19 trends and create meaningful visualizations from data.",
     "Python • Pandas • Matplotlib"),
    ("🎬 Movie Rating Analysis",
     "Explore movie ratings and identify patterns using data analysis techniques.",
     "Python • Pandas • Visualization"),
    ("📈 Stock Price Trend Analysis",
     "Analyze historical stock data and visualize price trends.",
     "Python • Pandas • Matplotlib"),
    ("⚡ PySpark Data Processing",
     "Process and transform larger datasets using distributed data processing.",
     "PySpark • Python • SQL"),
    ("🔄 Airflow ETL Pipeline",
     "Build an automated workflow for extracting, transforming and loading data.",
     "Apache Airflow • Python • SQL"),
    ("🤖 Machine Learning Project",
     "Build and evaluate a machine learning model from data preprocessing to prediction.",
     "Python • Pandas • Machine Learning"),
]

for i in range(0, len(projects), 2):
    cols = st.columns(2)
    for j, col in enumerate(cols):
        if i + j < len(projects):
            title, desc, tech = projects[i + j]
            with col:
                st.markdown(
                    f'<div class="card"><h3>{title}</h3>'
                    f'<p>{desc}</p><p><b>{tech}</b></p></div>',
                    unsafe_allow_html=True
                )

st.markdown('<h2 class="section-title">What I Work With</h2>', unsafe_allow_html=True)
a, b, c = st.columns(3)
with a:
    st.subheader("🐍 Python & Data")
    st.write("Core Python, NumPy, Pandas, Matplotlib and Excel")
with b:
    st.subheader("⚙️ Data Engineering")
    st.write("SQL, PySpark, Apache Airflow and ETL workflows")
with c:
    st.subheader("🤖 Machine Learning")
    st.write("Data preprocessing, model building and evaluation")

st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
st.write("**B.Tech (Data Science)** — NRI Institute of Technology")
st.write("2024 – 2028")

st.markdown('<h2 class="section-title">Resume</h2>', unsafe_allow_html=True)
resume = Path("assets/K_Dimbu_Venkata_Akshay_Resume.pdf")
if resume.exists():
    with open(resume, "rb") as f:
        st.download_button(
            "📄 Download My Resume",
            f,
            file_name="K_Dimbu_Venkata_Akshay_Resume.pdf",
            mime="application/pdf",
        )
else:
    st.info("Add your resume PDF to the assets folder to enable the download button.")

st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)
st.write("📧 karumujjidimbuvenkataakshay@gmail.com")
st.write("📱 +91 7995440068")
st.caption("© 2026 K. Dimbu Venkata Akshay • Built with Python & Streamlit")
