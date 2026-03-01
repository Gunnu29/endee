import requests
from embedding import get_embedding

ENDEE_URL = "http://localhost:8000/vectors"


def store_mistake(content: str, fix: str, tags: dict = None):
    if not (content.strip() and fix.strip()):
        raise ValueError("Content and fix must be non-empty")

    embedding = get_embedding(content)

    data = {
        "vector": embedding,
        "metadata": {
            "content": content,
            "fix": fix,
            "tags": tags or {}
        }
    }

    response = requests.post(ENDEE_URL, json=data)
    response.raise_for_status()