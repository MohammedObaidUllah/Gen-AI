from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love riding bikes",
    "I love driving cars",
    "I prefer bikes over cars"
]

embeddings = model.encode(sentences)

print(embeddings.shape)

# query = "best bike for city travel"

# query_embed = model.encode(query)

# print(query_embed.shape)


def cosine_similarity(A, B):
    dot_prod = np.dot(A, B)
    norml_len = np.linalg.norm(A) * np.linalg.norm(B)

    return (dot_prod / norml_len)

# cosine_score = []

# for embedding in embeddings:
#     cosine = cosine_similarity(embedding, query_embed)
#     cosine_score.append(cosine)
#     print(cosine)

# similarity_score = []

# for sentence, score in zip(sentences, cosine_score):
#     similarity_score.append((sentence, score))


# similarity_score.sort(key=lambda x: x[1], reverse = True)
# print(similarity_score)

# print(similarity_score[:2])


def semantic_search(query, k=2, threshold=0.3):
    sentence_embeddings = embeddings
    query_embeddings = model.encode(query)

    cosine_score = []
    for embedding in sentence_embeddings:
        cosine = cosine_similarity(embedding, query_embeddings)
        cosine_score.append(cosine)

    similarity_score = []
    for sentence, score in zip(sentences, cosine_score):
        if score >= threshold:
            similarity_score.append((sentence, score))

    similarity_score.sort(key=lambda x: x[1], reverse= True)

    return similarity_score[:k]

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
