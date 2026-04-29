# ReviewsIQ

AI-powered review analysis for small businesses.

## What It Does

ReviewsIQ analyzes customer reviews from Google Business and tells you:
- What customers love ✅
- What frustrates them ❌
- Exactly what to fix 🎯

**Instead of reading 100+ reviews manually, get a dashboard in seconds.**

## Example Output

**Input:** Paste "Sunny Days Lawn Care" (or any Google Business URL)

**Output Dashboard:**
- Overall sentiment: 58%
- Top issues: Pricing (67% negative), Online booking (67% negative)
- Strengths: Friendly staff (100% positive)
- Specific actions: "Review pricing vs competitors," "Add online booking tool"

## Tech Stack

- **Frontend:** Streamlit (Python-based UI)
- **Backend:** Python + Playwright (Google reviews scraper) + Claude API (AI analysis)
- **Deployment:** Streamlit Cloud (free)

## MVP Timeline

- **Week 1:** Frontend UI + Backend scraper
- **Week 2:** Integration + testing
- **Week 3:** Deploy live

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export ANTHROPIC_API_KEY='sk-...'

# Run the app (coming soon)
streamlit run app.py
```

## Team

- **Backend:** Sakthi
- **Frontend:** Bhuvana
- **Status:** 🚧 In Development

## Project Checklist

See [PROJECT_CHECKLIST.md](PROJECT_CHECKLIST.md) for detailed task breakdown.

## Documentation

- [User Stories](user_stories_final_reviewsiq.md) - What we're building
- [Claude Prompt](claude_review_analysis_prompt_reviewsiq.md) - How AI analyzes reviews
- [Testing Guide](TESTING_GUIDE_reviewsiq.md) - How to test the prompt
