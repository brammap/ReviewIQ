"""
ReviewsIQ - Complete Integrated App
======================================================================
Frontend (Streamlit UI) + Backend (Scraper + Analyzer) fully integrated

This combines:
- Bhuvana's beautiful Streamlit frontend
- Sakthi's production-ready backend
- Complete end-to-end analysis pipeline

Author: Sakthi + Bhuvana
Date: May 2026
======================================================================
"""

import streamlit as st
import time
import json
import logging
from scraper import fetch_reviews
from analyzer import analyze_reviews

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ========================================================================
# PAGE CONFIGURATION
# ========================================================================

st.set_page_config(
    page_title="ReviewsIQ",
    page_icon="🧠",
    layout="centered"
)

# ========================================================================
# STYLING
# ========================================================================

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

# ========================================================================
# SESSION STATE INITIALIZATION
# ========================================================================

if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = False
    st.session_state.analysis = None
    st.session_state.business_name = None
    st.session_state.business_location = None

# ========================================================================
# HELPER FUNCTIONS
# ========================================================================

def get_severity_icon(mentions):
    """
    Determine severity based on mention count
    
    Args:
        mentions (int): Number of mentions of this theme
    
    Returns:
        str: HTML icon with color
    """
    if mentions >= 5:
        return '<i class="fa-solid fa-triangle-exclamation" style="color:#c0392b; margin-right:6px;"></i><strong>High severity</strong>'
    elif mentions >= 3:
        return '<i class="fa-solid fa-circle-exclamation" style="color:#e67e22; margin-right:6px;"></i><strong>Moderate severity</strong>'
    else:
        return '<i class="fa-solid fa-circle-info" style="color:#3498db; margin-right:6px;"></i><strong>Low severity</strong>'

def format_summary(analysis):
    """
    Create a summary from analysis data
    
    Args:
        analysis (dict): Analysis from Claude
    
    Returns:
        str: Formatted summary text
    """
    if isinstance(analysis, dict):
        return analysis.get('summary', 'Customer feedback analysis complete.')
    return 'Your review analysis is ready.'

def display_sentiment_cards(breakdown):
    """
    Display sentiment breakdown cards
    
    Args:
        breakdown (dict): Sentiment breakdown with positive, neutral, negative %
    """
    positive = breakdown.get('positive', 0)
    neutral = breakdown.get('neutral', 0)
    negative = breakdown.get('negative', 0)
    
    st.markdown(f"""
        <div class="sentiment-grid">
            <div class="sentiment-card positive">
                <div class="sentiment-icon positive"><i class="fa-solid fa-face-smile"></i></div>
                <div class="sentiment-label positive">Positive</div>
                <div class="sentiment-value">{positive}%</div>
            </div>
            <div class="sentiment-card neutral">
                <div class="sentiment-icon neutral"><i class="fa-solid fa-face-meh"></i></div>
                <div class="sentiment-label neutral">Neutral</div>
                <div class="sentiment-value">{neutral}%</div>
            </div>
            <div class="sentiment-card negative">
                <div class="sentiment-icon negative"><i class="fa-solid fa-face-frown"></i></div>
                <div class="sentiment-label negative">Negative</div>
                <div class="sentiment-value">{negative}%</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def display_theme(theme):
    """
    Display a single theme/issue in an expander
    
    Args:
        theme (dict): Theme data from analysis
    """
    theme_name = theme.get('name', 'Unknown')
    mentions = theme.get('mentions', 0)
    quotes = theme.get('quotes', [])
    recommendation = theme.get('recommendation', 'No recommendation available')
    
    with st.expander(f"{theme_name} — {mentions} mention{'s' if mentions > 1 else ''}"):
        # Severity badge
        severity_html = get_severity_icon(mentions)
        st.markdown(f'<span style="color:#1a3c34;">{severity_html}</span>', unsafe_allow_html=True)
        
        # Customer quotes
        st.markdown("**What customers are saying:**")
        for quote in quotes:
            st.markdown(f"> {quote}")
        
        # Recommendation
        st.markdown(f'<span style="color:#1a3c34;"><i class="fa-solid fa-wand-magic-sparkles" style="color:#2a9d8f; margin-right:6px;"></i><strong>Recommended Action:</strong> {recommendation}</span>', unsafe_allow_html=True)

# ========================================================================
# PAGE 1: INPUT PAGE
# ========================================================================

if not st.session_state.show_dashboard:
    st.markdown("""
        <div class="hero">
            <div class="hero-title"><i class="fa-solid fa-brain" style="color:#2a9d8f; margin-right:12px;"></i>ReviewsIQ</div>
            <div class="hero-subtitle">Understand what your customers really think</div>
            <div class="hero-sub2">AI-powered review analysis for small businesses</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        business_name = st.text_input(
            "", 
            placeholder="Enter business name (e.g., Starbucks)...", 
            label_visibility="collapsed"
        )
    with col2:
        button = st.button("Analyze My Reviews")

    st.markdown('<p class="helper">No account needed · Free to try</p>', unsafe_allow_html=True)

    if button:
        if business_name and business_name.strip():
            try:
                st.divider()
                st.markdown('<p class="loading-title">Analyzing your reviews...</p>', unsafe_allow_html=True)

                progress_bar = st.progress(0)
                status = st.empty()

                # ============================================================
                # STEP 1: FETCH REVIEWS
                # ============================================================
                status.markdown('<p class="loading-text">📡 Reading reviews from Google...</p>', unsafe_allow_html=True)
                
                for i in range(33):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)

                logger.info(f"Fetching reviews for: {business_name}")
                reviews = fetch_reviews(business_name, "Chicago")
                logger.info(f"Got {len(reviews)} reviews")

                # ============================================================
                # STEP 2: ANALYZE REVIEWS
                # ============================================================
                status.markdown('<p class="loading-text">🧠 Analyzing sentiment and themes...</p>', unsafe_allow_html=True)
                
                for i in range(33, 66):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)

                logger.info("Analyzing reviews with Claude AI")
                analysis = analyze_reviews(reviews)
                logger.info("Analysis complete")

                # ============================================================
                # STEP 3: PARSE ANALYSIS
                # ============================================================
                status.markdown('<p class="loading-text">💡 Generating recommendations...</p>', unsafe_allow_html=True)
                
                for i in range(66, 100):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)

                # Parse JSON if needed
                if isinstance(analysis, str):
                    try:
                        analysis = json.loads(analysis)
                    except:
                        logger.warning("Could not parse analysis as JSON, using as-is")

                # ============================================================
                # STEP 4: SAVE AND SHOW DASHBOARD
                # ============================================================
                status.markdown('<p class="loading-text">Analysis complete!</p>', unsafe_allow_html=True)
                
                time.sleep(0.5)
                progress_bar.empty()
                
                # Save to session
                st.session_state.analysis = analysis
                st.session_state.business_name = business_name
                st.session_state.show_dashboard = True
                
                logger.info("Dashboard ready, rerunning...")
                st.rerun()

            except Exception as e:
                logger.error(f"Error during analysis: {str(e)}", exc_info=True)
                st.error(f"❌ Error analyzing reviews: {str(e)}")
                st.info("Please try again or check your API key.")

        else:
            st.warning("⚠️ Please enter a business name first.")

