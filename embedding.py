from sentence_transformers import SentenceTransformer

# Local semantic model (downloads once)
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text must be non-empty")

    embedding = model.encode(text)
    return embedding.tolist()