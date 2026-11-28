from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love riding bikes",
    "I love driving cars",
    "I prefer bikes over cars"
]

embeddings = model.encode(sentences)
faiss.normalize_L2(embeddings)

print(embeddings.shape)

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)
print("Total vectors:", index.ntotal)

def semantic_search(query, k=2, threshold=0.3):
    query_embeddings = model.encode([query])
    faiss.normalize_L2(query_embeddings)
    k = min(k, index.ntotal)  

    scores, indices = index.search(query_embeddings, k=k)

    similarity_score = []
    for score, idx in zip(scores[0], indices[0]):
        if score >= threshold:
            similarity_score.append((idx, sentences[idx], score))

    return similarity_score


while True:
    query = input("Enter a query: ")

    if query.strip().lower() == "exit":
        break

    while True:
        try:
            k = int(input("Enter k value: "))
            if k <= 0:
                print("K should be positive")
            else:  
                break
        except ValueError as e:
            print("Enter a valid k value")
            print("Error:", e)
    while True:
        try:
            threshold = float(input("Enter threshold value between 0 and 1: "))
            if not (0 <= threshold <= 1):
                print("threshold should be positive and between 0 and 1")
            else:
                break
        except ValueError as e:
            print("Enter a valid threshold value")
            print("Error:", e)

    print(semantic_search(query, k, threshold))