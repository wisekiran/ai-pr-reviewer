import jwt
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("GITHUB_APP_ID")

with open("private-key.pem", "r") as f:
    PRIVATE_KEY = f.read()


def generate_jwt():

    payload = {
        "iat": int(time.time()) - 60,
        "exp": int(time.time()) + 600,
        "iss": APP_ID,
    }

    encoded_jwt = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")

    return encoded_jwt


def get_installation_token(installation_id):

    jwt_token = generate_jwt()

    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"

    response = requests.post(url, headers=headers)

    print("Token response status:", response.status_code)

    if response.status_code != 201:
        print("Token error:", response.text)
        return None

    return response.json()["token"]
