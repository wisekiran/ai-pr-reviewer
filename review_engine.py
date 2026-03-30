from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def review_code(diff):

    prompt = f"""You are a senior software engineer reviewing a pull request.

Analyze the diff below and identify bugs, security issues, performance concerns,
and missing tests. Be concise and specific.

Diff:
{diff[:8000]}
"""

    try:
        print("Running AI review via Gemini...")
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=prompt
        )
        print("Gemini review complete.")
        return response.text

    except Exception as e:
        print("Gemini API error:", e)
        return """
AI review unavailable.

Basic automated review:
- Check for missing error handling
- Verify input validation
- Ensure tests cover new logic
"""
