from pm4py.algo.filtering.log.variants import variants_filter
from collections import Counter
import math
from Levenshtein import distance 

def internal_entropies(log):
    results = {
        "entropy_trace": trace_entropies(log),
        "entropy_prefix": prefix_entropy(log),
        "entropy_prefix_flattened_": prefix_flattened_entropy(log),
        "entropy_global_block": global_block_entropy(log),
        "entropy_global_block_flattened": flattened_global_block_entropy(log),
        "entropy_lempel_ziv": entropy_lempel_zev(log),
        "entropy_lempel_ziv_flattened": entropy_lempel_zev_flattened(log),
        "entropy_k_block_diff_1": entropy_k_block_diff(log, k=1),
        "entropy_k_block_diff_3": entropy_k_block_diff(log, k=3),
        "entropy_k_block_diff_5": entropy_k_block_diff(log, k=5),
        "entropy_k_block_ratio_1": entropy_k_block_ratio(log, k=1),
        "entropy_k_block_ratio_3": entropy_k_block_ratio(log, k=3),
        "entropy_k_block_ratio_5": entropy_k_block_ratio(log, k=5),
        "entropy_knn_3": entropy_flattened_knn(log, k=3),
        "entropy_knn_5": entropy_flattened_knn(log, k=5),
        "entropy_knn_7": entropy_flattened_knn(log, k=7),
    }
    return results

def trace_entropies(log):
    # Get unique traces and their counts
    trace_counts = Counter(tuple(event["concept:name"] for event in trace) for trace in log)
    
    # Calculate trace entropy
    trace_entropy = sum((count / len(log)) * math.log2(count / len(log)) for count in trace_counts.values())
    
    return round(-trace_entropy,3)  # Use negative sign to follow the convention of minimizing entropy


def prefix_entropy(log):
    # Get unique traces
    unique_traces = [tuple(event["concept:name"] for event in trace) for trace in log]

    # Generate all possible prefixes
    all_possible_prefixes = [tuple(trace[:i+1]) for trace in unique_traces for i in range(len(trace))]

    # Use Counter to count occurrences of each unique prefix
    prefix_counts = Counter(all_possible_prefixes)

    # Calculate prefix entropy
    total_prefixes = len(all_possible_prefixes)
    prefix_entropy = sum((count / total_prefixes) * math.log2(count / total_prefixes) for count in prefix_counts.values())

    return round(-prefix_entropy,3)

def prefix_flattened_entropy(log):
    unique_traces = variants_filter.get_variants(log)

    # Generate all possible prefixes
    all_possible_prefixes = [tuple(trace[:i+1]) for trace in unique_traces for i in range(len(trace))]

    # Use Counter to count occurrences of each unique prefix
    prefix_counts = Counter(all_possible_prefixes)

    # Calculate prefix entropy
    total_prefixes = len(all_possible_prefixes)
    prefix_entropy = sum((count / total_prefixes) * math.log2(count / total_prefixes) for count in prefix_counts.values())

    return round(-prefix_entropy,3)

def global_block_entropy(log):
    all_traces = [tuple(event["concept:name"] for event in trace) for trace in log]
    
    # Generate all possible substrings for all traces
    all_substrings = [sub for trace in all_traces for sub in (tuple(trace[i:j]) for i in range(len(trace)) for j in range(i + 1, len(trace) + 1))]
    
    substring_counts = Counter(all_substrings)
    total_substrings = len(all_substrings)
    
    # Calculate entropy
    substring_entropy = sum((count / total_substrings) * math.log2(count / total_substrings) for count in substring_counts.values())
    
    return round(-substring_entropy,3)

