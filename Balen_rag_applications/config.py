import os
from pathlib import Path
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
# Get the directory of this config file
BASE_DIR = Path(__file__).parent

# Use absolute paths based on script location instead of relative paths
TEXT_FILE_PATH = os.getenv("TEXT_FILE_PATH", str(BASE_DIR / "data" / "balen_story.txt"))
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", str(BASE_DIR / "faiss_store" / "index.faiss"))


# ─── Validation ────────────────────────────────────────────────────────────────
def validate_environment():
    """Validate that all required environment variables are set."""
    required_vars = {
        "RAG_API_KEY": RAG_API_KEY,
        "EMBEDDING_URL": EMBEDDING_URL,
        "EMBEDDING_MODEL": EMBEDDING_MODEL,
        "COMPLETION_URL": COMPLETION_URL,
        "COMPLETION_MODEL": COMPLETION_MODEL,
    }
    
    missing_vars = [name for name, value in required_vars.items() if not value]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            f"Please set these in your .env file or Streamlit Cloud secrets."
        )


# Validate on import
validate_environment()