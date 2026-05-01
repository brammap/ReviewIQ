import streamlit as st
import time

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
        .loading-title {
            font-size: 22px;
            font-weight: 700;
            color: #1a1a1a;
            text-align: center;
            margin-bottom: 20px;
        }
        .loading-text {
            font-size: 16px;
            color: #1a1a1a;
            text-align: center;
            margin: 8px 0px;
        }
        /* Progress bar color and thickness */
        .stProgress > div > div > div > div {
            background-color: #2a9d8f;
            height: 20px;
            border-radius: 10px;
        }
        .stProgress > div > div > div {
            height: 20px;
            border-radius: 10px;
            background-color: #b2e0d8;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# PAGE 1: Input Page
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

# PAGE 2: Loading Screen
if button:
    if url:
        st.divider()
        st.markdown('<p class="loading-title">🔍 Analyzing your reviews...</p>', unsafe_allow_html=True)

        progress_bar = st.progress(0)
        status = st.empty()

        # Step 1
        status.markdown('<p class="loading-text">📡 Reading reviews from Google...</p>', unsafe_allow_html=True)
        for i in range(33):
            time.sleep(0.03)
            progress_bar.progress(i + 1)

        # Step 2
        status.markdown('<p class="loading-text">🧠 Analyzing sentiment and themes...</p>', unsafe_allow_html=True)
        for i in range(33, 66):
            time.sleep(0.03)
            progress_bar.progress(i + 1)

        # Step 3
        status.markdown('<p class="loading-text">💡 Generating recommendations...</p>', unsafe_allow_html=True)
        for i in range(66, 100):
            time.sleep(0.03)
            progress_bar.progress(i + 1)

        status.markdown('<p class="loading-text">✅ Analysis complete!</p>', unsafe_allow_html=True)
        st.success("Your results are ready!")

    else:
        st.warning("⚠️ Please enter a Google Business URL first.")

# Trust signals
st.markdown("""
    <div class="trust">
        ⭐ 500+ Reviews Analyzed &nbsp;&nbsp;|&nbsp;&nbsp; 🏪 50+ Businesses &nbsp;&nbsp;|&nbsp;&nbsp; 🆓 Free to Try
    </div>
""", unsafe_allow_html=True)