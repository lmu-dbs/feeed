import json
import numpy as np
from feeed.feature_extractor import extract_features

# Extract features as a dictionary
features = extract_features("test_logs/Sepsis.xes")

# def default_handler(obj):
#     if hasattr(obj, '__dict__'):
#         return obj.__dict__
#     elif isinstance(obj, np.integer):
#         return int(obj)
#     else:
#         raise TypeError('Object of type %s is not JSON serializable' % type(obj))

# # Write the dictionary to a JSON file
# with open("output.json", "w") as json_file:
#     json.dump(features, json_file, default=default_handler)


expected_output = {"log": "Sepsis", "n_traces": 1050, "n_unique_traces": 846, "ratio_unique_traces_per_trace": 0.8057142857142857, "trace_len_coefficient_variation": 0.7916391922924689, "trace_len_entropy": 6.769403523350811, "trace_len_geometric_mean": 12.281860759040903, "trace_len_geometric_std": 1.7464004837799154, "trace_len_harmonic_mean": 10.47731701485374, "trace_len_hist1": 0.048613291470434326, "trace_len_hist10": 0.00010465724751439027, "trace_len_hist2": 0.005285190999476714, "trace_len_hist3": 0.0005756148613291472, "trace_len_hist4": 0.0002093144950287807, "trace_len_hist5": 0.00010465724751439036, "trace_len_hist6": 0.0, "trace_len_hist7": 5.232862375719522e-05, "trace_len_hist8": 0.0, "trace_len_hist9": 0.0, "trace_len_iqr": 7.0, "trace_len_kurtosis": 87.0376906898399, "trace_len_kurtosis_hist": 4.931206347805768, "trace_len_max": 185, "trace_len_mean": 14.48952380952381, "trace_len_median": 13.0, "trace_len_min": 3, "trace_len_mode": 8, "trace_len_q1": 9.0, "trace_len_q3": 16.0, "trace_len_skewness": 7.250526815880918, "trace_len_skewness_hist": 2.6128507781562513, "trace_len_std": 11.470474925273926, "trace_len_variance": 131.57179501133788, "kurtosis_variant_occurrence": 217.44268017168216, "mean_variant_occurrence": 1.2411347517730495, "ratio_most_common_variant": 0.03333333333333333, "ratio_top_10_variants": 0.2742857142857143, "ratio_top_1_variants": 0.12, "ratio_top_20_variants": 0.35523809523809524, "ratio_top_50_variants": 0.5971428571428572, "ratio_top_5_variants": 0.21523809523809523, "ratio_top_75_variants": 0.7980952380952381, "skewness_variant_occurrence": 13.637101374069475, "std_variant_occurrence": 1.7594085182491936, "activities_iqr": 983.5, "activities_kurtosis": 1.05777753209275, "activities_max": 3383, "activities_mean": 950.875, "activities_median": 788.0, "activities_min": 6, "activities_q1": 101.75, "activities_q3": 1085.25, "activities_skewness": 1.3912385607018212, "activities_std": 1008.5815457239935, "activities_variance": 1017236.734375, "n_unique_activities": 16, "n_unique_start_activities": 6, "start_activities_iqr": 9.25, "start_activities_kurtosis": 1.199106773708694, "start_activities_max": 995, "start_activities_mean": 175.0, "start_activities_median": 12.0, "start_activities_min": 6, "start_activities_q1": 7.75, "start_activities_q3": 17.0, "start_activities_skewness": 1.7883562472303318, "start_activities_std": 366.73787187399483, "start_activities_variance": 134496.66666666666, "end_activities_iqr": 39.5, "end_activities_kurtosis": 2.5007579343413617, "end_activities_max": 393, "end_activities_mean": 75.0, "end_activities_median": 32.5, "end_activities_min": 2, "end_activities_q1": 14.0, "end_activities_q3": 53.5, "end_activities_skewness": 2.004413358907822, "end_activities_std": 112.91400014423114, "end_activities_variance": 12749.57142857143, "n_unique_end_activities": 14, "eventropy_global_block": 14.501, "eventropy_global_block_flattened": 14.655, "eventropy_k_block_diff_1": 3.238, "eventropy_k_block_diff_3": 1.712, "eventropy_k_block_diff_5": 1.104, "eventropy_k_block_ratio_1": 3.238, "eventropy_k_block_ratio_3": 2.262, "eventropy_k_block_ratio_5": 1.871, "eventropy_knn_3": 4.956, "eventropy_knn_5": 4.49, "eventropy_knn_7": 4.191, "eventropy_lempel_ziv": 1.727, "eventropy_lempel_ziv_flattened": 1.888, "eventropy_prefix": 10.227, "eventropy_prefix_flattened": 10.595, "eventropy_trace": 9.334, "epa_variant_entropy": 40624.49329803771, "epa_normalized_variant_entropy": 0.6957588422064969, "epa_sequence_entropy": 76528.6794749776, "epa_normalized_sequence_entropy": 0.5223430410751398, "epa_sequence_entropy_linear_forgetting": 32139.284589305265, "epa_normalized_sequence_entropy_linear_forgetting": 0.21936523360299368, "epa_sequence_entropy_exponential_forgetting": 43880.53919110408, "epa_normalized_sequence_entropy_exponential_forgetting": 0.29950463593968696, "accumulated_time_min": 0.0, "accumulated_time_max": 36488789.0, "accumulated_time_mean": 396893.5456158801, "accumulated_time_median": 11924.0, "accumulated_time_mode": 0.0, "accumulated_time_std": 1603193.2693230484, "accumulated_time_variance": 2570228658802.724, "accumulated_time_q1": 1138.5, "accumulated_time_q3": 273793.5, "accumulated_time_iqr": 272655.0, "accumulated_time_geometric_mean": 10904.332835327954, "accumulated_time_geometric_std": 44.90292804116573, "accumulated_time_harmonic_mean": 0.0, "accumulated_time_skewness": 11.401470845961647, "accumulated_time_kurtosis": 172.5725804780399, "accumulated_time_coefficient_variation": 4.039353340541942, "accumulated_time_entropy": 7.7513093893416505, "accumulated_time_skewness_hist": 2.6663623098416838, "accumulated_time_kurtosis_hist": 5.1101603988544575, "execution_time_min": 0.0, "execution_time_max": 36051318.0, "execution_time_mean": 169759.47397134217, "execution_time_median": 188.0, "execution_time_mode": 0.0, "execution_time_std": 1442884.0333930077, "execution_time_variance": 2081914333820.474, "execution_time_q1": 0.0, "execution_time_q3": 18623.25, "execution_time_iqr": 18623.25, "execution_time_geometric_mean": 199.88320191111325, "execution_time_geometric_std": 127.92792986844444, "execution_time_harmonic_mean": 0.0, "execution_time_skewness": 14.528527518337812, "execution_time_kurtosis": 250.488253204707, "execution_time_coefficient_variation": 8.499578843161146, "execution_time_entropy": 6.221052534222753, "execution_time_skewness_hist": 2.666603580180752, "execution_time_kurtosis_hist": 5.110914600502133, "remaining_time_min": 0.0, "remaining_time_max": 36488789.0, "remaining_time_mean": 2796232.825161036, "remaining_time_median": 619470.0, "remaining_time_mode": 0.0, "remaining_time_std": 5281078.119895141, "remaining_time_variance": 27889786108435.19, "remaining_time_q1": 202862.5, "remaining_time_q3": 2487420.0, "remaining_time_iqr": 2284557.5, "remaining_time_geometric_mean": 224736.22203397762, "remaining_time_geometric_std": 70.1715364379747, "remaining_time_harmonic_mean": 0.0, "remaining_time_skewness": 3.1659682263680318, "remaining_time_kurtosis": 11.666720436340661, "remaining_time_coefficient_variation": 1.8886403422401359, "remaining_time_entropy": 8.55331137332654, "remaining_time_skewness_hist": 2.61693528788402, "remaining_time_kurtosis_hist": 4.950830339077765, "within_day_min": 0.0, "within_day_max": 86390.0, "within_day_mean": 41330.543183909555, "within_day_median": 37800.0, "within_day_mode": 21600.0, "within_day_std": 20590.894075207732, "within_day_variance": 423984918.8164249, "within_day_q1": 23113.75, "within_day_q3": 57600.0, "within_day_iqr": 34486.25, "within_day_geometric_mean": 35069.233548115764, "within_day_geometric_std": 1.9726454507370417, "within_day_harmonic_mean": 0.0, "within_day_skewness": 0.3603519661740256, "within_day_kurtosis": -0.9142275965359778, "within_day_coefficient_variation": 0.49820042247168106, "within_day_entropy": 9.501009299480838, "within_day_skewness_hist": 1.7511033515349685, "within_day_kurtosis_hist": 2.6115894228132266}

if features == expected_output:
    print("JSON files are identical")
else:
    print("JSON files differ")
    exit(1)