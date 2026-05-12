import numpy as np

class TrafficLawRetriever:
    def __init__(self, index, chunks, embedder, top_k=5):
        self.index = index
        self.chunks = chunks
        self.embedder = embedder
        self.top_k = top_k

    def retrieve(self, query: str, top_k: int = None) -> list[dict]:
        k = top_k or self.top_k

        # Embed query
        q_emb = self.embedder.encode(
            [query],
            normalize_embeddings=True,
            convert_to_numpy=True,
        ).astype(np.float32)

        print("===== DEBUG FAISS =====")
        print("Index dim:", self.index.d)
        print("Query shape:", q_emb.shape)
        print("=======================")

        # Search
        scores, indices = self.index.search(q_emb, k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx != -1:
                chunk = self.chunks[idx].copy()
                chunk['retrieval_score'] = float(score)
                results.append(chunk)

        return results

    def format_context(self, results: list[dict], max_chunks: int = 3) -> str:
        """Format retrieved chunks thành context string cho LLM"""
        context_parts = []
        for i, chunk in enumerate(results[:max_chunks]):
            context_parts.append(
                f"[{i+1}] {chunk['title']}\n"
                f"{chunk['text'][:800]}"  # Giới hạn mỗi chunk 800 chars
            )
        return "\n\n".join(context_parts)
