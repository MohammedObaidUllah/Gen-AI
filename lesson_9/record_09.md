# Day 9 – GenAI Learning Log

**Date:** 27-11-2026  
**Lesson:** Semantic Search

## Topics learned
- Bag of Words vs. text embeddings
- Sentence Transformers
- Dot product, cosine similarity and vector normalization
- Semantic search
- Top-K retrieval and similarity threshold filtering
- Input validation and exception handling
- Brute-force search and Approximate Nearest Neighbor (ANN) search

## What I understood
- The differences between Bag of Words and text embeddings.
- How to use Sentence Transformers locally to generate embeddings.
- Why cosine similarity removes the influence of vector magnitude when measuring directional similarity.
- How validation and exception handling serve different purposes.
- Why document embeddings should be precomputed and reused.
- Why combining top-K retrieval with a similarity threshold can return fewer than K results.

## What I struggled with
- Initially distinguishing the applications of Bag of Words and text embeddings.
- Recollecting Python lambda functions.
- Maintaining sentence-score associations while filtering.
- Articulating technical concepts concisely during interviews.

## Coding exercises completed
- [x] Generated sentence and query embeddings using `all-MiniLM-L6-v2`.
- [x] Implemented cosine similarity from scratch using NumPy.
- [x] Implemented ranking and top-K retrieval.
- [x] Added similarity threshold filtering.
- [x] Built a reusable `semantic_search()` function.
- [x] Implemented an interactive search loop with input validation and exception handling.
- [x] Successfully tested the search engine with relevant and unrelated queries.

**Project:** `lesson_9/semantic_search.py`

## Mock interview score
**8/10**

Good conceptual understanding; technical articulation needs improvement, particularly concise explanations and precise terminology.

## What I need to revise
- Applications of different text representations.
- Python lambda functions and sorting.
- Conditions that require regenerating document embeddings.
- ANN search and its speed-recall trade-off.

---

**Day 9 status:** Completed.

**Day 10 plan:** Vector databases, FAISS, vector indexing and efficient similarity search.
