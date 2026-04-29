# ReviewsIQ: Claude Review Analysis Prompt
## Production-Ready Prompt for Google Reviews Analysis

---

## System Prompt (Send First)

```
You are an expert business analyst specializing in customer sentiment analysis and actionable business recommendations.

Your task is to analyze customer reviews and extract meaningful insights that small business owners can act on immediately.

Core principles:
1. Always provide specific, actionable recommendations (not generic advice)
2. Back every insight with actual customer quotes and mention counts
3. Rank problems by impact (most negative mentions first)
4. Use simple language (6th-grade reading level, no jargon)
5. Return structured JSON only - no markdown, no explanations

You will receive:
- A list of customer reviews (each with rating and text)
- The total number of reviews analyzed

You must return valid JSON matching the exact schema provided.
```

---

## Main Analysis Prompt (Send After System Prompt)

```
Analyze the following customer reviews and return ONLY a valid JSON object.

REVIEWS TO ANALYZE:
---
{REVIEWS_HERE}
---

Total Reviews: {TOTAL_COUNT}

ANALYSIS INSTRUCTIONS:

1. SENTIMENT SCORE (0-100):
   - Calculate as: (count of 4-5 star reviews / total reviews) × 100
   - Round to nearest integer
   - Example: 91 positive out of 127 total = (91/127) × 100 = 71.65 ≈ 72

2. SENTIMENT BREAKDOWN:
   - Positive: 4-5 star reviews (%)
   - Neutral: 3 star reviews (%)
   - Negative: 1-2 star reviews (%)
   - All three must sum to 100%

3. SUMMARY (2 sentences maximum):
   - Sentence 1: What customers like (one positive)
   - Sentence 2: What frustrates them (one major issue)
   - Use simple language. No words: sentiment, metrics, recurring, actionable, optimize, leverage
   - 6th-grade reading level
   - Example: "Customers love your friendly staff, but parking is confusing and wait times are frustrating."

4. THEMES EXTRACTION:
   - Identify top 3-5 recurring topics customers mention
   - Each theme must appear in at least 3 reviews
   - Rank by: (negative mention count) × (% negative sentiment for that theme)
     - Example: "Pricing" = 20 negative mentions × 0.85 (85% of pricing mentions are negative) = impact score 17
   - Themes with impact score <3 are low-confidence (flag as such)

5. FOR EACH THEME:
   a. Theme name (concise, 2-3 words max)
      - Good: "Pricing", "Wait Times", "Staff Friendliness"
      - Bad: "Customer perception of pricing strategy", "Temporal service delays"
   
   b. Mention count (how many reviews mention this)
      - Count all mentions (positive + negative + neutral)
   
   c. Percentage of feedback
      - (theme mentions / total reviews) × 100
   
   d. Sentiment breakdown FOR THIS THEME ONLY:
      - Count mentions by sentiment (positive, neutral, negative)
      - Calculate percentages
      - Example: "Pricing" appears in 24 reviews: 3 positive (12%), 1 neutral (4%), 20 negative (84%)
   
   e. Customer quotes (2-3 verbatim quotes)
      - MUST be exact text from reviews
      - Cap at 20 words per quote (use "..." if longer)
      - Choose quotes that show WHY customers feel this way
      - Include mix of negative/positive for that theme
      - Example quotes for "Pricing":
        * "Your prices are 30% higher than competitors"
        * "Great service but I can't afford monthly maintenance"
   
   f. Impact score (for ranking)
      - Calculate: (negative mentions for this theme) × (% negative sentiment for this theme)
      - Used to rank themes from highest to lowest
   
   g. Recommendation (1 per theme, specific + actionable)
      - Format: "[Specific action] because [evidence: X customers mentioned this], which should [expected outcome]"
      - MUST include actual mention count (e.g., "because 24 customers mentioned this")
      - MUST be doable within 30 days with no major capital
      - Action verbs: add, post, hire, schedule, send, change, create, improve (list is longer than these examples)
      - BANNED words (do not use): improve, enhance, listen, optimize, leverage, synergy, actionable, data-driven, recurring
      - Examples:
        * ✅ GOOD: "Review pricing against local competitors. Consider package discounts for recurring customers (mentioned in 24 reviews)."
        * ✅ GOOD: "Add an online booking system and extend Saturday hours (requested in 18 reviews)."
        * ❌ BAD: "Improve pricing strategy"
        * ❌ BAD: "Enhance customer experience"
      - Low-confidence themes (<3 mentions) still get a recommendation, but it's flagged as "low-confidence"

6. PRIORITY BADGES:
   - 🔴 HIGH PRIORITY: Impact score >15, >20% of feedback, 75%+ negative
   - 🟠 MEDIUM PRIORITY: Impact score 5-15, 10-20% of feedback, 50-75% negative
   - ✅ STRENGTH: 75%+ positive mentions (reinforce, don't fix)

EDGE CASES:
- If <10 reviews total: Return error message "Minimum 10 reviews required for analysis"
- If all reviews 4-5 stars (no negative): Still extract themes, but recommendations become "reinforce" not "fix"
- If a theme appears only once: Flag as "low-confidence - only 1 mention"
- If reviews in multiple languages: Analyze only English reviews, note count of excluded reviews

OUTPUT FORMAT (REQUIRED):
Return ONLY this exact JSON structure, no markdown formatting, no additional text:

{
  "status": "success",
  "total_reviews_analyzed": NUMBER,
  "sentiment_score": NUMBER (0-100),
  "sentiment_breakdown": {
    "positive": NUMBER,
    "neutral": NUMBER,
    "negative": NUMBER
  },
  "summary": "STRING (2 sentences max, simple language)",
  "themes": [
    {
      "rank": NUMBER (1, 2, 3...),
      "name": "STRING (2-3 words)",
      "mentions": NUMBER,
      "percentage_of_feedback": NUMBER (0-100),
      "sentiment": {
        "positive_count": NUMBER,
        "neutral_count": NUMBER,
        "negative_count": NUMBER,
        "positive_percent": NUMBER,
        "neutral_percent": NUMBER,
        "negative_percent": NUMBER
      },
      "quotes": [
        "STRING (verbatim, <20 words)",
        "STRING (verbatim, <20 words)",
        "STRING (verbatim, <20 words)"
      ],
      "impact_score": NUMBER,
      "priority": "STRING (HIGH/MEDIUM/STRENGTH or LOW_CONFIDENCE)",
      "recommendation": "STRING (specific action + evidence + outcome)"
    }
  ]
}

VALIDATION BEFORE RETURNING:
- ✓ sentiment_score is 0-100
- ✓ sentiment_breakdown sums to 100
- ✓ All themes ranked 1-5
- ✓ All quotes are <20 words
- ✓ All recommendations reference actual theme + mention count
- ✓ No banned words in summary or recommendations
- ✓ JSON is valid (test with JSON parser)
- ✓ Themes ranked by impact_score descending

Return ONLY the JSON object. No preamble, no explanation, no markdown backticks.
```

