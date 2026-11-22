from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load a pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love programming",
    "I enjoy coding",
    "I like eating pizza"
]

# Generate embeddings
embeddings = model.encode(sentences)

# Compare the sentence vectors
similarity_matrix = cosine_similarity(embeddings)


for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("Vector Dimensions:", len(embedding))
    print("First 5 values:", embedding[:5])

print("\nSimilarity Matrix:")
print(similarity_matrix)

# Compare specific sentence pairs
print("\nProgramming vs Coding:")
print(similarity_matrix[0][1])

print("\nProgramming vs Pizza:")
print(similarity_matrix[0][2])
