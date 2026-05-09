"""
ReviewsIQ Main Pipeline
Complete end-to-end pipeline combining scraper + analyzer
"""

import os
import json
import logging
import time
from scraper import fetch_reviews
from analyzer import analyze_reviews

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def analyze_business(business_name, location=""):
    """
    Complete pipeline: Fetch reviews → Analyze → Return results
    
    Args:
        business_name (str): Name of the business to analyze
        location (str): Location of the business (optional)
    
    Returns:
        dict: Complete analysis with business info, sentiment, themes
    """
    
    try:
        logger.info(f"Starting analysis for: {business_name}, {location}")
        
        # STEP 1: Fetch Reviews
        logger.info("Step 1: Fetching reviews...")
        start_time = time.time()
        
        reviews = fetch_reviews(business_name, location)
        
        fetch_time = time.time() - start_time
        logger.info(f"✅ Step 1 complete: Got {len(reviews)} reviews in {fetch_time:.2f}s")
        
        if not reviews:
            logger.warning("No reviews returned")
            return None
        
        # STEP 2: Analyze Reviews
        logger.info("Step 2: Analyzing reviews with Claude AI...")
        start_time = time.time()
        
        analysis = analyze_reviews(reviews)
        
        analysis_time = time.time() - start_time
        logger.info(f"✅ Step 2 complete: Analysis finished in {analysis_time:.2f}s")
        
        # STEP 3: Return Results
        logger.info("Step 3: Preparing final results...")
        
        if isinstance(analysis, dict):
            result = {
                "business": {
                    "name": business_name,
                    "location": location,
                    "reviews_count": len(reviews)
                },
                "analysis": analysis,
                "metadata": {
                    "fetch_time_seconds": fetch_time,
                    "analysis_time_seconds": analysis_time,
                    "total_time_seconds": fetch_time + analysis_time
                }
            }
        else:
            result = {
                "business": {
                    "name": business_name,
                    "location": location,
                    "reviews_count": len(reviews)
                },
                "analysis": analysis,
                "metadata": {
                    "fetch_time_seconds": fetch_time,
                    "analysis_time_seconds": analysis_time,
                    "total_time_seconds": fetch_time + analysis_time
                }
            }
        
        logger.info("✅ Step 3 complete: Results prepared")
        logger.info(f"✅ Analysis complete in {fetch_time + analysis_time:.2f}s total")
        
        return result
    
    except Exception as e:
        logger.error(f"Error in analysis pipeline: {str(e)}", exc_info=True)
        return None


def print_results(result):
    """Pretty print analysis results"""
    
    if not result:
        print("❌ No results to display")
        return
    
    print("\n" + "=" * 70)
    print("REVIEWSIQ ANALYSIS RESULTS")
    print("=" * 70 + "\n")
    
    business = result.get('business', {})
    print(f"Business: {business.get('name', 'Unknown')}")
    print(f"Location: {business.get('location', 'Unknown')}")
    print(f"Reviews Analyzed: {business.get('reviews_count', 0)}\n")
    
    analysis = result.get('analysis', {})
    
    if isinstance(analysis, dict):
        sentiment_score = analysis.get('sentiment_score', 'N/A')
        print(f"📊 Overall Sentiment Score: {sentiment_score}%")
        
        breakdown = analysis.get('sentiment_breakdown', {})
        print(f"\n😊 Sentiment Breakdown:")
        print(f"  Positive: {breakdown.get('positive', 0)}%")
        print(f"  Neutral:  {breakdown.get('neutral', 0)}%")
        print(f"  Negative: {breakdown.get('negative', 0)}%")
        
        summary = analysis.get('summary', '')
        if summary:
            print(f"\n📝 Summary:")
            print(f"  {summary}")
        
        themes = analysis.get('themes', [])
        if themes:
            print(f"\n🎯 Top Themes ({len(themes)} found):")
            for i, theme in enumerate(themes[:3], 1):
                print(f"\n  {i}. {theme.get('name', 'Unknown')}")
                print(f"     Mentions: {theme.get('mentions', 0)}")
                
                sentiment_pct = theme.get('sentiment_percentage', {})
                print(f"     Sentiment: {sentiment_pct.get('positive', 0)}% positive, "
                      f"{sentiment_pct.get('negative', 0)}% negative")
                
                print(f"     Recommendation: {theme.get('recommendation', 'N/A')}")
    
    metadata = result.get('metadata', {})
    print(f"\n⏱️ Performance:")
    print(f"  Fetch time: {metadata.get('fetch_time_seconds', 0):.2f}s")
    print(f"  Analysis time: {metadata.get('analysis_time_seconds', 0):.2f}s")
    print(f"  Total time: {metadata.get('total_time_seconds', 0):.2f}s")
    
    print("\n" + "=" * 70)
    print("✅ Analysis Complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("ReviewsIQ - Complete Pipeline Test")
    print("=" * 70 + "\n")
    
    print("Test 1: Analyze Starbucks in Chicago")
    print("-" * 70 + "\n")
    
    result = analyze_business("Starbucks", "Chicago")
    
    if result:
        print_results(result)
    else:
        print("❌ Analysis failed")
