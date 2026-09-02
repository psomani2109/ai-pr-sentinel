import os
import requests
from google import genai

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
PR_NUMBER = os.getenv("PR_NUMBER")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_pr_diff():
    url = f"https://api.github.com/repos/{REPO_NAME}/pulls/{PR_NUMBER}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.diff",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def analyze_code_with_ai(diff_text):
    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are an automated Senior Software Engineer conducting an automated code review on a GitHub Pull Request.
Examine this git diff:

--- DIFF START ---
{diff_text[:8000]}
--- DIFF END ---

Provide a structured, professional markdown review addressing:
1. Critical Bugs & Edge Cases
2. Algorithmic Efficiency
3. Code Quality & Style
4. Summary & Verdict: State one of: APPROVE, COMMENT, or REQUEST CHANGES.
"""
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )
    return response.text

def post_github_comment(review_body):
    url = f"https://api.github.com/repos/{REPO_NAME}/issues/{PR_NUMBER}/comments"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    payload = {
        "body": f"### 🤖 AI Sentinel PR Review\n\n{review_body}\n\n*Automated review powered by Gemini & GitHub Actions*"
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

if __name__ == "__main__":
    if not PR_NUMBER:
        exit(0)

    diff = get_pr_diff()
    if not diff.strip():
        exit(0)

    review = analyze_code_with_ai(diff)
    post_github_comment(review)
