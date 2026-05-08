import numpy as np
from utils.embedding import get_embedding


def retrieve_top_k(query, index, chunk_mapping, k=5):
    """
    Retrieve the top-k most relevant chunks for a given query.

    Args:
        query (str): The user's question.
        index (faiss.Index): The FAISS index.
        chunk_mapping (list[str]): List of text chunks mapped to index positions.
        k (int): Number of top results to retrieve.

    Returns:
        list[str]: Top-k relevant text chunks.
    """
    query_embedding = get_embedding(query)

    if query_embedding is None:
        raise ValueError("Failed to get embedding for the query.")

    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"), k
    )

    results = []
    for idx in indices[0]:
        if idx < len(chunk_mapping):
            results.append(chunk_mapping[idx])

    return results