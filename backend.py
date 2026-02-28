from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

database = []


class VectorItem(BaseModel):
    vector: List[float]
    metadata: dict


class SearchRequest(BaseModel):
    vector: List[float]
    top_k: int = 3


@app.post("/vectors")
def store_vector(item: VectorItem):
    database.append(item)
    return {"message": "Stored successfully"}


@app.post("/search")
def search_vectors(req: SearchRequest):
    if not database:
        return []

    query_vector = np.array(req.vector)

    results = []

    for item in database:
        stored_vector = np.array(item.vector)

        max_len = max(len(query_vector), len(stored_vector))

        q = np.pad(query_vector, (0, max_len - len(query_vector)))
        s = np.pad(stored_vector, (0, max_len - len(stored_vector)))

        similarity = cosine_similarity([q], [s])[0][0]

        if similarity > 0.3:
            results.append({
                "score": float(similarity),
                "metadata": item.metadata
            })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:req.top_k]