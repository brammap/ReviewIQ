import streamlit as st

st.set_page_config(
    page_title="ReviewsIQ",
    page_icon="⭐",
    layout="centered"
)

st.markdown("""
    <style>
        .stApp {
            background-color: #e0f5f0;
        }
        .hero {
            text-align: center;
            padding: 60px 20px 30px 20px;
        }
        .hero-title {
            font-size: 42px;
            font-weight: 800;
            color: #1a1a1a;
            margin-bottom: 10px;
        }
        .hero-subtitle {
            font-size: 18px;
            color: #333333;
            margin-bottom: 8px;
        }
        .hero-sub2 {
            font-size: 15px;
            color: #555555;
            margin-bottom: 30px;
        }
        .stButton > button {
            background-color: #2a9d8f;
            color: white;
            font-size: 15px;
            padding: 10px 24px;
            border-radius: 8px;
            border: none;
            height: 50px;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #21867a;
        }
        .stTextInput > div > input {
            font-size: 15px;
            padding: 12px;
            border-radius: 8px;
            height: 50px;
            background-color: #a8ddd6 !important;
        }
        .helper {
            text-align: center;
            color: #555555;
            font-size: 13px;
            margin-top: 8px;
        }
        .trust {
            text-align: center;
            color: #333333;
            font-size: 14px;
            margin-top: 50px;
            padding-top: 30px;
            border-top: 1px solid #b2e0d8;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <div class="hero-title">⭐ ReviewsIQ</div>
        <div class="hero-subtitle">Understand what your customers really think</div>
        <div class="hero-sub2">AI-powered review analysis for small businesses</div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    url = st.text_input("", placeholder="Paste your Google Business URL here...", label_visibility="collapsed")

with col2:
    button = st.button("Analyze My Reviews")

st.markdown('<p class="helper">No account needed · Free to try</p>', unsafe_allow_html=True)

if button:
    if url:
        st.success("✅ Got it! Loading your analysis...")
    else:
        st.warning("⚠️ Please enter a Google Business URL first.")

st.markdown("""
    <div class="trust">
        ⭐ 500+ Reviews Analyzed &nbsp;&nbsp;|&nbsp;&nbsp; 🏪 50+ Businesses &nbsp;&nbsp;|&nbsp;&nbsp; 🆓 Free to Try
    </div>
""", unsafe_allow_html=True)