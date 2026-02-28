import requests
from embedding import get_embedding

ENDEE_SEARCH = "http://localhost:8000/search"


def search_similar(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Query text must be a non-empty string.")
    embedding = get_embedding(text)
    try:
        response = requests.post(ENDEE_SEARCH, json={"vector": embedding, "top_k": 3}, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error searching for similar mistakes: {e}")
        return []

if __name__ == "__main__":
    q = input("New mistake: ")
    results = search_similar(q)

    for r in results:
        print("\nSimilar mistake:", r["metadata"]["mistake"])
        print("Fix:", r["metadata"]["fix"])

    
    print("\n⚠ Prevention Tip:")
    print("You have made a similar mistake before.")
    print("Review past fixes and check edge cases before solving again.")