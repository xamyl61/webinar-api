import os
from dotenv import load_dotenv

load_dotenv()


class Headers:

    basic = {
        "X-Task-Id": "API-3",
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
    }