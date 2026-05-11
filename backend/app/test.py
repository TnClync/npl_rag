from vectorstore.embedding_model import embedding_model

texts = [
    "Tôi vượt đèn đỏ bị phạt bao nhiêu?",
    "Luật giao thông đường bộ Việt Nam",
    "Học máy và trí tuệ nhân tạo"
]

embeddings = embedding_model.encode(texts)

print("Shape:", embeddings.shape)
print("\nVector sample:")
print(embeddings[0][:10])
