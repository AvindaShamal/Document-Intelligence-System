from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_text_embeddings(text: str | list[str]) -> np.ndarray:
    """
    Generates a text embedding using a pre-trained SentenceTransformer model.

    Args:
        text (str | list[str]): The input text or list of texts to be embedded.

    Returns:
        np.ndarray: The text embedding as a numpy array."""

    embeddings = model.encode(text)
    return embeddings
