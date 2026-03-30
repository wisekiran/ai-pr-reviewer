import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"  # Free, runs locally via Ollama


def review_code(diff):

    prompt = f"""You are a senior software engineer reviewing a pull request.

Analyze the diff below and identify bugs, security issues, performance concerns,
and missing tests. Be concise and specific.

Diff:
{diff[:8000]}
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }, timeout=60)

        response.raise_for_status()
        return response.json()["response"]

    except Exception as e:
        print("AI error:", e)
        return """
AI review unavailable. Make sure Ollama is running: `ollama serve`

Basic automated review:
- Check for missing error handling
- Verify input validation
- Ensure tests cover new logic
"""
