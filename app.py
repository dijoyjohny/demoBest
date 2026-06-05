import streamlit as st

st.set_page_config(
    page_title="Mahindra University",
    page_icon="🎓",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #7b1113, #1f1f1f);
    }

    .hero {
        padding: 70px 50px;
        border-radius: 25px;
        background: linear-gradient(135deg, #7b1113, #2b2b2b);
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 55px;
        font-weight: 800;
        margin-bottom: 20px;
    }

    .hero p {
        font-size: 22px;
        line-height: 1.6;
        max-width: 850px;
        margin: auto;
    }

    .card {
        background-color: white;
        color: #222;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
        min-height: 210px;
    }

    .card h3 {
        color: #7b1113;
        font-size: 26px;
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        padding: 25px;
        margin-top: 40px;
        color: gray;
        font-size: 15px;
    }

    .button-style {
        display: inline-block;
        padding: 14px 30px;
        margin-top: 25px;
        background-color: white;
        color: #7b1113;
        border-radius: 30px;
        font-weight: bold;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h1>Hello World 🌍</h1>
        <h1>Welcome to Mahindra University</h1>
        <p>
            Mahindra University, located in Hyderabad, is a multidisciplinary institution
            focused on innovation, experiential learning, interdisciplinary research,
            entrepreneurship, and real-world impact.
        </p>
        <a class="button-style" href="https://www.mahindrauniversity.edu.in/" target="_blank">
            Visit Official Website
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("About Mahindra University")

st.write(
    """
    Mahindra University aims to develop future-ready professionals through a strong
    combination of academic excellence, practical exposure, research-driven learning,
    and industry-oriented education.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Innovation</h3>
            <p>
                Encourages creativity, entrepreneurship, and technology-driven solutions
                for modern challenges.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>Research</h3>
            <p>
                Promotes interdisciplinary research with academic, industrial, and
                societal relevance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>Experiential Learning</h3>
            <p>
                Focuses on hands-on learning, real-world problem solving, and practical
                exposure for students.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="footer">
        © 2026 Mahindra University Landing Page | Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
