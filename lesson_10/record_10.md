# Daily Learning Log — 28-11-2026

**Lesson 10 — FAISS, IVF, Search Evaluation and Index Persistence**

## 1. Topics learned

- FAISS (Facebook AI Similarity Search).
- Cosine similarity using FAISS.
- L2 normalization and inner product.
- Exact search using `IndexFlatIP`.
- Approximate search using `IndexIVFFlat`.
- Quantizer, centroids, `nlist` and `nprobe`.
- Recall\@K, search latency and speedup.
- Warm-up searches and median-based benchmarking.
- Handling two-dimensional NumPy arrays.
- Python `zip()`, indexing and slicing.
- Index persistence using `faiss.write_index()` and `faiss.read_index()`.
- Incrementally adding embeddings to an existing trained index.

## 2. What I understood

- How to perform vector similarity search using FAISS instead of manually calculating cosine similarity.
- The difference between exact and approximate search.
- `nlist` determines the number of clusters, whereas `nprobe` determines how many clusters are searched per query.
- The trade-off between search speed and recall.
- When and why to use the `zip()` function.
- How to handle two-dimensional NumPy arrays and interpret their shapes.
- The input and output structures at different stages of the program.
- How indexing removes a dimension while slicing preserves it.
- Why warm-up searches and median-based measurements improve benchmarking reliability.
- How to persist and reload a trained FAISS index.
- Why a restored index does not require retraining or re-adding existing embeddings.
- How new embeddings can be assigned to existing clusters without mandatory retraining.
- Why changing `nlist` requires rebuilding the index.

## 3. What I struggled with

- Understanding the purpose of `METRIC_INNER_PRODUCT`.
- Differentiating between quantizer centroids and stored IVF vectors.
- Understanding NumPy array dimensions.
- Initially identifying when retraining an IVF index is necessary.
- Explaining technical concepts concisely and confidently.

## 4. Coding exercises completed

- [x] Generated 10,000 synthetic embeddings with 384 dimensions.
- [x] Implemented exact vector search.
- [x] Implemented approximate IVF search.
- [x] Evaluated six different `nprobe` configurations.
- [x] Implemented Recall\@K.
- [x] Developed a reusable benchmarking function.
- [x] Calculated average recall, latency and speedup.
- [x] Presented experimental results using Pandas.
- [x] Saved the trained IVF index to disk.
- [x] Loaded the saved index in a separate Python program.
- [x] Verified that the original and restored indexes returned identical IDs for the test query.

## 5. Experimental results

| nprobe | Avg. time (ms) | Speedup | Recall\@10 |
| -----: | -------------: | ------: | ---------: |
|      1 |         0.0214 |  27.45x |       4.9% |
|      5 |         0.0745 |   7.89x |      22.0% |
|     10 |         0.1295 |   4.54x |      36.2% |
|     20 |         0.2691 |   2.18x |      60.7% |
|     50 |         0.5595 |   1.05x |      94.6% |
|    100 |         0.7454 |   0.79x |       100% |

Exact search average time: 0.5876 ms.

**Observation:** Increasing `nprobe` improves recall but generally increases search latency. Approximate search does not necessarily outperform exact search at high recall, particularly with smaller datasets.

## 6. Index persistence verification

| Parameter  | Before saving | After loading |
| ---------- | ------------: | ------------: |
| is_trained |          True |          True |
| ntotal     |         10000 |         10000 |
| nlist      |           100 |           100 |
| nprobe     |            20 |            20 |

- All 10 retrieved IDs matched in the same order.
- No retraining was performed.
- No existing embeddings were re-added.
- Index persistence was successfully implemented and verified for the test query.

## 7. Performance

- Benchmarking coding exercise: 10/10 (previous lesson assessment).
- Array structure assessment 1: 4/6.
- Array structure assessment 2: 4/4.
- Index persistence implementation: Successfully completed.
- Technical communication: Independently explained the complete project.
- Formal mock interview score: Not conducted today.

## 8. What I need to revise

- Inner product and its relationship with cosine similarity.
- L2 normalization.
- Quantizer and cluster centroids.
- NumPy array shapes and dimensionality.
- FAISS function input and output structures.
- Incremental indexing and when changes in data distribution may justify rebuilding and retraining.
- Technical communication skills.

## 9. Pending practical work

- Implement incremental addition of new embeddings to a saved index.
- Perform semantic search using real text embeddings instead of synthetic random vectors.
- Associate vector IDs with original text and document metadata.

## 10. Key achievement of the day

I independently implemented, benchmarked, explained, saved and restored a FAISS IVF index. I understood the complete vector search pipeline, its data structures, evaluation metrics and persistence mechanism.

**Lesson 10 status: Completed.**
