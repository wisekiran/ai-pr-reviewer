import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def review_code(diff):

    prompt = f"""You are a senior software engineer reviewing a pull request.

Analyze the diff below and identify bugs, security issues, performance concerns,
and missing tests. Be concise and specific.

Diff:
{diff[:8000]}
"""

    try:
        print("Running AI review via Claude API...")
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        print("Claude review complete.")
        return response.content[0].text

    except Exception as e:
        print("Claude API error:", e)
        return """
AI review unavailable.

Basic automated review:
- Check for missing error handling
- Verify input validation
- Ensure tests cover new logic
"""