---

## How to Use This Prompt in Your Code

### Python Example (Using Anthropic SDK):

```python
import json
from anthropic import Anthropic

def analyze_reviews(reviews_list: list, business_name: str) -> dict:
    """
    Analyze customer reviews using Claude.
    
    Args:
        reviews_list: List of dicts with keys: rating (1-5), text (str), date (optional)
        business_name: Name of the business
    
    Returns:
        Parsed JSON response with analysis
    """
    
    # Format reviews for Claude
    formatted_reviews = []
    for i, review in enumerate(reviews_list, 1):
        rating = review.get('rating', 'N/A')
        text = review.get('text', '')
        date = review.get('date', 'Unknown date')
        formatted_reviews.append(
            f"Review {i} [Rating: {rating}/5, Date: {date}]:\n{text}"
        )
    
    reviews_text = "\n---\n".join(formatted_reviews)
    
    # Create the prompt
    system_prompt = """You are an expert business analyst specializing in customer sentiment analysis and actionable business recommendations.

Your task is to analyze customer reviews and extract meaningful insights that small business owners can act on immediately.

Core principles:
1. Always provide specific, actionable recommendations (not generic advice)
2. Back every insight with actual customer quotes and mention counts
3. Rank problems by impact (most negative mentions first)
4. Use simple language (6th-grade reading level, no jargon)
5. Return structured JSON only - no markdown, no explanations"""
    
    user_prompt = f"""Analyze the following customer reviews and return ONLY a valid JSON object.

REVIEWS TO ANALYZE:
---
{reviews_text}
---

Total Reviews: {len(reviews_list)}

[... rest of main prompt ...]"""
    
    # Call Claude API
    client = Anthropic()
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    
    # Extract and parse JSON response
    response_text = message.content[0].text
    
    try:
        analysis = json.loads(response_text)
        return analysis
    except json.JSONDecodeError as e:
        return {
            "status": "error",
            "message": f"Failed to parse Claude response: {e}",
            "raw_response": response_text
        }


# Example usage:
if __name__ == "__main__":
    sample_reviews = [
        {
            "rating": 5,
            "text": "Excellent service! The staff was so friendly and professional.",
            "date": "2024-04-20"
        },
        {
            "rating": 2,
            "text": "Prices are way too high. Competitors charge half of what you do.",
            "date": "2024-04-19"
        },
        # ... more reviews
    ]
    
    result = analyze_reviews(sample_reviews, "Sunny Days Lawn Care")
    
    if result.get("status") == "success":
        print(f"Sentiment Score: {result['sentiment_score']}%")
        print(f"Summary: {result['summary']}")
        for theme in result['themes']:
            print(f"\n{theme['priority']}: {theme['name']}")
            print(f"  Mentions: {theme['mentions']}")
            print(f"  Recommendation: {theme['recommendation']}")
    else:
        print(f"Error: {result['message']}")
```