# ========================================================================
# PAGE 2: DASHBOARD
# ========================================================================

else:
    # Get analysis from session
    analysis = st.session_state.get('analysis')
    business_name = st.session_state.get('business_name', 'Your Business')
    
    if analysis and isinstance(analysis, dict):
        # ================================================================
        # HEADER
        # ================================================================
        st.markdown(f'<p class="dashboard-title"><i class="fa-solid fa-brain" style="color:#2a9d8f; margin-right:10px;"></i>Review Analysis for {business_name}</p>', unsafe_allow_html=True)

        # ================================================================
        # SUMMARY BOX
        # ================================================================
        summary = format_summary(analysis)
        st.markdown(f"""
            <div class="summary-box">
                <p class="summary-text">
                    {summary}
                </p>
            </div>
        """, unsafe_allow_html=True)

        # ================================================================
        # SENTIMENT BREAKDOWN
        # ================================================================
        st.markdown("#### Overall Sentiment")
        
        breakdown = analysis.get('sentiment_breakdown', {})
        display_sentiment_cards(breakdown)

        st.divider()

        # ================================================================
        # TOP THEMES
        # ================================================================
        st.markdown("#### Top Issues from Customers")
        
        themes = analysis.get('themes', [])
        
        if themes:
            for theme in themes:
                display_theme(theme)
        else:
            st.info("ℹ️ No major themes identified. Customer feedback is generally positive!")

        st.divider()

        # ================================================================
        # ACTION BUTTONS
        # ================================================================
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("← Analyze Another Business"):
                st.session_state.show_dashboard = False
                st.session_state.analysis = None
                st.session_state.business_name = None
                st.rerun()
        
        with col2:
            st.info("💡 Tip: Share this analysis with your team to address top issues!")

    else:
        st.error("❌ Analysis data not found. Please start over.")
        if st.button("← Go Back"):
            st.session_state.show_dashboard = False
            st.rerun()

# ========================================================================
# FOOTER
# ========================================================================

st.markdown("""
    <div class="trust">
        500+ Reviews Analyzed &nbsp;&nbsp;|&nbsp;&nbsp; 50+ Businesses &nbsp;&nbsp;|&nbsp;&nbsp; Free to Try
    </div>
""", unsafe_allow_html=True)
