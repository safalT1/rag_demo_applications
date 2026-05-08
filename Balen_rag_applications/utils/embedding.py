import os
import requests
import numpy as np
import faiss
from config import RAG_API_KEY, EMBEDDING_MODEL, EMBEDDING_URL


def get_embedding(text):
    """
    Get embedding vector for a given text using NVIDIA API.

    Args:
        text (str): Text to embed.

    Returns:
        np.ndarray or None: Embedding vector, or None if request fails.
    """
    headers = {
        "Authorization": f"Bearer {RAG_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": EMBEDDING_MODEL,
        "input": text,
        "input_type": "passage"
    }

    response = requests.post(EMBEDDING_URL, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"Embedding error {response.status_code}: {response.text}")
        return None

    data = response.json()
    return np.array(data["data"][0]["embedding"])


def build_faiss_index(chunks):
    """
    Build a FAISS index from a list of text chunks.

    Args:
        chunks (list[str]): List of text chunks to embed and index.

    Returns:
        tuple: (faiss.Index, list[str]) — the index and chunk mapping.
    """
    print("Building FAISS index...")

    # Get dimension from first chunk
    test_embedding = get_embedding(chunks[0])
    if test_embedding is None:
        raise ValueError("Failed to get embedding for the first chunk. Check your API key.")

    dimension = test_embedding.shape[0]
    index = faiss.IndexFlatL2(dimension)
    chunk_mapping = []

    for i, chunk in enumerate(chunks):
        emb = get_embedding(chunk)
        if emb is None:
            raise ValueError(f"Failed to get embedding for chunk {i}: {chunk[:50]}...")
        index.add(np.array([emb]).astype("float32"))
        chunk_mapping.append(chunk)
        print(f"  Indexed chunk {i + 1}/{len(chunks)}")

    print(f"FAISS index built with {index.ntotal} vectors of dimension {dimension}.")
    return index, chunk_mapping


def save_index(index, path="faiss_store/index.faiss"):
    """Save FAISS index to disk."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    faiss.write_index(index, path)
    print(f"Index saved to {path}")


def load_index(path="faiss_store/index.faiss"):
    """Load FAISS index from disk."""
    index = faiss.read_index(path)
    print(f"Index loaded from {path}")
    return index