### Streamlit Integration Example:

```python
import streamlit as st
from anthropic import Anthropic
import json

st.set_page_config(page_title="ClearVoice", layout="wide")

st.title("ClearVoice")
st.subtitle("AI-powered review analysis for small businesses")

# Input
business_input = st.text_input(
    "Enter your business name or Google Business URL:",
    placeholder="e.g., Sunny Days Lawn Care"
)

if st.button("Analyze My Reviews", type="primary"):
    with st.spinner("Reading your reviews..."):
        # Step 1: Fetch reviews (your backend function)
        reviews = fetch_google_reviews(business_input)
        
        if len(reviews) < 10:
            st.error("Please provide a business with at least 10 reviews")
        else:
            with st.spinner("Analyzing sentiment and themes..."):
                # Step 2: Analyze with Claude
                analysis = analyze_reviews(reviews, business_input)
            
            if analysis.get("status") == "success":
                # Display results
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Positive", f"{analysis['sentiment_breakdown']['positive']}%")
                with col2:
                    st.metric("Neutral", f"{analysis['sentiment_breakdown']['neutral']}%")
                with col3:
                    st.metric("Negative", f"{analysis['sentiment_breakdown']['negative']}%")
                
                st.info(analysis['summary'])
                
                st.subheader("Top Issues from Your Customers")
                for theme in analysis['themes']:
                    with st.expander(
                        f"{theme['priority']}: {theme['name']} ({theme['mentions']} mentions)"
                    ):
                        st.write(f"**Sentiment:** {theme['sentiment']['negative_percent']}% negative")
                        st.write("**Customer quotes:**")
                        for quote in theme['quotes']:
                            st.write(f"- \"{quote}\"")
                        st.write(f"**Action:** {theme['recommendation']}")
            else:
                st.error(f"Analysis failed: {analysis.get('message')}")
```

---

## Testing the Prompt

### Test Case 1: Normal Input
**Reviews:** 127 reviews, 91 positive, 20 neutral, 16 negative

**Expected Output:**
- sentiment_score: ~72
- Top theme should be "Pricing" if mentioned 24 times with 83% negative
- Recommendation should be specific: "Review pricing vs competitors (24 mentions)"

### Test Case 2: Low Data
**Reviews:** 8 reviews

**Expected Output:**
```json
{
  "status": "error",
  "message": "Minimum 10 reviews required for analysis"
}
```

### Test Case 3: All Positive
**Reviews:** 50 reviews, all 4-5 stars

**Expected Output:**
- sentiment_score: 100
- Themes should be positive (e.g., "Staff Friendliness")
- Recommendations should reinforce, not fix: "Keep promoting your team's friendliness..."

---

## Tips for Best Results

1. **Prompt Refinement:** If Claude isn't following the format, add more examples or be more explicit
2. **Review Quality:** Better reviews = better analysis (long form > star-only)
3. **Error Handling:** Always catch JSON parse errors and return useful error messages
4. **Token Usage:** This prompt uses ~500-1000 tokens per analysis (depends on review count)
5. **Caching:** Consider caching results for the same business (save API costs)

---

## Version History

- **v1.0** — Initial production-ready prompt
  - Full schema definition
  - Edge case handling
  - Code examples
  - Testing guidelines
