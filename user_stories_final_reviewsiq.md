# ReviewsIQ: User Flows & User Stories
## Version 2.0 | Final with Integrated Feedback

---

## Primary User Definition

**Who they are:** Small business owner or manager, 1-3 locations, 10-500 Google reviews, actively customer-facing. Limited time, low data literacy, high motivation to protect their reputation and understand what customers think.

[COMMENT: Good definition. Consider adding for clarity: "Focuses on 1-3 location businesses to keep scope tight for MVP. Post-v1 can expand to enterprise."]

**What they need:** The answer, not the analysis. They want to know what to fix, not how to read a chart.

[COMMENT: ✅ Excellent. This is the core insight that drives all acceptance criteria. Keep this as north star for all design decisions.]

---

## User Flow 1 — First Time User (Core Flow)

**Trigger:** User hears about the tool from a friend, social post, or search. Lands on homepage.

**Flow:**
- Homepage
- Sees headline + one-line value prop
- Pastes Google Business URL into input field
- Hits "Analyze My Reviews"
- Loading screen ("Reading your reviews... Finding patterns... Building your summary...")
- Dashboard loads with:
  - Plain-language summary paragraph (top)
  - Sentiment breakdown — % positive / neutral / negative
  - Theme cards (top 3-5, ranked by impact)
  - Actionable recommendations per theme
- User reads summary + browses theme cards
- User copies or screenshots their insight
- [Optional] Prompted to save results or return later

**Success moment:** User reads the plain-language summary and says "yes, that's exactly what I've been hearing from customers."

---

## User Flow 2 — User With a Specific Problem

**Trigger:** Business owner has noticed their rating dropped recently and wants to understand why.

**Flow:**
- Lands on homepage with a specific question in mind ("why did my rating drop?")
- Enters Google Business URL
- Dashboard loads
- Scans sentiment breakdown — sees dip
- Looks at theme cards sorted by impact
- Identifies the rising complaint cluster (e.g., "Wait Times")
- Reads verbatim customer quotes under that theme
- Reads the action recommendation (e.g., "Consider additional staffing Friday-Saturday evenings")
- Has a specific, evidence-backed action to take

**Success moment:** User leaves with one concrete thing to change, not just a feeling that something is wrong.

[COMMENT: This flow is currently MVP-scope. Trend lines (comparing last 3 months) come in User Story 3 post-v1.]

---

## User Flow 3 — Returning User (Post-V1)

**Trigger:** User made operational changes based on last analysis and wants to see if it worked.

**Flow:**
- Returns to tool after 6-8 weeks
- Logs in (post-v1 feature)
- Hits "Refresh Analysis"
- Sees updated dashboard with trend comparison
- Notices "Wait Time complaints down 28% since last analysis"
- Reads new theme that has emerged ("Parking" — 12 new mentions)
- Gets new recommendation for emerging issue
- Shares month-over-month summary with business partner or manager

**Success moment:** User sees their changes actually worked. This is the retention hook — the tool becomes more valuable over time.

[COMMENT: This is POST-MVP (User Story 3). Requires: user accounts, saved history, trend comparison logic.]

---

# User Stories

## User Story 1 — The Insight Seeker

**Story:**
> "As a small business owner with limited time, I want to understand what my customers are collectively saying without reading every review, so that I can quickly identify what's working and what needs to change."

[COMMENT: Strong story. Motivation is clear and dual-part (problems + validation). Connects directly to primary user definition: limited time + wants answers, not analysis.]

### Acceptance Criteria

**Criterion 1:** User enters a Google Business URL and receives a synthesized result within 60 seconds on first load; cached results load instantly on repeat analyses

[COMMENT: 30 seconds is too tight.
- Google API fetch time: 5-15 seconds
- Claude API analysis: 10-30 seconds
- Network latency: 3-5 seconds
- Realistic total: 40-60 seconds

Set realistic expectations upfront or users will mark tool as "slow." If you want sub-30s, show a real-time progress bar ("Reading reviews... Analyzing themes...") to make it feel faster.]

---

**Criterion 2:** Output includes a plain-language summary (2 sentences maximum) that leads with the #1 business issue, includes one positive finding, and uses 6th-grade vocabulary (no jargon like "sentiment," "metrics," or "recurring themes")

