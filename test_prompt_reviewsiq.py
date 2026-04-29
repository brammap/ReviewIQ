#!/usr/bin/env python3
"""
ReviewsIQ: Claude Prompt Test Script
Tests the review analysis prompt with sample data
"""

import json
import os
from anthropic import Anthropic

def test_claude_prompt():
    """Test the Claude prompt with sample reviews"""
    
    # Get API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ERROR: ANTHROPIC_API_KEY environment variable not set")
        print("\nTo run this test:")
        print("1. Get your API key from: https://console.anthropic.com/")
        print("2. Set it: export ANTHROPIC_API_KEY='sk-...'")
        print("3. Run this script: python3 test_prompt.py")
        return False
    
    # Initialize client
    client = Anthropic(api_key=api_key)
    
    # Sample reviews (realistic data)
    sample_reviews = [
        {"rating": 5, "text": "Excellent service! The staff is incredibly friendly and professional. Best experience I've had."},
        {"rating": 5, "text": "Your team is amazing. They went above and beyond to help us. Highly recommend!"},
        {"rating": 4, "text": "Good work overall, but the pricing is quite high compared to other companies."},
        {"rating": 2, "text": "Great quality but prices are 30% higher than competitors. Can't afford regular service."},
        {"rating": 3, "text": "Service is fine but it's hard to book appointments. No online scheduling option."},
        {"rating": 2, "text": "Would use them more if I could book online. Also wish they had weekend availability."},
        {"rating": 1, "text": "Waited 45 minutes and was charged extra. Long wait times and poor communication."},
        {"rating": 5, "text": "Staff friendliness is unmatched. They treat you like family. Will keep using them."},
        {"rating": 2, "text": "Confusing parking situation. Hard to find where to go when I first arrived."},
        {"rating": 4, "text": "Good service, professional team. Just wish it was more affordable."},
        {"rating": 5, "text": "Best customer service ever. The team is so kind and helpful!"},
        {"rating": 3, "text": "Decent work but scheduling is a pain. Need better online booking."}
    ]
    
    # Format reviews
    formatted_reviews = []
    for i, review in enumerate(sample_reviews, 1):
        rating = review['rating']
        text = review['text']
        formatted_reviews.append(f"Review {i} [Rating: {rating}/5]:\n{text}")
    
    reviews_text = "\n---\n".join(formatted_reviews)
    
    # System prompt
    system_prompt = """You are an expert business analyst specializing in customer sentiment analysis and actionable business recommendations.

Your task is to analyze customer reviews and extract meaningful insights that small business owners can act on immediately.

Core principles:
1. Always provide specific, actionable recommendations (not generic advice)
2. Back every insight with actual customer quotes and mention counts
3. Rank problems by impact (most negative mentions first)
4. Use simple language (6th-grade reading level, no jargon)
5. Return structured JSON only - no markdown, no explanations"""
    
    # User prompt
    user_prompt = f"""Analyze these {len(sample_reviews)} customer reviews and return ONLY valid JSON.

REVIEWS:
---
{reviews_text}
---

Return ONLY this JSON structure (no markdown, no explanation):

{{
  "status": "success",
  "total_reviews_analyzed": {len(sample_reviews)},
  "sentiment_score": NUMBER_0_TO_100,
  "sentiment_breakdown": {{
    "positive": PERCENT,
    "neutral": PERCENT,
    "negative": PERCENT
  }},
  "summary": "2 sentences max. What customers like + what frustrates them.",
  "themes": [
    {{
      "rank": 1,
      "name": "THEME_NAME",
      "mentions": COUNT,
      "percentage_of_feedback": PERCENT,
      "sentiment": {{
        "positive_count": NUM,
        "neutral_count": NUM,
        "negative_count": NUM,
        "positive_percent": PERCENT,
        "neutral_percent": PERCENT,
        "negative_percent": PERCENT
      }},
      "quotes": ["quote 1 max 20 words", "quote 2 max 20 words"],
      "impact_score": NUM,
      "priority": "HIGH/MEDIUM/STRENGTH",
      "recommendation": "Specific action (mentioned in X reviews)"
    }}
  ]
}}

Rules:
- Sentiment score = (4-5 star reviews / total) × 100
- Identify top 3-5 themes (each appears 3+ times)
- Rank by impact: (negative mentions) × (% negative sentiment)
- Quotes: verbatim, max 20 words each
- Recommendations: specific + reference mention count
- No banned words: improve, enhance, optimize, leverage, synergy
- All percentages sum correctly"""
    
    print("=" * 80)
    print("ReviewsIQ: Claude Prompt Test")
    print("=" * 80)
    print(f"\n📝 Test Data: {len(sample_reviews)} sample reviews")
    print("   • 4 positive (5-star)")
    print("   • 2 neutral (3-star)")  
    print("   • 6 negative (1-2 star)")
    print("\n📤 Calling Claude API...\n")
    
    try:
        message = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=2000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}]
        )
        
        response_text = message.content[0].text
        
        # Try to parse JSON
        try:
            analysis = json.loads(response_text)
        except json.JSONDecodeError:
            print("❌ Failed to parse JSON response")
            print(f"\nRaw response:\n{response_text}")
            return False
        
        # Print full response
        print("✅ RESPONSE RECEIVED & PARSED")
        print("=" * 80)
        print(json.dumps(analysis, indent=2))
        
        # Validate
        print("\n" + "=" * 80)
        print("VALIDATION CHECKLIST")
        print("=" * 80)
        
        checks = [
            (analysis.get("status") == "success", "Status is 'success'"),
            (isinstance(analysis.get("sentiment_score"), (int, float)), "Sentiment score is a number"),
            (0 <= analysis.get("sentiment_score", -1) <= 100, f"Sentiment score in range (got {analysis.get('sentiment_score')})"),
            (sum(analysis.get("sentiment_breakdown", {}).values()) == 100, "Sentiment breakdown sums to 100"),
            (1 <= analysis.get("summary", "").count(".") <= 2, "Summary is 1-2 sentences"),
            (3 <= len(analysis.get("themes", [])) <= 5, f"Themes count 3-5 (got {len(analysis.get('themes', []))})"),
            (all("rank" in t and "name" in t and "recommendation" in t for t in analysis.get("themes", [])), "All themes have required fields"),
        ]
        
        all_passed = True
        for passed, check_name in checks:
            status = "✅" if passed else "❌"
            print(f"{status} {check_name}")
            if not passed:
                all_passed = False
        
        # Print summary
        print("\n" + "=" * 80)
        print("ANALYSIS RESULTS")
        print("=" * 80)
        
        breakdown = analysis.get("sentiment_breakdown", {})
        score = analysis.get("sentiment_score", 0)
        print(f"\n📊 Overall Sentiment: {score}%")
        print(f"   ✅ Positive: {breakdown.get('positive', 0)}%")
        print(f"   ⚪ Neutral:  {breakdown.get('neutral', 0)}%")
        print(f"   ❌ Negative: {breakdown.get('negative', 0)}%")
        
        print(f"\n💬 Summary:")
        print(f"   {analysis.get('summary', 'N/A')}")
        
        print(f"\n🎯 Top Issues Identified:")
        for theme in analysis.get("themes", []):
            priority = theme.get("priority", "?")
            name = theme.get("name", "?")
            mentions = theme.get("mentions", 0)
            percent = theme.get("percentage_of_feedback", 0)
            neg_percent = theme.get("sentiment", {}).get("negative_percent", 0)
            
            print(f"\n   {priority}: {name.upper()}")
            print(f"      • Mentioned: {mentions} reviews ({percent:.1f}% of feedback)")
            print(f"      • Sentiment: {neg_percent:.0f}% negative")
            print(f"      • Action: {theme.get('recommendation', 'N/A')}")
        
        # Final verdict
        print("\n" + "=" * 80)
        if all_passed:
            print("✅ TEST PASSED - Prompt is production-ready!")
            print("\nNext steps:")
            print("1. Integrate this prompt into your backend")
            print("2. Build the Google reviews fetcher (Playwright)")
            print("3. Connect to Streamlit frontend")
            return True
        else:
            print("⚠️ SOME CHECKS FAILED - Review the results above")
            return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    success = test_claude_prompt()
    exit(0 if success else 1)