def flattened_global_block_entropy(log):
    all_traces = variants_filter.get_variants(log)
    
    # Generate all possible substrings for all traces
    all_substrings = [sub for trace in all_traces for sub in (tuple(trace[i:j]) for i in range(len(trace)) for j in range(i + 1, len(trace) + 1))]
    
    substring_counts = Counter(all_substrings)
    total_substrings = len(all_substrings)
    
    # Calculate entropy
    substring_entropy = sum((count / total_substrings) * math.log2(count / total_substrings) for count in substring_counts.values())
    
    return round(-substring_entropy,3)

def entropy_k_block(log, k=1):
    all_k_object_substrings = [trace[i:i + k] for trace in (tuple(event["concept:name"] for event in trace) for trace in log) for i in range(len(trace) - k + 1)]
    
    k_sub_counts = Counter(all_k_object_substrings)
    total_k_substrings = len(all_k_object_substrings)

    k_substring_entropy = sum((count / total_k_substrings) * math.log2(count / total_k_substrings) for count in k_sub_counts.values()) 
    return round(-k_substring_entropy,3)

def entropy_k_block_ratio(log, k):
    return entropy_k_block(log, k)/k

def entropy_k_block_diff(log, k):
    return entropy_k_block(log, k) - entropy_k_block(log, k-1)

def entropy_lempel_zev(log):
    unique_traces = [tuple(event["concept:name"] for event in trace) for trace in log]
    N, N_w, words = 0, 0, set()

    for trace in unique_traces:
        word = ""
        for activity in trace:
            word += activity
            if word not in words:
                words.add(word)
                word = ""

        N += len(trace)

    N_w = len(words)
    
    lempel_zev_entropy = N_w * math.log2(N) / N
    return round(lempel_zev_entropy,3)

def entropy_lempel_zev_flattened(log):
    unique_traces = list(variants_filter.get_variants(log))
    N, N_w, words = 0, 0, set()

    for trace in unique_traces:
        word = ""
        for activity in trace:
            word += activity
            if word not in words:
                words.add(word)
                word = ""

        N += len(trace)

    N_w = len(words)
    
    lempel_zev_entropy = N_w * math.log2(N) / N
    return round(lempel_zev_entropy,3)

# Calculating knn entropies
def entropy_flattened_knn(log, k=1):
    unique_traces = variants_filter.get_variants(log)
    unique_traces = list(unique_traces)
    local_neighbour_list = find_nearest_neighbors(unique_traces, k)
    n= len(unique_traces)
    
    knn_entropy = 0
    for neighbour in local_neighbour_list:
        normalized_lev = neighbour
        part_2 = math.log(normalized_lev)
        part_3 = math.log(math.pow(math.pi, 1/ 2.0) / math.gamma(1.0 / 2.0 + 1.0))
        part_4 = 0.5772
        part_5 = harmonic_sum(k-1)
        part_6 = math.log(n)
        local_sum = 1/n * (part_2 + part_3 + part_4 - part_5 + part_6)
        knn_entropy += local_sum
    return round(knn_entropy,3)

# some helper functions for calculating knn entropy

def harmonic_sum(j):
    if j < 0:
        return None
    elif j == 0:
        return 0.0
    else:
        L_j = 0.0
        for i in range(1, j + 1):
            L_j += 1.0 / float(i)
        return L_j
    
def calculate_distance_matrix(trace_list):
    n = len(trace_list)
    distance_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(trace_list[i], trace_list[j])
            distance_matrix[i][j] = dist
            distance_matrix[j][i] = dist

    return distance_matrix

def find_nearest_neighbors(trace_list, k=1):
    n = len(trace_list)
    distance_matrix = calculate_distance_matrix(trace_list)

    def calculate_normalized_distance(i, j):
        return distance_matrix[i][j] / max(len(trace_list[i]), len(trace_list[j]))

    neighbour_list = []

    for i in range(n):
        distances = [(calculate_normalized_distance(i, j))
                     for j in range(n) if i != j]
        distances.sort(key=lambda x: x)

        filtered_distances = [d for d in distances if d != 0]
        neighbour_list.append(filtered_distances[k-1])

    return neighbour_list
