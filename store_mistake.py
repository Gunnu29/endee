import requests
from embedding import get_embedding

ENDEE_URL = "http://localhost:8000/vectors"


def store_mistake(text, fix):
    if not (isinstance(text, str) and text.strip() and isinstance(fix, str) and fix.strip()):
        raise ValueError("Both mistake and fix must be non-empty strings.")
    embedding = get_embedding(text)
    data = {
        "vector": embedding,
        "metadata": {
            "mistake": text,
            "fix": fix
        }
    }
    try:
        response = requests.post(ENDEE_URL, json=data, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f"Error storing mistake: {e}")

if __name__ == "__main__":
    m = input("Mistake: ")
    f = input("Fix: ")
    store_mistake(m, f)