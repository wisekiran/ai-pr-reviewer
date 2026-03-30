# AI PR Reviewer

An automated pull request reviewer powered by a local LLM (Llama 3.2 via Ollama). When a new PR is opened in your GitHub repository, this bot fetches the diff, runs it through an AI model, and posts a code review comment automatically — all running on your own machine, for free.

---

## How It Works

1. A pull request is opened on GitHub
2. GitHub sends a webhook event to this app
3. The app fetches the PR diff using the GitHub API
4. The diff is sent to Llama 3.2 running locally via Ollama
5. The AI review is posted as a comment on the PR

---

## Tech Stack

- **Python** + **Flask** — webhook server
- **Ollama** + **Llama 3.2** — local AI model for code review (free, no API key needed)
- **GitHub Apps API** — authentication and posting comments
- **ngrok** — exposes local server to GitHub webhooks

---

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed
- [ngrok](https://ngrok.com) installed
- A GitHub App created and installed on your repository

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-pr-reviewer.git
cd ai-pr-reviewer
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull the AI model

```bash
ollama pull llama3.2
```

### 4. Create a GitHub App

- Go to **https://github.com/settings/apps** → New GitHub App
- Set the webhook URL to your ngrok URL + `/webhook` (e.g. `https://your-ngrok-url.ngrok-free.app/webhook`)
- Set a webhook secret (any string, e.g. `supersecret123`)
- Under **Permissions**, set:
  - **Issues** → Read and Write
  - **Pull requests** → Read-only
- Generate and download a **private key** (.pem file) — place it in the project folder as `private-key.pem`
- Install the app on your repository

### 5. Configure environment variables

Copy `.env` and fill in your values:

```
GITHUB_APP_ID=your_github_app_id_here
GITHUB_WEBHOOK_SECRET=your_webhook_secret_here
```

---

## Running the App

Open **3 terminals** and run one command in each:

**Terminal 1 — Start Ollama**
```bash
ollama serve
```

**Terminal 2 — Start the Flask server**
```bash
python app.py
```

**Terminal 3 — Expose to the internet via ngrok**
```bash
ngrok http 5000
```

Copy the ngrok forwarding URL (e.g. `https://xxxx.ngrok-free.app`) and make sure it matches the webhook URL in your GitHub App settings.

---

## Usage

Open a new pull request on your GitHub repository. Within a few seconds, the bot will post an automated code review comment on the PR.

---

## Project Structure

```
ai-pr-reviewer/
├── app.py              # Flask webhook server
├── review_engine.py    # AI review logic (Ollama/Llama 3.2)
├── github_utils.py     # Fetch PR diff, post comments
├── github_auth.py      # GitHub App JWT authentication
├── private-key.pem     # GitHub App private key (not committed)
├── .env                # Environment variables (not committed)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Notes

- `private-key.pem` and `.env` should never be committed to GitHub — add them to `.gitignore`
- The app only reviews PRs with `action: opened` — reopened or updated PRs are ignored
- Ollama must be running before starting the Flask server
