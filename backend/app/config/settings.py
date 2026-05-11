import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# APP CONFIG
# =========================
APP_NAME = os.getenv("APP_NAME", "RAG API")

# =========================
# EMBEDDING MODEL
# =========================
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING",
    "sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# VALIDATION (QUAN TRỌNG)
# =========================
if not EMBEDDING_MODEL:
    raise ValueError("❌ EMBEDDING_MODEL is not set!")