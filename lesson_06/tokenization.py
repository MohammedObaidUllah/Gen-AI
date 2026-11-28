import tiktoken

text = "I love AI. I love programming. I love learning."

# Load a tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

# Convert text into token Ids
tokens = encoding.encode(text)

print("Token Ids:", tokens)
print("No. of tokens:", len(tokens))

# Convert each token ID back into its text representation
for token_id in tokens:
    print(token_id, "->", encoding.decode([token_id]))

# Convert token IDs back into text
decoded_text = encoding.decode(tokens)

print("Decoded text:", decoded_text)