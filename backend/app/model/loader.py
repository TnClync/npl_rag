from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
import torch
import faiss
import json
import os

# =========================
# CONFIG
# =========================
from config.settings import MODEL_NAME, HF_TOKEN, LORA_MODEL_PATH, TOP_K, FAISS_PATH, CHUNKS_PATH
from vectorstore.retriever import TrafficLawRetriever
from vectorstore.embedding_model import embedding_model


# =========================
# QUANT CONFIG (4-bit)
# =========================
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16  # an toàn hơn bfloat16
)

# =========================
# LOAD BASE MODEL
# =========================
def load_base_model():
    model = AutoModelForCausalLM.from_pretrained(
        "/home/clyde/User/NLP_fin/inference/backend/app/model/base/gemma2",
        quantization_config=bnb_config,
        device_map="auto",
        attn_implementation="eager",
        token = HF_TOKEN
    )
    model.eval()

    return model

# =========================
# LOAD TOKENIZER
# =========================
def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("/home/clyde/User/NLP_fin/inference/backend/app/model/base/gemma2", local_files_only=True)
    tokenizer.padding_side = "right"
    return tokenizer

# =========================
# LOAD FINE-TUNED MODEL (LoRA)
# =========================
def load_finetuned_model(base_model):
    model = PeftModel.from_pretrained(base_model, LORA_MODEL_PATH)
    model.eval()
    return model



# =========================
# LOAD RETRIEVER
# =========================

def load_index(FAISS_PATH= FAISS_PATH):
    return faiss.read_index(FAISS_PATH)

def load_chunks(CHUNKS_PATH = CHUNKS_PATH):
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    return chunks


def load_embedder():
    return embedding_model



def load_retriever():
    index = load_index()

    chunks = load_chunks()

    embedder = load_embedder()
    retriever = TrafficLawRetriever(
        index=index,
        chunks=chunks,
        embedder=embedder,
        top_k=TOP_K
    )

    return retriever