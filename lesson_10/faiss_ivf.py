# ivf: inverted file index

import numpy as np
import faiss
import time
import pandas as pd

dimension = 384
num_vectors = 10000
nlist = 100
nprobe_values = [1, 5, 10, 20, 50, 100]
results = []

rng = np.random.default_rng(42)

embeddings = rng.random(
    (num_vectors, dimension)
).astype(np.float32)

faiss.normalize_L2(embeddings)

print(embeddings.shape)

exact_index = faiss.IndexFlatIP(embeddings.shape[1])
exact_index.add(embeddings)

print("Total: ", exact_index.ntotal)

quantizer = faiss.IndexFlatIP(dimension)

ivf_index = faiss.IndexIVFFlat(
    quantizer,
    dimension,
    nlist,
    faiss.METRIC_INNER_PRODUCT
)

print("Before training:", ivf_index.is_trained)

ivf_index.train(embeddings)

print("After training:", ivf_index.is_trained)
print("Quantizer vectors:", quantizer.ntotal)
print("IVF vectors:", ivf_index.ntotal)

ivf_index.add(embeddings)


print("IVF vectors:", ivf_index.ntotal)
print("Clusters:", ivf_index.nlist)
# print("Clusters searched:", ivf_index.nprobe)


def recall_at_k(exact_ids, approx_ids):
    exact_set = set(exact_ids)
    approx_set = set(approx_ids)

    common_ids = exact_set.intersection(approx_set)

    recall = len(common_ids) / len(exact_set)
    return recall

def benchmark_search(index, queries, k=10, repeats=5):
    index.search(queries, k=k)
    times = []

    for _ in range(repeats):
        start_time = time.perf_counter()
        scores, indices = index.search(queries, k=k)
        end_time = time.perf_counter()

        total_time = (end_time - start_time) * 1000
        times.append(total_time)

    median_time = np.median(times)

    return scores, indices, median_time

num_queries = 100

queries = rng.random(
    (num_queries, dimension)
).astype(np.float32)

faiss.normalize_L2(queries)

print(queries.shape)

exact_scores, exact_indices, exact_total_time = benchmark_search(exact_index, queries)
exact_avg_time = exact_total_time / num_queries

print(f"Exact total time: {exact_total_time:.4f} ms")
print(f"Exact average time: {exact_avg_time:.4f} ms")   



for probe in nprobe_values:
    ivf_index.nprobe = probe

    data = {}  

    approx_scores, approx_ids, approx_total_time = benchmark_search(ivf_index, queries)
    
    approx_avg_time = approx_total_time / num_queries

    speedup = exact_total_time / approx_total_time

    recall_values = []
    for ex_idx, ap_idx in zip(exact_indices, approx_ids):
        value = recall_at_k(ex_idx, ap_idx)
        recall_values.append(value)

    avg_recall = np.mean(recall_values)

    data["nprobe"] = probe
    data["total_time"] = approx_total_time
    data["avg_time"] = approx_avg_time
    data["speedup"] = speedup
    data["avg_recall"] = avg_recall

    results.append(data)

df = pd.DataFrame(results)

print(df.to_string(index=False))

ivf_index.nprobe = 20

test_query = queries[0:1]

scores, indices = ivf_index.search(test_query, k=10)

print("Original IDs:", indices)

faiss.write_index(ivf_index, "lesson_10/ivf_index.faiss")

np.save("lesson_10/test_query.npy", test_query)

print("Index saved successfully!")