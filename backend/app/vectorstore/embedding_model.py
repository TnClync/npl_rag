import numpy as np
from sentence_transformers import SentenceTransformer

from config.settings import EMBEDDING_MODEL    


EMBED_MODEL_NAME = EMBEDDING_MODEL

class EmbeddingModel:
    def __init__(self, model_name: str = EMBED_MODEL_NAME):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.dim = self.model.get_embedding_dimension()
        print(f"Embedding model loaded! Dimension: {self.dim}")

    def encode(self, texts):
        """
        texts: str or List[str]
        return: np.array
        """
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return np.array(embeddings)

    def get_dim(self):
        return self.dim


# ============================================================
# Singleton (quan trọng: load 1 lần duy nhất)
# ============================================================

embedding_model = EmbeddingModel().model