import requests
from embedding import get_embedding

ENDEE_SEARCH = "http://localhost:8000/search"


def search_similar(text, top_k=3):
    embedding = get_embedding(text)

    response = requests.post(
        ENDEE_SEARCH,
        json={"vector": embedding, "top_k": top_k}
    )

    response.raise_for_status()

    return response.json()