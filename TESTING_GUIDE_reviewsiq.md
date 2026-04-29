# Testing the ReviewsIQ Prompt: Beginner's Guide
## Step-by-Step Instructions for Testing

---

## What Are We Testing?

We're testing if Claude can:
- Read 12 sample customer reviews
- Analyze them correctly
- Return the data in the right format (JSON)
- Give specific recommendations

It should take **30 minutes max**.

---

## Step 1: Get Your API Key (5 minutes)

An **API key** is like a password that lets your code talk to Claude.

### How to Get It:

1. Go to: https://console.anthropic.com/
2. Click **"Log in"** (create account if you don't have one)
3. Click your profile icon (top right)
4. Click **"API Keys"**
5. Click **"Create Key"**
6. Copy the key (it looks like: `sk-ant-...`)
   - ⚠️ **Save it somewhere safe** — you won't see it again!

**Example API key (fake):**
```
sk-ant-abc123defghijk789mnopqrst...
```

---

## Step 2: Download the Test File (2 minutes)

You already have `test_prompt.py` — it's the file I gave you earlier.

**Save it to a folder on your computer**, for example:
```
~/Documents/reviewsiq/test_prompt.py
```

---

## Step 3: Open Terminal (2 minutes)

A **terminal** is a text-based way to run code on your computer.

### On Mac:
1. Press **Command + Space**
2. Type **"Terminal"**
3. Press **Enter**

### On Windows:
1. Press **Windows Key + R**
2. Type **"cmd"**
3. Press **Enter**

### On Linux:
- Open Terminal from Applications menu

**You should see something like:**
```
user@computer ~ %
```

or

```
C:\Users\user>
```

---

## Step 4: Navigate to Your Folder (2 minutes)

Tell the terminal where your test file is.

### Mac/Linux:
```bash
cd ~/Documents/reviewsiq
```

### Windows:
```bash
cd C:\Users\YourUsername\Documents\reviewsiq
```

**Then check if the file is there:**

### Mac/Linux:
```bash
ls
```

### Windows:
```bash
dir
```

**You should see:**
```
test_prompt.py
```

---

## Step 5: Set Your API Key (2 minutes)

Tell the terminal your API key so Claude can recognize you.

### Mac/Linux:
```bash
export ANTHROPIC_API_KEY='sk-ant-abc123...'
```

### Windows:
```bash
set ANTHROPIC_API_KEY=sk-ant-abc123...
```

**Replace `sk-ant-abc123...` with YOUR actual key.**

**Example (not real):**
```bash
export ANTHROPIC_API_KEY='sk-ant-vF9Q8j2kL3mN4oPqRsT5uVwXyZ1a2b3c4d5e6f7g8h9i'
```

---

## Step 6: Run the Test (3-5 minutes)

Now tell the terminal to run the test:

```bash
python3 test_prompt.py
```

**What happens:**
- Terminal will connect to Claude
- Claude will read 12 sample reviews
- Claude will analyze them
- Claude will return results
- You'll see the output in the terminal

**This takes about 10-20 seconds. Be patient!**

---

## Step 7: Read the Results (10 minutes)

The output will look something like this:

```
================================================================================
ClearVoice: Claude Prompt Test
================================================================================

📝 Test Data: 12 sample reviews
   • 4 positive (5-star)
   • 2 neutral (3-star)
   • 6 negative (1-2 star)

📤 Calling Claude API...

✅ RESPONSE RECEIVED & PARSED
================================================================================
{
  "status": "success",
  "total_reviews_analyzed": 12,
  "sentiment_score": 67,
  "sentiment_breakdown": {
    "positive": 67,
    "neutral": 17,
    "negative": 17
  },
  "summary": "Customers love your friendly staff, but pricing and scheduling are frustrating.",
  "themes": [
    {
      "rank": 1,
      "name": "Pricing",
      "mentions": 4,
      "percentage_of_feedback": 33.3,
      "sentiment": {
        "positive_count": 1,
        "neutral_count": 0,
        "negative_count": 3,
        "positive_percent": 25,
        "neutral_percent": 0,
        "negative_percent": 75
      },
      "quotes": [
        "prices are 30% higher than competitors",
        "Can't afford regular service"
      ],
      "impact_score": 2.25,
      "priority": "HIGH",
      "recommendation": "Review pricing against competitors. Consider package discounts for recurring customers (mentioned in 4 reviews)."
    }
  ]
}

VALIDATION CHECKLIST
================================================================================
✅ Status is 'success'
✅ Sentiment score in range (67)
✅ Sentiment breakdown sums to 100
✅ Summary is 1-2 sentences
✅ Themes count 3-5 (got 4)
✅ All themes have required fields

✅ TEST PASSED - Prompt is production-ready!
```

---

## Understanding the Results

### ✅ If You See "TEST PASSED":

**Congratulations! The prompt works perfectly.** You can now:
1. Show results to your friend
2. Start building the app
3. Move to the next phase

### ❌ If You See "TEST FAILED":

**Something didn't work.** Common issues:

**Problem 1: "ANTHROPIC_API_KEY not set"**
- **Fix:** Make sure you ran the `export` command correctly
- Paste your key exactly as shown

**Problem 2: "Failed to parse JSON"**
- **Fix:** Claude returned something wrong
- Copy the "Raw response" and share with me
- I can fix the prompt

**Problem 3: "Connection refused"**
- **Fix:** Check your internet connection
- Make sure API key is correct

---

## Common Mistakes to Avoid

❌ **Don't:**
- Close the terminal while it's running
- Share your API key with anyone
- Run it multiple times at once (costs money per request)

✅ **Do:**
- Wait for it to finish (takes 10-20 seconds)
- Keep your API key secret
- Run once, check results, then stop

---

## What Each Part Means

### Sentiment Score: 67%
- Out of 100 customers, about 67 are happy
- 67% gave 4-5 stars
- 17% gave 3 stars
- 17% gave 1-2 stars

### Themes: Pricing, Scheduling, Staff
- These are the **topics customers mention most**
- "Pricing" = 4 reviews mention this
- "Scheduling" = 4 reviews mention this
- "Staff" = 6 reviews mention this

### Priority: HIGH vs MEDIUM
- 🔴 HIGH = Fix this first (lots of negative mentions)
- 🟠 MEDIUM = Fix after HIGH
- ✅ STRENGTH = This is good, keep it!

### Recommendation: "Review pricing..."
- This is the **action to take**
- Based on actual customer feedback
- Specific and doable within 30 days

---

## Next Steps After Testing

If TEST PASSED ✅:

1. **Take a screenshot** of the results
2. **Share with your friend:**
   - "Hey, the prompt is working! Here's what Claude returned..."
   - Show the sentiment score, themes, and recommendations
3. **Confirm timeline:**
   - Can you both commit 2-3 weeks?
   - Split: You = backend, Friend = frontend
4. **Start Week 1:**
   - You build Google reviews fetcher
   - Friend builds Streamlit UI

---

## Troubleshooting

**Q: How much will this cost?**
A: Each test costs about $0.01-0.03 (very cheap). Free tier includes $5 credits.

**Q: Can I run it multiple times?**
A: Yes, but each run costs money. Run once, check results, then stop.

**Q: What if Claude gives different results?**
A: That's normal! Claude varies slightly. As long as format is valid, it's fine.

**Q: Do I need to run this for the app?**
A: No, this is just to test. Once you build the app, your code will handle it automatically.

---

## Questions?

If something goes wrong:
1. Copy the error message
2. Take a screenshot
3. Share with me
4. I'll help you fix it

**You've got this! 🚀**
