import streamlit as st
import time

st.set_page_config(
    page_title="ReviewsIQ",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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
        .summary-box {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 20px 24px;
            margin-bottom: 24px;
            border-left: 5px solid #2a9d8f;
        }
        .summary-text {
            font-size: 16px;
            color: #1a1a1a;
            line-height: 1.6;
        }
        .dashboard-title {
            font-size: 32px;
            font-weight: 800;
            color: #1a1a1a;
            margin-bottom: 20px;
        }
        .sentiment-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }
        .sentiment-card {
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }
        .sentiment-card.positive { background-color: #085041; }
        .sentiment-card.neutral { background-color: #2a9d8f; }
        .sentiment-card.negative { background-color: #0F6E56; }
        .sentiment-icon { font-size: 28px; margin-bottom: 8px; }
        .sentiment-icon.positive { color: #9FE1CB; }
        .sentiment-icon.neutral { color: #e0f5f0; }
        .sentiment-icon.negative { color: #5DCAA5; }
        .sentiment-label {
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
        }
        .sentiment-label.positive { color: #9FE1CB; }
        .sentiment-label.neutral { color: #e0f5f0; }
        .sentiment-label.negative { color: #5DCAA5; }
        .sentiment-value {
            font-size: 36px;
            font-weight: 800;
            color: #ffffff;
        }
        h4 { color: #1a3c34 !important; }
        .streamlit-expanderHeader {
            color: #1a3c34 !important;
            font-weight: 600;
            font-size: 15px;
        }
        .streamlit-expanderContent { color: #1a3c34 !important; }
        .streamlit-expanderHeader svg { fill: #1a3c34 !important; }
        details summary { color: #1a3c34 !important; }
        details summary svg { fill: #1a3c34 !important; }
        .stMarkdown p { color: #1a3c34 !important; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = False

if not st.session_state.show_dashboard:
    # PAGE 1: Input Page
    st.markdown("""
        <div class="hero">
            <div class="hero-title"><i class="fa-solid fa-brain" style="color:#2a9d8f; margin-right:12px;"></i>ReviewsIQ</div>
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
            st.divider()
            st.markdown('<p class="loading-title">Analyzing your reviews...</p>', unsafe_allow_html=True)

            progress_bar = st.progress(0)
            status = st.empty()

            status.markdown('<p class="loading-text">📡 Reading reviews from Google...</p>', unsafe_allow_html=True)
            for i in range(33):
                time.sleep(0.03)
                progress_bar.progress(i + 1)

            status.markdown('<p class="loading-text">🧠 Analyzing sentiment and themes...</p>', unsafe_allow_html=True)
            for i in range(33, 66):
                time.sleep(0.03)
                progress_bar.progress(i + 1)

            status.markdown('<p class="loading-text">💡 Generating recommendations...</p>', unsafe_allow_html=True)
            for i in range(66, 100):
                time.sleep(0.03)
                progress_bar.progress(i + 1)

            status.markdown('<p class="loading-text">Analysis complete!</p>', unsafe_allow_html=True)
            progress_bar.empty()
            st.session_state.show_dashboard = True
            st.rerun()

        else:
            st.warning("Please enter a Google Business URL first.")

else:
    # PAGE 3: Dashboard
    st.markdown('<p class="dashboard-title"><i class="fa-solid fa-brain" style="color:#2a9d8f; margin-right:10px;"></i>Your Review Analysis</p>', unsafe_allow_html=True)

    # Summary Box
    st.markdown("""
        <div class="summary-box">
            <p class="summary-text">
                Customers love your friendly staff and quick service, but pricing and wait times are common frustrations.
                Addressing these issues could significantly improve your overall rating.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Sentiment Cards
    st.markdown("#### Overall Sentiment")
    st.markdown("""
        <div class="sentiment-grid">
            <div class="sentiment-card positive">
                <div class="sentiment-icon positive"><i class="fa-solid fa-face-smile"></i></div>
                <div class="sentiment-label positive">Positive</div>
                <div class="sentiment-value">50%</div>
            </div>
            <div class="sentiment-card neutral">
                <div class="sentiment-icon neutral"><i class="fa-solid fa-face-meh"></i></div>
                <div class="sentiment-label neutral">Neutral</div>
                <div class="sentiment-value">17%</div>
            </div>
            <div class="sentiment-card negative">
                <div class="sentiment-icon negative"><i class="fa-solid fa-face-frown"></i></div>
                <div class="sentiment-label negative">Negative</div>
                <div class="sentiment-value">33%</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Theme Cards
    st.markdown("#### Top Issues from Customers")

    with st.expander("Pricing — 4 mentions"):
        st.markdown('<span style="color:#1a3c34;"><i class="fa-solid fa-triangle-exclamation" style="color:#c0392b; margin-right:6px;"></i><strong>High severity</strong></span>', unsafe_allow_html=True)
        st.markdown("**What customers are saying:**")
        st.markdown("> Prices are 30% higher than competitors")
        st.markdown("> Cannot afford to come back regularly")
        st.markdown("> Good quality but not worth the price")
        st.markdown('<span style="color:#1a3c34;"><i class="fa-solid fa-wand-magic-sparkles" style="color:#2a9d8f; margin-right:6px;"></i><strong>Recommended Action:</strong> Review your pricing strategy and compare with local competitors.</span>', unsafe_allow_html=True)

    with st.expander("Wait Times — 3 mentions"):
        st.markdown('<span style="color:#1a3c34;"><i class="fa-solid fa-triangle-exclamation" style="color:#c0392b; margin-right:6px;"></i><strong>High severity</strong></span>', unsafe_allow_html=True)
        st.markdown("**What customers are saying:**")
        st.markdown("> Waited 45 minutes for a table")
        st.markdown("> Service was slow even when not busy")
        st.markdown("> Need more staff during peak hours")
        st.markdown('<span style="color:#1a3c34;"><i class="fa-solid fa-wand-magic-sparkles" style="color:#2a9d8f; margin-right:6px;"></i><strong>Recommended Action:</strong> Consider a reservation system or hire additional staff for busy periods.</span>', unsafe_allow_html=True)

    with st.expander("Parking — 2 mentions"):
        st.markdown('<span style="color:#1a3c34;"><i class="fa-solid fa-circle-exclamation" style="color:#e67e22; margin-right:6px;"></i><strong>Moderate severity</strong></span>', unsafe_allow_html=True)
        st.markdown("**What customers are saying:**")
        st.markdown("> No parking nearby, had to walk far")
        st.markdown("> Parking situation is frustrating")
        st.markdown('<span style="color:#1a3c34;"><i class="fa-solid fa-wand-magic-sparkles" style="color:#2a9d8f; margin-right:6px;"></i><strong>Recommended Action:</strong> Partner with a nearby parking lot or provide directions to closest parking.</span>', unsafe_allow_html=True)

    st.divider()

    if st.button("← Analyze Another Business"):
        st.session_state.show_dashboard = False
        st.rerun()

# Trust signals
st.markdown("""
    <div class="trust">
        500+ Reviews Analyzed &nbsp;&nbsp;|&nbsp;&nbsp; 50+ Businesses &nbsp;&nbsp;|&nbsp;&nbsp; Free to Try
    </div>
""", unsafe_allow_html=True)