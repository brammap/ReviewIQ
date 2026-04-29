# ReviewsIQ: Week 1 Project Checklist
## Sakthi & Bhuvana - April 30 - May 6, 2026

---

## WEEK 1 OVERVIEW

| | Date | Sakthi (Backend) | Bhuvana (Frontend) | Sync |
|---|---|---|---|---|
| **Day 1** | **Thu, Apr 30** | Build scraper | Build input page | Daily standup |
| **Day 2** | **Fri, May 1** | Claude integration | Loading screen | Daily standup |
| **Day 3** | **Sat, May 2** | Integration + testing | Dashboard UI | Daily standup |
| **Day 4** | **Sun, May 3** | Ready for frontend | Polish UI | Daily standup |
| **Day 5** | **Mon, May 4** | Polish + fixes | Final testing | Daily standup |
| **Sync Call** | **Wed, May 6 @ 5 PM** | **CONNECT BACKEND ↔ FRONTEND** | **30 mins** | ✅ **INTEGRATION** |

---

## WEEK 1 SCHEDULE

```
Thursday, Apr 30  → Day 1 starts (you both build separately)
Friday, May 1     → Day 2 (continue building)
Saturday, May 2   → Day 3 (integration on backend, dashboard on frontend)
Sunday, May 3     → Day 4 (refinement)
Monday, May 4     → Day 5 (final polish)
Tuesday, May 5    → Rest/buffer day (catch up if needed)
Wednesday, May 6  → Sync Call at 5 PM (connect everything)
```

---

# SAKTHI'S CHECKLIST - BACKEND

## DAY 1: Thursday, April 30 - Google Reviews Scraper (4 hours)

### Morning Setup (1 hour)
- [ ] Install Playwright: `pip install playwright`
- [ ] Create folder structure:
  ```
  ReviewsIQ/
  ├── backend.py (your main file)
  ├── scraper.py (scraping code)
  ├── analyzer.py (Claude code - later)
  └── requirements.txt
  ```
- [ ] Watch Playwright tutorial (20 mins): YouTube "Playwright Python tutorial"
- [ ] Create `scraper.py` file

### Build Scraper (2 hours)
- [ ] Write `fetch_reviews(url)` function that:
  - [ ] Takes Google Business URL as input
  - [ ] Scrapes reviews from Google
  - [ ] Extracts: rating (1-5), text, date
  - [ ] Returns list of reviews
- [ ] Test with 1 real Google Business URL
- [ ] Make sure it fetches 50+ reviews

### Test & Commit (1 hour)
- [ ] Test scraper works correctly
- [ ] Add comments to your code
- [ ] Commit to GitHub:
  ```bash
  git add scraper.py
  git commit -m "Day 1 (Apr 30): Add Google reviews scraper"
  git push origin main
  ```

### End of Day 1 (Thursday, Apr 30) Checklist
- [ ] `scraper.py` is written
- [ ] Tested with real URL
- [ ] Returns clean review data
- [ ] Pushed to GitHub
- [ ] Send Bhuvana: "✅ Day 1 Scraper done! (Apr 30)"

---

## DAY 2: Friday, May 1 - Claude API Integration (3 hours)

### Setup (30 mins)
- [ ] Install Anthropic SDK: `pip install anthropic`
- [ ] Create `analyzer.py` file
- [ ] Get API key from https://console.anthropic.com/

### Build Claude Integration (2 hours)
- [ ] Write `analyze_reviews(reviews)` function that:
  - [ ] Takes list of reviews as input
  - [ ] Calls Claude API with prompt from `claude_review_analysis_prompt_reviewsiq.md`
  - [ ] Parses JSON response
  - [ ] Returns analysis data:
    ```python
    {
      "sentiment_score": 58,
      "sentiment_breakdown": {...},
      "summary": "...",
      "themes": [...]
    }
    ```
- [ ] Test with reviews from Day 1
- [ ] Make sure it returns valid JSON

### Error Handling (30 mins)
- [ ] Add try/except for API errors
- [ ] Handle invalid JSON responses
- [ ] Add helpful error messages

