import faiss
import numpy as np

vectors = np.array([
    [1,2],
    [4,6],
    [1,2],  
    [3,4]
], dtype=np.float32)

faiss.normalize_L2(vectors)

dimension = 2

index = faiss.IndexFlatIP(dimension)
index.add(vectors)
print("Total vectors:", index.ntotal)

query = np.array([[1, 2]], dtype = np.float32)
faiss.normalize_L2(query)

scores, indices = index.search(query, k=3)
print("Scores:", scores)
print("Indices:", indices)

