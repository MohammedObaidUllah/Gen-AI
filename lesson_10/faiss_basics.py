# faiss: facebook ai semantic search

import faiss
import numpy as np

vectors = np.array([
    [1,2],
    [4,6],
    [1,2],  
    [3,4]
], dtype=np.float32)


dimension = 2

index = faiss.IndexFlatL2(dimension)

index.add(vectors)

print("Total vectors:", index.ntotal)

query = np.array([[1, 2]], dtype = np.float32)

distances, indices = index.search(query, k=3)

print("Distances:", distances)
print("Indices:", indices)