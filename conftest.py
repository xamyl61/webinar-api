import os

from dotenv import load_dotenv
import requests
import pytest

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" else "https://release-gs.qa-playground.com/api/v1"


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={
            "X-Task-Id": "API-6",
            "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
        }
    )
    assert response.status_code == 205