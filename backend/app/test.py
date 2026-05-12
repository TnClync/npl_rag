from model.loader import load_retriever, load_base_model, load_tokenizer
# from model.generation import generate_answer
# if __name__ == "__main__":
#     model = load_base_model()
#     tokenizer = load_tokenizer
#     retriever = load_retriever()
#     test_q = "Người điều khiển xe máy vượt đèn đỏ bị phạt bao nhiêu tiền và có bị trừ điểm giấy phép lái xe không?"

#     print(generate_answer(model, tokenizer,test_q))


from transformers import AutoModelForCausalLM, AutoTokenizer
import os


SAVE_DIR = "backend/app/model/base/gemma2"

os.makedirs(SAVE_DIR, exist_ok=True)

# =========================
# Download tokenizer
# =========================
tokenizer = load_tokenizer()

tokenizer.save_pretrained(SAVE_DIR)

# =========================
# Download model
# =========================
model = load_base_model()

model.save_pretrained(SAVE_DIR)

print("✅ Model saved to:", SAVE_DIR)