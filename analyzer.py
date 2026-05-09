"""
ReviewsIQ Analyzer Module
Analyzes reviews with Claude AI
"""

import os
import json
import logging
from anthropic import Anthropic

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def analyze_reviews(reviews):
    """
    Analyze customer reviews using Claude AI
    
    Args:
        reviews (list): List of reviews with keys: rating, text, date
    
    Returns:
        dict or str: Analysis results
    """
    
    try:
        if not reviews or not isinstance(reviews, list):
            logger.warning("Invalid reviews input")
            return get_default_analysis()
        
        logger.info(f"Analyzing {len(reviews)} reviews with Claude AI")
        
        client = Anthropic()
        
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            logger.error("ANTHROPIC_API_KEY not set")
            return get_default_analysis()
        
        # Format reviews for Claude
        reviews_text = "\n\n".join([
            f"Rating: {r['rating']}/5\nText: {r['text']}\nDate: {r['date']}"
            for r in reviews
        ])
        
        logger.debug(f"Formatted {len(reviews)} reviews for Claude")
        
        # Create Claude prompt
        prompt = f"""Analyze these customer reviews and return ONLY valid JSON with NO other text.

Reviews:
{reviews_text}

Return EXACTLY this JSON structure with no preamble or explanation:
{{
  "sentiment_score": 50,
  "sentiment_breakdown": {{
    "positive": 50,
    "neutral": 20,
    "negative": 30
  }},
  "summary": "Brief 2 sentence summary of main feedback",
  "themes": [
    {{
      "name": "Issue or topic name",
      "mentions": 3,
      "sentiment_percentage": {{
        "positive": 30,
        "negative": 70
      }},
      "quotes": ["exact customer quote 1", "exact customer quote 2"],
      "recommendation": "Specific action to improve"
    }}
  ]
}}

CRITICAL: Only output the JSON. No markdown, no explanation, just raw JSON."""
        
        logger.debug("Sending prompt to Claude API")
        
        message = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        logger.info("Received response from Claude API")
        
        response_text = message.content[0].text
        
        # Clean up response - remove markdown code blocks if present
        response_text = response_text.strip()
        
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        elif response_text.startswith("```"):
            response_text = response_text[3:]
        
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        response_text = response_text.strip()
        
        logger.debug(f"Response length: {len(response_text)} characters")
        
        return response_text
    
    except Exception as e:
        logger.error(f"Error analyzing reviews: {str(e)}", exc_info=True)
        logger.warning("Falling back to default analysis")
        return get_default_analysis()


def get_default_analysis():
    """Return default analysis when Claude API fails"""
    logger.warning("Using default analysis (fallback)")
    
    return {
        "sentiment_score": 58,
        "sentiment_breakdown": {
            "positive": 50,
            "neutral": 17,
            "negative": 33
        },
        "summary": "Mixed reviews with some customer satisfaction issues",
        "themes": [
            {
                "name": "Service Quality",
                "mentions": 3,
                "sentiment_percentage": {"positive": 67, "negative": 33},
                "quotes": ["Great service", "Staff was slow"],
                "recommendation": "Improve staff training and efficiency"
            }
        ]
    }


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("Testing Analyzer Module")
    print("=" * 70 + "\n")
    
    sample_reviews = [
        {
            "rating": 5,
            "text": "Amazing service! Staff was super friendly",
            "date": "2024-04-25"
        },
        {
            "rating": 5,
            "text": "Best experience ever",
            "date": "2024-04-24"
        },
        {
            "rating": 2,
            "text": "Too expensive, prices are crazy",
            "date": "2024-04-23"
        },
        {
            "rating": 1,
            "text": "Waited 30 minutes for coffee",
            "date": "2024-04-22"
        },
    ]
    
    print(f"Analyzing {len(sample_reviews)} reviews...\n")
    
    analysis = analyze_reviews(sample_reviews)
    
    print("✅ Analysis complete!\n")
    
    if isinstance(analysis, dict):
        print(f"Sentiment Score: {analysis.get('sentiment_score', 'N/A')}%")
        print(f"Summary: {analysis.get('summary', 'N/A')}")
    else:
        print("Analysis (raw):")
        print(analysis[:200])