### Test & Commit (30 mins)
- [ ] Test analyzer works correctly
- [ ] Add comments to code
- [ ] Commit to GitHub:
  ```bash
  git add analyzer.py
  git commit -m "Day 2 (May 1): Add Claude API integration"
  git push origin main
  ```

### End of Day 2 (Friday, May 1) Checklist
- [ ] `analyzer.py` is written
- [ ] Tested with real reviews
- [ ] Returns valid JSON
- [ ] Error handling works
- [ ] Pushed to GitHub
- [ ] Send Bhuvana: "✅ Day 2 Claude integration done! (May 1)"

---

## DAY 3: Saturday, May 2 - Integration + Testing (2 hours)

### Combine Everything (1 hour)
- [ ] Create `main.py` that:
  - [ ] Imports `scraper.py` and `analyzer.py`
  - [ ] Takes Google URL as input
  - [ ] Calls `fetch_reviews(url)`
  - [ ] Calls `analyze_reviews(reviews)`
  - [ ] Returns final analysis JSON
- [ ] Write simple function documentation

### End-to-End Testing (45 mins)
- [ ] Test with 3+ real Google Business URLs
- [ ] Check output is correct
- [ ] Make sure sentiment score is reasonable
- [ ] Check themes make sense
- [ ] Fix any bugs

### Final Polish (15 mins)
- [ ] Remove debug print statements
- [ ] Add comments
- [ ] Clean up code
- [ ] Commit to GitHub:
  ```bash
  git add main.py
  git commit -m "Day 3 (May 2): Complete backend integration"
  git push origin main
  ```

### End of Day 3 (Saturday, May 2) Checklist
- [ ] `main.py` is written
- [ ] Tested with multiple real businesses
- [ ] Output is clean and correct
- [ ] Code is readable
- [ ] Pushed to GitHub
- [ ] Send Bhuvana: "✅ Day 3 Backend ready! (May 2)"

---

## DAY 4: Sunday, May 3 - Refinement + Documentation (2 hours)

### Code Quality (1 hour)
- [ ] Review your code
- [ ] Add docstrings (explanations for each function)
- [ ] Clean up variable names
- [ ] Add error messages
- [ ] Test one more time

### Documentation (30 mins)
- [ ] Create simple README in `backend/` folder
- [ ] Explain what each file does
- [ ] Show how to use `main.py`

### Prepare for Integration (30 mins)
- [ ] Make sure code is ready for Bhuvana to use
- [ ] Write a simple guide on how to call your function
- [ ] Commit:
  ```bash
  git add .
  git commit -m "Day 4 (May 3): Backend refinement and documentation"
  git push origin main
  ```

### End of Day 4 (Sunday, May 3) Checklist
- [ ] Code is polished
- [ ] Documentation is written
- [ ] Ready for Wednesday sync
- [ ] All pushed to GitHub

---

## DAY 5: Monday, May 4 - Final Polish + Ready for Week 2 (2 hours)

### Testing (1 hour)
- [ ] Test with 2 more real businesses
- [ ] Make sure everything still works
- [ ] Check for any edge cases

### Final Review (30 mins)
- [ ] Code looks professional
- [ ] No bugs or errors
- [ ] Documentation is clear

### Commit Final Version (30 mins)
- [ ] Commit:
  ```bash
  git add .
  git commit -m "Day 5 (May 4): Final backend polish"
  git push origin main
  ```

### End of Day 5 (Monday, May 4) Checklist
- [ ] Backend is production-ready
- [ ] All code on GitHub
- [ ] Documentation complete
- [ ] Ready to sync with Bhuvana Wednesday

---

## WEDNESDAY, MAY 6 @ 5 PM: Sync Call (30 mins)

### Before Call (Tue, May 5)
- [ ] Make sure all code is pushed to GitHub
- [ ] Copy your `main.py` function
- [ ] Prepare to explain how Bhuvana should use it

### During Call (Wed, May 6 @ 5 PM)
- [ ] Share your `main.py` function with Bhuvana
- [ ] Explain what it takes as input and returns
- [ ] Test together with a real URL
- [ ] Help Bhuvana integrate it into her app
- [ ] Debug any issues