Example: "Customers love your friendly staff, but parking is confusing and wait times are frustrating."

[COMMENT: "Plain-language paragraph" was too vague. Specific constraints:
- Max 2 sentences (scannable)
- Leads with biggest problem (action-oriented)
- Includes one positive (balanced, not all-doom)
- 6th-grade reading level (target small business owner, not data analyst)
Your friend building the UI needs exact specs, not interpretation room.]

---

**Criterion 3:** Top 3-5 themes are displayed, ranked by negative sentiment frequency (highest-impact problems first), showing: theme name, frequency count, sentiment split (e.g., "8 negative, 2 neutral, 1 positive"), and recency indicator (e.g., "mentioned in last 30 days")

[COMMENT: "3-5 themes" with "frequency counts" was unclear on ranking logic. High-frequency ≠ high-impact.
Example problem: "Parking" mentioned 50 times but 95% positive = LOW PRIORITY. "Wait times" mentioned 20 times, 80% negative = HIGH PRIORITY.

Ranking by negative sentiment ensures action-takers see what matters. Also add recency so user knows if it's a current problem.]

---

**Criterion 4:** Each theme includes 2-3 verbatim customer quotes as evidence, with quote length capped at 20 words (use "..." for longer quotes to keep dashboard scannable)

Example quote: "The staff were friendly, but I waited 45 minutes just for check-in." (18 words)

[COMMENT: Long, rambling quotes kill readability and scannability. Remember your user has limited time. Cap at 20 words; use "..." if longer. Keeps dashboard fast to scan.]

---

## User Story 2 — The Action Taker

**Story:**
> "As a business owner who has identified a problem area, I want specific and prioritized recommendations based on my actual reviews, so that I know exactly what to fix first rather than guessing."

[COMMENT: ✅ Good story. Clear motivation (tired of guessing). Connects directly to User Story 1 (identifies problem → wants action).]

### Acceptance Criteria

**Criterion 1:** Each theme generates exactly one recommendation using this format: "[Specific action] because [evidence: X customers mentioned this], expected to [outcome]"

Example (good): "Add a parking sign with directions (mentioned in 12 recent reviews) to reduce check-in confusion"

Example (bad): "Improve customer communication"

[COMMENT: "Concrete, specific recommendation" is subjective. Define the exact format so Claude's output is consistent. Without a template, you'll get vague advice like "improve service." Format forces specificity.]

---

**Criterion 2:** Recommendations must reference the specific theme name + include a number (e.g., "12 customers mentioned wait times"), avoid banned words, and be achievable within 30 days by a small business owner without major capital

Banned words: "improve," "enhance," "listen," "synergy," "optimize," "leverage"

Use instead: "add," "post," "ask," "send," "schedule," "hire," "change"

Example (good): "Customers keep saying wait times are long. Hire one more person Friday-Saturday evenings."

Example (bad): "Sentiment analysis reveals recurring metric around operational efficiency."

[COMMENT: "Not generic advice" needs guardrails. Define banned words + action verbs so Claude + your team have explicit rules. Also "30 days" sets realistic action window for small business owner (not "transform entire company").]

---

**Criterion 3:** Recommendations are ranked by impact score: (# negative mentions) × (% negative sentiment). Theme with most negative recent mentions appears first. Themes with <3 supporting reviews marked "low-confidence" and appear last.

Example formula:
- "Pricing": 24 mentions × 83% negative = 19.9 impact score
- "Wait Times": 18 mentions × 65% negative = 11.7 impact score
- "Parking": 3 mentions × 70% negative = 2.1 impact score (marked "low-confidence")

Ranking: Pricing (1st) → Wait Times (2nd) → Parking (3rd, flagged)

[COMMENT: "Highest-impact issue appears first" was vague. Define the formula explicitly so Claude + your team know exact logic. Also filter out noise: a single complaint about parking shouldn't trigger a recommendation. <3 mentions = low-confidence flag.]

---

**Criterion 4:** Language is 6th-grade reading level. Banned words: "sentiment," "metrics," "optimize," "leverage," "synergy," "actionable insights," "data-driven," "recurring"

Use simple verbs: "feeling," "number," "better," "use," "try," "fix"

[COMMENT: "Plain English, no jargon" was too vague. Explicit banned word list helps Claude's prompt + your team stay focused on simple language. Your user is a lawn care owner, not a data analyst.]

---

# Edge Cases & Constraints

## Minimum Data Threshold

- **If <10 reviews:** Show message "Collect at least 10 reviews to get reliable themes. Come back once you reach 10+."
- **If 10-30 reviews:** Show themes but include flag "Early stage — patterns may shift as more reviews come in"
- **If 30+ reviews:** Full analysis, no caveats

[COMMENT: Why? 5 reviews with 3 complaints about parking ≠ a real pattern. Protects against false positives and maintains credibility with user.]

---

## Language Support (MVP)

- MVP supports English reviews only
- Non-English reviews are counted in overall review total but excluded from theme analysis
- User sees transparency: "Analyzed 87 English reviews. 13 reviews in other languages were not analyzed."

[COMMENT: Why? Claude can handle multiple languages, but for MVP scope, stick to English. Be transparent about exclusions so users don't distrust results or think data is missing.]

---

## All-Positive Reviews Edge Case

- **If business has 4-5 stars only, no complaints:** Show sentiment + themes customers praise (e.g., "Staff friendliness," "Quality of work")
- Recommendations become "reinforce what's working" instead of "fix problems"
- Example: "Keep promoting your team's friendliness — it's your strongest differentiator (mentioned in 34 reviews)"

[COMMENT: Why? Not every business has crises. Handle the happy path too so tool stays useful for successful businesses. Don't force-fit complaints where none exist.]

---

## Metrics Required for MVP Display

Based on User Stories 1 & 2, your Claude output must include:

1. **Overall Sentiment Score** (0-100%) — "72% of customers are satisfied"
2. **Sentiment Breakdown** — % Positive | Neutral | Negative (displayed as 3 cards)
3. **Top 3-5 Themes** — With mention counts, ranked by impact
4. **Theme Sentiment** — Positive % vs Negative % per theme
5. **Theme Impact Score** — Used to rank recommendations (highest impact first)
6. **Actionable Recommendations** — 1 per theme, formatted as specified

[COMMENT: Post-MVP can add: NPS, trend comparison, confidence indicators, word clouds. For now, these 6 metrics support both user stories.]

---

## Claude Prompt Output Format (JSON)

Your Claude prompt should return structured data in this format:

```json
{
  "sentiment_score": 72,
  "sentiment_breakdown": {
    "positive": 72,
    "neutral": 16,
    "negative": 12
  },
  "summary": "Customers love your friendly staff, but parking is confusing and wait times are frustrating.",
  "themes": [
    {
      "rank": 1,
      "name": "Pricing",
      "mentions": 24,
      "percentage_of_feedback": 19,
      "sentiment": {
        "positive": 3,
        "neutral": 1,
        "negative": 20,
        "positive_percent": 12,
        "negative_percent": 83
      },
      "quotes": [
        "Your prices are 30% higher than competitors",
        "Great work but I can't afford regular maintenance"
      ],
      "impact_score": 19.9,
      "recommendation": "Review pricing vs competitors. Consider package discounts for recurring customers."
    },
    {
      "rank": 2,
      "name": "Scheduling",
      "mentions": 18,
      "percentage_of_feedback": 14,
      "sentiment": {
        "positive": 2,
        "neutral": 4,
        "negative": 12,
        "positive_percent": 11,
        "negative_percent": 67
      },
      "quotes": [
        "Would book more often if online scheduling was available",
        "No weekend appointments when I need them"
      ],
      "impact_score": 12.1,
      "recommendation": "Add online booking system. Extend weekend hours on Saturdays."
    }
  ]
}
```

[COMMENT: This JSON structure ensures Claude outputs consistent, parseable data that your Streamlit frontend can display reliably.]

---

## Version History

- **v1.0** — Initial user stories (working draft)
- **v2.0** — Integrated feedback from architecture review
  - Clarified acceptance criteria (specific, measurable, testable)
  - Added edge cases & constraints
  - Added metrics requirements
  - Added Claude output format
  - Removed ambiguous language; replaced with explicit guardrails

---

## Next Steps

1. ✅ Approve this document with Bhuvana
2. 🔨 Write the Claude prompt for review analysis
3. 🏗️ Set up Streamlit app structure
4. 🚀 Implement review fetching (Playwright)
5. 🎯 Build dashboard UI
6. 🧪 Test with real business contact
