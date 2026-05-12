import torch

SYSTEM_PROMPT = """Bạn là trợ lý pháp lý chuyên về Luật Trật tự, an toàn giao thông đường bộ Việt Nam 2024.
Hãy trả lời ngắn gọn, chính xác, dựa trên căn cứ pháp luật.
Nếu câu hỏi nằm ngoài phạm vi luật giao thông đường bộ Việt Nam, hãy từ chối trả lời lịch sự."""


def generate_answer(
    model,
    tokenizer,
    question: str,
    context: str = None,
    max_new_tokens: int = 1024,
) -> str:
    """Generate câu trả lời từ model"""

    if context:
        user_content = (
            f"{SYSTEM_PROMPT}\n\n"
            f"### Tài liệu tham khảo:\n{context}\n\n"
            f"### Câu hỏi:\n{question}"
        )
    else:
        user_content = f"{SYSTEM_PROMPT}\n\n{question}"

    # Format theo Gemma 2 ChatML
    prompt = (
        f"<start_of_turn>user\n{user_content}<end_of_turn>\n"
        f"<start_of_turn>model\n"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,          # Greedy decoding cho reproducibility
            temperature=1.0,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id,
        )

    # Decode chỉ phần generated
    generated = outputs[0][inputs['input_ids'].shape[1]:]
    answer = tokenizer.decode(generated, skip_special_tokens=True).strip()

    # Cắt tại <end_of_turn> nếu có
    if "<end_of_turn>" in answer:
        answer = answer.split("<end_of_turn>")[0].strip()

    return answer

print("Inference functions ready!")