### After Call
- [ ] Any final fixes
- [ ] Celebrate - Week 1 backend is done! 🎉

---

---

# BHUVANA'S CHECKLIST - FRONTEND

## DAY 1: Thursday, April 30 - Streamlit Setup + Input Page (3 hours)

### Setup (1 hour)
- [ ] Install Streamlit: `pip install streamlit`
- [ ] Install Python if not already (https://www.python.org/downloads/)
- [ ] Create `app.py` file
- [ ] Watch Streamlit tutorial (20 mins): https://docs.streamlit.io/library/get-started

### Build Input Page (1.5 hours)
- [ ] Open `app.py`
- [ ] Add:
  ```python
  import streamlit as st
  
  st.title("ReviewsIQ")
  st.subtitle("AI-powered review analysis for small businesses")
  
  url = st.text_input("Enter your Google Business URL")
  button = st.button("Analyze My Reviews")
  ```
- [ ] Test locally: `streamlit run app.py`
- [ ] Should see: Title, Subtitle, Input field, Button

### Styling (30 mins)
- [ ] Make it look professional:
  - [ ] Add colors (use `st.markdown()` for CSS)
  - [ ] Adjust spacing
  - [ ] Make font bigger
  - [ ] Add an icon or image (optional)
- [ ] Test it looks good

### Test & Commit (30 mins)
- [ ] Test input page works
- [ ] Button responds to clicks
- [ ] Commit to GitHub:
  ```bash
  git add app.py
  git commit -m "Day 1 (Apr 30): Add input page"
  git push origin main
  ```

### End of Day 1 (Thursday, Apr 30) Checklist
- [ ] `app.py` is created
- [ ] Input page works
- [ ] Looks professional
- [ ] Pushed to GitHub
- [ ] Send Sakthi: "✅ Day 1 Input page done! (Apr 30)"

---

## DAY 2: Friday, May 1 - Loading State (2 hours)

### Add Progress Bar (1 hour)
- [ ] Add to `app.py`:
  ```python
  if button:
      progress_bar = st.progress(0)
      
      # Update progress
      progress_bar.progress(33)  # 33%
      st.write("✓ Reading reviews from Google...")
      
      progress_bar.progress(66)  # 66%
      st.write("⏳ Analyzing sentiment and themes...")
      
      progress_bar.progress(100)  # 100%
      st.write("⏳ Generating recommendations...")
  ```
- [ ] Test it works

### Polish Loading Screen (1 hour)
- [ ] Make messages look nice
- [ ] Add emojis (✓, ⏳, ✅)
- [ ] Make progress bar smooth
- [ ] Test timing (should take 5-10 seconds)

### Test & Commit (30 mins)
- [ ] Test loading screen works
- [ ] Looks professional
- [ ] Timing is right
- [ ] Commit to GitHub:
  ```bash
  git add app.py
  git commit -m "Day 2 (May 1): Add loading state with progress bar"
  git push origin main
  ```

### End of Day 2 (Friday, May 1) Checklist
- [ ] Loading screen is built
- [ ] Progress bar works
- [ ] Looks professional
- [ ] Pushed to GitHub
- [ ] Send Sakthi: "✅ Day 2 Loading screen done! (May 1)"

---

## DAY 3: Saturday, May 2 - Dashboard UI (3 hours)

### Build Summary Box (45 mins)
- [ ] Add to `app.py` (after loading screen):
  ```python
  # Fake data for now
  summary = "Customers love your friendly staff, but pricing and scheduling frustrate them."
  
  st.subheader("Summary")
  st.write(summary)
  ```
- [ ] Make it look nice (bigger text, nice styling)

### Build Sentiment Cards (1 hour)
- [ ] Add 3 metric cards:
  ```python
  col1, col2, col3 = st.columns(3)
  
  with col1:
      st.metric("Positive", "50%", "🟢")
  
  with col2:
      st.metric("Neutral", "17%", "⚪")
  
  with col3:
      st.metric("Negative", "33%", "🔴")
  ```
- [ ] Test they display correctly
- [ ] Make colors match theme

### Build Theme Cards (1 hour)
- [ ] Add expandable theme cards:
  ```python
  st.subheader("Top Issues from Customers")
  
  with st.expander("🔴 Pricing (67% negative)"):
      st.write("Mentions: 4")
      st.write('"Prices 30% higher than competitors"')
      st.write('"Can\'t afford regular service"')
      st.write("**Action:** Review pricing vs competitors")
  
  # Repeat for other themes
  ```
- [ ] Add 3-5 theme cards
- [ ] Use fake data for now

### Test & Commit (15 mins)
- [ ] Test dashboard displays all components
- [ ] Everything looks nice
- [ ] Expanders work properly
- [ ] Commit to GitHub:
  ```bash
  git add app.py
  git commit -m "Day 3 (May 2): Add complete dashboard UI"
  git push origin main
  ```

### End of Day 3 (Saturday, May 2) Checklist
- [ ] Summary box added
- [ ] Sentiment cards added
- [ ] Theme cards added
- [ ] Dashboard looks professional
- [ ] All fake data for testing
- [ ] Pushed to GitHub
- [ ] Send Sakthi: "✅ Day 3 Dashboard UI done! (May 2)"

---

## DAY 4: Sunday, May 3 - Polish + Final Testing (2 hours)

### Design Polish (1 hour)
- [ ] Review dashboard appearance
- [ ] Adjust colors (make them match brand)
- [ ] Adjust spacing (padding, margins)
- [ ] Adjust fonts (size, weight)
- [ ] Add icons where helpful
- [ ] Make sure mobile-friendly (if possible)

### Functionality Testing (45 mins)
- [ ] Test all buttons work
- [ ] Test all expanders work
- [ ] Test loading screen works
- [ ] Test input page validation

### Final Review (15 mins)
- [ ] Everything looks professional
- [ ] No broken layouts
- [ ] All text is readable
- [ ] Commit:
  ```bash
  git add app.py
  git commit -m "Day 4 (May 3): Polish dashboard design"
  git push origin main
  ```

### End of Day 4 (Sunday, May 3) Checklist
- [ ] Dashboard is polished
- [ ] All features work
- [ ] Looks professional
- [ ] Ready for Wednesday sync

---

## DAY 5: Monday, May 4 - Final Preparation (2 hours)

### Code Review (1 hour)
- [ ] Check code is clean
- [ ] Add comments
- [ ] Remove test code
- [ ] Make variable names clear

### Prepare for Integration (45 mins)
- [ ] Get ready to receive Sakthi's code
- [ ] Understand how to use his `main.py` function
- [ ] Test you can import and use it

### Final Commit (15 mins)
- [ ] Commit:
  ```bash
  git add app.py
  git commit -m "Day 5 (May 4): Final frontend preparation"
  git push origin main
  ```

### End of Day 5 (Monday, May 4) Checklist
- [ ] Code is clean and documented
- [ ] Ready to integrate with backend
- [ ] All pushed to GitHub

---

## WEDNESDAY, MAY 6 @ 5 PM: Sync Call (30 mins)

### Before Call (Tuesday, May 5)
- [ ] Make sure all frontend code is on GitHub
- [ ] Prepare to receive Sakthi's backend code
- [ ] Test your app one more time

### During Call (Wednesday, May 6 @ 5 PM)
- [ ] Receive Sakthi's `main.py` function
- [ ] Copy it into your `app.py`
- [ ] Replace fake data with real function calls
- [ ] Test end-to-end with a real Google URL
- [ ] Debug any issues together

### After Call
- [ ] Finish integration
- [ ] Test thoroughly
- [ ] Commit final version

---

---

# BOTH: DAILY STANDUP

## Every Morning (5 mins)

**Send a message in Slack/Discord/WhatsApp:**

### Sakthi's Template
```
✅ Yesterday: [What I finished]
🚀 Today: [What I'm starting]
⚠️ Blocker: [Any problems?]
📅 Date: [Today's date]
```

### Bhuvana's Template
```
✅ Yesterday: [What I finished]
🚀 Today: [What I'm starting]
⚠️ Blocker: [Any problems?]
📅 Date: [Today's date]
```

### Example Messages

**Sakthi - Thursday, Apr 30 (Day 1):**
```
✅ Yesterday: N/A (Day 1)
🚀 Today: Building fetch_reviews() scraper function
⚠️ Blocker: None
📅 Apr 30
```

**Bhuvana - Friday, May 1 (Day 2):**
```
✅ Yesterday: Built input page with URL field and button (Apr 30)
🚀 Today: Adding loading screen with progress bar
⚠️ Blocker: None
📅 May 1
```

---

# WEEK 1 AT A GLANCE

| Day | Date | Sakthi | Bhuvana |
|-----|------|--------|---------|
| 1 | Thu, Apr 30 | Scraper | Input page |
| 2 | Fri, May 1 | Claude API | Loading screen |
| 3 | Sat, May 2 | Integration | Dashboard UI |
| 4 | Sun, May 3 | Refinement | Polish |
| 5 | Mon, May 4 | Final polish | Final prep |
| Buffer | Tue, May 5 | Catch up if needed | Catch up if needed |
| Sync | Wed, May 6 @ 5 PM | **CONNECT** | **CONNECT** |

---

# SUCCESS CHECKLIST (End of Week 1 - Wednesday, May 6)

## Sakthi's Deliverables
- [ ] `scraper.py` - Fetches Google reviews
- [ ] `analyzer.py` - Calls Claude API
- [ ] `main.py` - Combines both functions
- [ ] All code on GitHub
- [ ] Code is clean and documented
- [ ] Works with multiple real businesses

## Bhuvana's Deliverables
- [ ] `app.py` - Complete Streamlit app
- [ ] Input page working
- [ ] Loading screen working
- [ ] Dashboard UI complete
- [ ] All code on GitHub
- [ ] Looks professional and polished

## Together
- [ ] Backend + Frontend connected (Wed, May 6)
- [ ] End-to-end testing done
- [ ] User can paste URL and see analysis
- [ ] No major bugs
- [ ] All code on GitHub
- [ ] Ready for Week 2 deployment

---

# WEEK 2 PREVIEW (May 7-13)

### Monday, May 6: Test with Real Business
- Contact lawn care business
- Paste their Google URL
- Get real feedback

### Tuesday-Thursday, May 7-9: Refine
- Fix bugs based on feedback
- Improve UI based on feedback
- Optimize performance

### Friday, May 10: Deploy
- Deploy to Streamlit Cloud
- Live at: reviewsiq.streamlit.app
- Celebrate! 🎉

---

# GITHUB COMMIT MESSAGES (Template)

**Sakthi:**
```
Day 1 (Apr 30): Add Google reviews scraper
Day 2 (May 1): Add Claude API integration
Day 3 (May 2): Complete backend integration
Day 4 (May 3): Backend refinement and documentation
Day 5 (May 4): Final backend polish
```

**Bhuvana:**
```
Day 1 (Apr 30): Add input page
Day 2 (May 1): Add loading state with progress bar
Day 3 (May 2): Add complete dashboard UI
Day 4 (May 3): Polish dashboard design
Day 5 (May 4): Final frontend preparation
```

---

# COMMUNICATION CHECKLIST

- [ ] Both joined same GitHub repo
- [ ] Both know meeting time (Wednesday, May 6 @ 5 PM)
- [ ] Both know daily standup expectation (every morning, 5 mins)
- [ ] Both have each other's contact (Slack/Discord/WhatsApp)
- [ ] Both understand their role
- [ ] Both committed to timeline (Apr 30 - May 6)

---

# FINAL NOTES

**Sakthi:** Focus on making backend work correctly. Don't worry about UI.
**Bhuvana:** Focus on making UI look great. Don't worry about how analysis works.

**Together:** You're building something real. Stay focused, ship daily, help each other.

**Timeline:**
- **Apr 30 - May 4:** Build separately (both coding)
- **May 5:** Buffer day (catch up if needed)
- **May 6 @ 5 PM:** Sync call (connect backend ↔ frontend)
- **May 7-10:** Week 2 (refine + deploy)

**Let's ship this! 🚀**
