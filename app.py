from flask import Flask, request
from github_utils import get_pr_diff, post_pr_comment
from review_engine import review_code

app = Flask(__name__)


@app.route("/")
def home():
    return "AI PR Reviewer running"


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    print("=== WEBHOOK RECEIVED ===")
    print("Action:", data.get("action"))
    print("Repo:", data.get("repository", {}).get("full_name"))
    print("Installation ID:", data.get("installation", {}).get("id"))

    if data["action"] != "opened":
        return {"status": "ignored"}

    repo = data["repository"]["full_name"]
    pr_number = data["pull_request"]["number"]
    installation_id = data["installation"]["id"]

    diff = get_pr_diff(repo, pr_number, installation_id)
    print("Diff length:", len(diff))

    review = review_code(diff)
    print("Review generated, length:", len(review))

    post_pr_comment(repo, pr_number, installation_id, review)

    return {"status": "review posted"}


if __name__ == "__main__":
    app.run(port=5000)
