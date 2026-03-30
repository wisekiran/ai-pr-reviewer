# AI PR Reviewer Bot

An automated pull request reviewer powered by Google Gemini AI. When a new PR is opened, the bot instantly fetches the diff, runs it through an AI model, and posts a detailed code review comment — fully automated, deployed on the cloud.

## 🚀 Live Demo

Want to see it in action? Open a pull request on the demo repository and the bot will automatically review your code within seconds:

**👉 [Open a PR to test the bot](https://github.com/wisekiran/demo-ai-pr-reviewer)**

> Just create any file or make any change, open a PR, and watch the bot comment.

---

## How It Works

1. A pull request is opened on GitHub
2. GitHub sends a webhook event to the deployed server
3. The app authenticates via GitHub App and fetches the PR diff
4. The diff is sent to Google Gemini AI for analysis
5. The AI-generated review is posted as a comment on the PR — automatically

---

## Tech Stack

- **Python** + **Flask** — webhook server
- **Google Gemini API** — AI model for code review
- **GitHub Apps API** — authentication and posting comments
- **Render** — cloud deployment (always on, no local setup needed)

---

## Features

- ✅ Automatically triggers on every new pull request
- ✅ Identifies bugs, security issues, and performance concerns
- ✅ Flags missing tests and input validation gaps
- ✅ Posts review as a native GitHub PR comment
- ✅ Deployed 24/7 on the cloud — no local server needed

---

## Project Structure

```
ai-pr-reviewer/
├── app.py              # Flask webhook server
├── review_engine.py    # AI review logic (Google Gemini)
├── github_utils.py     # Fetch PR diff, post comments
├── github_auth.py      # GitHub App JWT authentication
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment config
└── README.md
```

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/wisekiran/ai-pr-reviewer.git
cd ai-pr-reviewer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file:

```
GITHUB_APP_ID=your_github_app_id
GITHUB_WEBHOOK_SECRET=your_webhook_secret
GEMINI_API_KEY=your_gemini_api_key
GITHUB_PRIVATE_KEY=your_private_key_contents
```

### 4. Run the server

```bash
python app.py
```

---

## Deployment

This app is deployed on [Render](https://render.com) using the included `render.yaml` config. The `GITHUB_PRIVATE_KEY`, `GEMINI_API_KEY`, and other secrets are stored as environment variables in the Render dashboard.
