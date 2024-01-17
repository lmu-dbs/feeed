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
        "entropy_k_block_ratio_1": entropy_k_block_ratio(log, k=1),
        "entropy_k_block_ratio_3": entropy_k_block_ratio(log, k=3),
        "entropy_k_block_ratio_5": entropy_k_block_ratio(log, k=5),
        "entropy_k_block_diff_1": entropy_k_block_diff(log, k=1),
        "entropy_k_block_diff_3": entropy_k_block_diff(log, k=3),
        "entropy_k_block_diff_5": entropy_k_block_diff(log, k=5),
        "entropy_knn_flattened_3": entropy_flattened_knn(log, k=3),
        "entropy_knn_flattened_5": entropy_flattened_knn(log, k=5),
        "entropy_knn_flattened_7": entropy_flattened_knn(log, k=7),
    }
    return results

def trace_entropies(log):
    # Get unique traces and their counts
    trace_counts = Counter(tuple(event["concept:name"] for event in trace) for trace in log)
    
    # Calculate trace entropy
    trace_entropy = sum((count / len(log)) * math.log2(count / len(log)) for count in trace_counts.values())
    
    return -trace_entropy  # Use negative sign to follow the convention of minimizing entropy


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

    return -prefix_entropy

def prefix_flattened_entropy(log):
    unique_traces = variants_filter.get_variants(log)

    # Generate all possible prefixes
    all_possible_prefixes = [tuple(trace[:i+1]) for trace in unique_traces for i in range(len(trace))]

    # Use Counter to count occurrences of each unique prefix
    prefix_counts = Counter(all_possible_prefixes)

    # Calculate prefix entropy
    total_prefixes = len(all_possible_prefixes)
    prefix_entropy = sum((count / total_prefixes) * math.log2(count / total_prefixes) for count in prefix_counts.values())

    return -prefix_entropy

def global_block_entropy(log):
    all_traces = [tuple(event["concept:name"] for event in trace) for trace in log]
    
    # Generate all possible substrings for all traces
    all_substrings = [sub for trace in all_traces for sub in (tuple(trace[i:j]) for i in range(len(trace)) for j in range(i + 1, len(trace) + 1))]
    
    substring_counts = Counter(all_substrings)
    total_substrings = len(all_substrings)
    
    # Calculate entropy
    substring_entropy = sum((count / total_substrings) * math.log2(count / total_substrings) for count in substring_counts.values())
    
    return -substring_entropy

def flattened_global_block_entropy(log):
    all_traces = variants_filter.get_variants(log)
    
    # Generate all possible substrings for all traces
    all_substrings = [sub for trace in all_traces for sub in (tuple(trace[i:j]) for i in range(len(trace)) for j in range(i + 1, len(trace) + 1))]
    
    substring_counts = Counter(all_substrings)
    total_substrings = len(all_substrings)
    
    # Calculate entropy
    substring_entropy = sum((count / total_substrings) * math.log2(count / total_substrings) for count in substring_counts.values())
    
    return -substring_entropy

def entropy_k_block(log, k=1):
    all_k_object_substrings = [trace[i:i + k] for trace in (tuple(event["concept:name"] for event in trace) for trace in log) for i in range(len(trace) - k + 1)]
    
    k_sub_counts = Counter(all_k_object_substrings)
    total_k_substrings = len(all_k_object_substrings)

    k_substring_entropy = sum((count / total_k_substrings) * math.log2(count / total_k_substrings) for count in k_sub_counts.values()) 
    return -k_substring_entropy

def entropy_k_block_ratio(log, k):
    return entropy_k_block(log, k)/k

def entropy_k_block_diff(log, k):
    return entropy_k_block(log, k) - entropy_k_block(log, k-1)

# Calculating knn entropies
def entropy_flattened_knn(log, k=1):
    unique_traces = variants_filter.get_variants(log)
    local_neighbour_list = find_nearest_neighbor(unique_traces, k)
    n= len(unique_traces)
    
    knn_entropy = 0
    
    for neighbour in local_neighbour_list:
        item, d, max_len, normalized_lev = neighbour
        part_2 = math.log(normalized_lev)
        part_3 = math.log(math.pow(math.pi, 1/ 2.0) / math.gamma(1.0 / 2.0 + 1.0))
        part_4 = 0.5772
        part_5 = harmonic_sum(k-1)
        part_6 = math.log(n)
        local_sum = 1/n * (part_2 + part_3 + part_4 - part_5 + part_6)
        knn_entropy += local_sum
        
    return knn_entropy

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
    
def find_nearest_neighbor(trace_list, k =1):
    neighbour_list = []
    for other_trace in trace_list:
        list1 = [(trace, distance(other_trace,trace), max(len(other_trace),len(trace)), distance(other_trace,trace)/max(len(other_trace),len(trace)))for trace in trace_list]
        list2 = sorted(list1,key=lambda x: x[3])
        filtered_list = list(filter(lambda x: x[3] != 0, list2))
        neighbour_list.append(filtered_list[k-1])
    return neighbour_list