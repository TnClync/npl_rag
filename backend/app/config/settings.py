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
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


TOP_K = int(os.getenv("TOP_K"))

FAISS_PATH = os.getenv("FAISS_PATH")

CHUNKS_PATH = os.getenv("CHUNKS_PATH")



# =========================
# VALIDATION (QUAN TRỌNG)
# =========================
if not EMBEDDING_MODEL:
    raise ValueError("❌ EMBEDDING_MODEL is not set!")


MODEL_NAME = os.getenv("MODEL_NAME", "google/gemma-2-2b-it")


HF_TOKEN = os.getenv("HF_TOKEN","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")

LORA_MODEL_PATH = os.getenv(
    "LORA_MODEL_PATH")