import requests
from github_auth import get_installation_token


def get_pr_diff(repo, pr_number, installation_id):

    token = get_installation_token(installation_id)

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.diff",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"

    response = requests.get(url, headers=headers)
    print("Diff fetch status:", response.status_code)

    return response.text


def post_pr_comment(repo, pr_number, installation_id, comment):

    token = get_installation_token(installation_id)

    if not token:
        print("ERROR: Could not get installation token, skipping comment.")
        return

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    data = {"body": comment}

    response = requests.post(url, headers=headers, json=data)

    print("COMMENT STATUS:", response.status_code)
    print("COMMENT RESPONSE:", response.text)
