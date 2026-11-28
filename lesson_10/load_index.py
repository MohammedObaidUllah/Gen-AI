import faiss
import numpy as np

loaded_index = faiss.read_index("lesson_10/ivf_index.faiss")

test_query = np.load("lesson_10/test_query.npy")

loaded_index.nprobe = 20

print("Trained:", loaded_index.is_trained)
print("Total vectors:", loaded_index.ntotal)
print("Clusters:", loaded_index.nlist)
print("Query shape:", test_query.shape)

scores, indices = loaded_index.search(test_query, k=10)

print("Loaded IDs:", indices)