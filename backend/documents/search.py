import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def semantic_search(
    query_embedding: np.ndarray, document_embeddings: list[np.ndarray]
) -> float:
    """
    Perform semantic search by calculating cosine similarity between the query embedding
    and a list of document embeddings.

    Args:
        query_embedding (np.ndarray): The embedding vector for the search query.
        document_embeddings (List[np.ndarray]): A list of embedding vectors for documents.

    Returns:
        float: The maximum cosine similarity score between the query embedding and document embeddings.
    """
    if not document_embeddings:
        return 0.0

    # Convert list of embeddings to a 2D numpy array
    doc_emb_matrix = np.array(document_embeddings)

    # Reshape query embedding for compatibility
    query_emb_reshaped = query_embedding.reshape(1, -1)

    # Calculate cosine similarities
    similarities = cosine_similarity(query_emb_reshaped, doc_emb_matrix)

    return float(similarities.max())
