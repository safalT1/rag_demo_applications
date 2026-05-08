import os
from dotenv import load_dotenv

# Load all values from .env file
load_dotenv()

# ─── API Key ───────────────────────────────────────────────────────────────────
RAG_API_KEY = os.getenv("RAG_API_KEY")

# ─── Embedding ─────────────────────────────────────────────────────────────────
EMBEDDING_URL   = os.getenv("EMBEDDING_URL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# ─── Completion ────────────────────────────────────────────────────────────────
COMPLETION_URL   = os.getenv("COMPLETION_URL")
COMPLETION_MODEL = os.getenv("COMPLETION_MODEL")

# ─── Chunking ──────────────────────────────────────────────────────────────────
CHUNK_MAX_WORDS = int(os.getenv("CHUNK_MAX_WORDS", 100))

# ─── Retrieval ─────────────────────────────────────────────────────────────────
TOP_K = int(os.getenv("TOP_K", 5))

# ─── Paths ─────────────────────────────────────────────────────────────────────
TEXT_FILE_PATH   = os.getenv("TEXT_FILE_PATH")
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH")