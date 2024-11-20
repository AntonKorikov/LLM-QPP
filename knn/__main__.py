from abc import ABC, abstractmethod
from utils.setup_logging import setup_logging
import pickle
import json
import torch
import heapq
from .knn import ExactKNN
#todo: some tests 
if __name__ == "__main__":
    # Define query and document embeddings
    a = torch.tensor([2, 3, 4], dtype=torch.float32).to(dtype=torch.float32, device='cuda' if torch.cuda.is_available() else 'cpu')
    b = torch.tensor([3, 7, 1], dtype=torch.float32)
    c = torch.tensor([5, 3, 2], dtype=torch.float32)

    # Pickle document embeddings in batches
    corpus_path = "corpus.pkl"
    with open(corpus_path, 'wb') as f:
        for doc_id, embedding in zip(["d1", "d2"], [b, c]):
            pickle.dump({"doc_id": doc_id, "embedding": embedding}, f)


    # Define a configuration for ExactKNN
    config = {
        'logging': {'level' : 'DEBUG'}
    }

    # Initialize ExactKNN
    knn = ExactKNN(config, corpus_path)

    # Test cosine similarity
    result_cos = knn.get_top_k(a, 'cosine', 2, 'load_all')
    print("Cosine Similarity:", result_cos["sim_scores"])  # Expected: tensor([0.7494])

    # Test dot product similarity
    result_dot = knn.get_top_k(a, 'dot', 2, 'load_all')
    print("Dot Product Similarity:", result_dot["sim_scores"])  # Expected: tensor([[31.]])

    # Test Euclidean distance similarity
    result_euc = knn.get_top_k(a, 'euclidean', 2, 'load_all')
    print("Euclidean Distance Similarity:", result_euc["sim_scores"])  # Expected: -5.099019527435303