# FEEED
**Fe**ature **E**xtraction for **E**vent **D**ata

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation
### Requirements
- Python > 3.9
- [Java](https://www.java.com/en/download/)

### Clone

Clone this repo to your local machine using

```shell
git clone git@github.com:lmu-dbs/feeed.git
```

To directly use meta feature extraction methods via `import`
```shell
cd feeed
pip install -e .
```
Run:
```shell
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_logs/100_4_0.1_0.1_0.1_0.35_0.35_0.xes'))"
```

## Usage

### Feature types
Specific features can be selected refering their feature types:

| Feature Type     | Features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| simple_stats     | n_traces, n_unique_traces, ratio_unique_traces_per_trace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| trace_length     | trace_len_min, trace_len_max, trace_len_mean, trace_len_median, trace_len_mode, trace_len_std, trace_len_variance, trace_len_q1, trace_len_q3, trace_len_iqr, trace_len_geometric_mean, trace_len_geometric_std, trace_len_harmonic_mean, trace_len_skewness, trace_len_kurtosis, trace_len_coefficient_variation, trace_len_entropy, trace_len_hist1, trace_len_hist2, trace_len_hist3, trace_len_hist4, trace_len_hist5, trace_len_hist6, trace_len_hist7, trace_len_hist8, trace_len_hist9, trace_len_hist10, trace_len_skewness_hist, trace_len_kurtosis_hist |
| trace_variant    | ratio_most_common_variant, ratio_top_1_variants, ratio_top_5_variants, ratio_top_10_variants, ratio_top_20_variants, ratio_top_50_variants, ratio_top_75_variants, mean_variant_occurrence, std_variant_occurrence, skewness_variant_occurrence, kurtosis_variant_occurrence                                                                                                                                                                                                                                                                                      |
| activities       | n_unique_activities, activities_min, activities_max, activities_mean, activities_median, activities_std, activities_variance, activities_q1, activities_q3, activities_iqr, activities_skewness, activities_kurtosis                                                                                                                                                                                                                                                                                                                                              |
| start_activities | n_unique_start_activities, start_activities_min, start_activities_max, start_activities_mean, start_activities_median, start_activities_std, start_activities_variance, start_activities_q1, start_activities_q3, start_activities_iqr, start_activities_skewness, start_activities_kurtosis                                                                                                                                                                                                                                                                      |
| end_activities   | n_unique_end_activities, end_activities_min, end_activities_max, end_activities_mean, end_activities_median, end_activities_std, end_activities_variance, end_activities_q1, end_activities_q3, end_activities_iqr, end_activities_skewness, end_activities_kurtosis                                                                                                                                                                                                                                                                                              |
| entropies        | entropy_trace, entropy_prefix, entropy_global_block, entropy_lempel_ziv, entropy_k_block_diff_1, entropy_k_block_diff_3, entropy_k_block_diff_5, entropy_k_block_ratio_1, entropy_k_block_ratio_3, entropy_k_block_ratio_5, entropy_knn_3, entropy_knn_5, entropy_knn_7                                                                                                                                                                                                                                                                                           |
| complexity       | variant_entropy, normalized_variant_entropy, sequence_entropy, normalized_sequence_entropy, sequence_entropy_linear_forgetting, normalized_sequence_entropy_linear_forgetting, sequence_entropy_exponential_forgetting, normalized_sequence_entropy_exponential_forgetting                                                                                                                                                                                                                                                                                        |

### Examples
#### Example 1:
Pass sublist ['trace_variant', 'start_activities'] to get a list of values for the features 'trace_variant' and 'start_activities' only
```python
from feeed.feature_extractor import extract_features

features = extract_features("test_logs/100_4_0.1_0.1_0.1_0.35_0.35_0.xes", ['trace_variant', 'start_activities'])
```

Output should look like:
```python
{
'log': '100_4_0.1_0.1_0.1_0.35_0.35_0',
'ratio_most_common_variant': 0.23,
'ratio_top_1_variants': 0.0,
'ratio_top_5_variants': 0.23,
'ratio_top_10_variants': 0.38,
'ratio_top_20_variants': 0.61,
'ratio_top_50_variants': 0.86,
'ratio_top_75_variants': 0.94,
'mean_variant_occurrence': 4.545454545454546,
'std_variant_occurrence': 5.718608164478746,
'skewness_variant_occurrence': 1.985072284899168,
'kurtosis_variant_occurrence': 3.0175466630186563,
'n_unique_start_activities': 3,
'start_activities_min': 3,
'start_activities_max': 76,
'start_activities_mean': 33.333333333333336,
'start_activities_median': 21.0,
'start_activities_std': 31.051927834229907,
'start_activities_variance': 964.2222222222222,
'start_activities_q1': 12.0,
'start_activities_q3': 48.5,
'start_activities_iqr': 36.5,
'start_activities_skewness': 0.5331183329294154,
'start_activities_kurtosis': -1.5    
}
```



#### Example 2:
Get a full list of all feature values
```python
from feeed.feature_extractor import extract_features

features = extract_features("test_logs/100_4_0.1_0.1_0.1_0.35_0.35_0.xes")

```
Output should look like:
```python
{
'log': '100_4_0.1_0.1_0.1_0.35_0.35_0',
'n_traces': 100,
'n_unique_traces': 22,
'ratio_unique_traces_per_trace': 0.22,
'trace_len_min': 2,
'trace_len_max': 4,
'trace_len_mean': 2.95,
'trace_len_median': 3.0,
'trace_len_mode': 3,
'trace_len_std': 0.7399324293474372,
'trace_len_variance': 0.5475000000000001,
'trace_len_q1': 2.0,
'trace_len_q3': 3.25,
'trace_len_iqr': 1.25,
'trace_len_geometric_mean': 2.854490231707705,
'trace_len_geometric_std': 1.2984764500078683,
'trace_len_harmonic_mean': 2.758620689655172,
'trace_len_skewness': 0.07960741718130866,
'trace_len_kurtosis': -1.1710764996559713,
'trace_len_coefficient_variation': 0.25082455232116513,
'trace_len_entropy': 4.573311200693104,
'trace_len_hist1': 1.4999999999999987,
'trace_len_hist2': 0.0,
'trace_len_hist3': 0.0,
'trace_len_hist4': 0.0,
'trace_len_hist5': 0.0,
'trace_len_hist6': 2.2499999999999982,
'trace_len_hist7': 0.0,
'trace_len_hist8': 0.0,
'trace_len_hist9': 0.0,
'trace_len_hist10': 1.249999999999999,
'trace_len_skewness_hist': 0.07960741718130866,
'trace_len_kurtosis_hist': -1.1710764996559713,
'ratio_most_common_variant': 0.23,
'ratio_top_1_variants': 0.0,
'ratio_top_5_variants': 0.23,
'ratio_top_10_variants': 0.38,
'ratio_top_20_variants': 0.61,
'ratio_top_50_variants': 0.86,
'ratio_top_75_variants': 0.94,
'mean_variant_occurrence': 4.545454545454546,
'std_variant_occurrence': 5.718608164478746,
'skewness_variant_occurrence': 1.985072284899168,
'kurtosis_variant_occurrence': 3.0175466630186563,
'n_unique_activities': 4,
'activities_min': 46,
'activities_max': 100,
'activities_mean': 73.75,
'activities_median': 74.5,
'activities_std': 26.271419832205492,
'activities_variance': 690.1875,
'activities_q1': 48.25,
'activities_q3': 100.0,
'activities_iqr': 51.75,
'activities_skewness': -0.004885988614644778,
'activities_kurtosis': -1.9934880032201305,
'n_unique_start_activities': 3,
'start_activities_min': 3,
'start_activities_max': 76,
'start_activities_mean': 33.333333333333336,
'start_activities_median': 21.0,
'start_activities_std': 31.051927834229907,
'start_activities_variance': 964.2222222222222,
'start_activities_q1': 12.0,
'start_activities_q3': 48.5,
'start_activities_iqr': 36.5,
'start_activities_skewness': 0.5331183329294154,
'start_activities_kurtosis': -1.5,
'n_unique_end_activities': 4,
'end_activities_min': 15,
'end_activities_max': 31,
'end_activities_mean': 25.0,
'end_activities_median': 27.0,
'end_activities_std': 6.041522986797286,
'end_activities_variance': 36.5,
'end_activities_q1': 23.25,
'end_activities_q3': 28.75,
'end_activities_iqr': 5.5,
'end_activities_skewness': -0.8570822627169729,
'end_activities_kurtosis': -0.8648902233064364,
'entropy_trace': 3.631,
'entropy_prefix': 3.681,
'entropy_global_block': 4.201,
'entropy_lempel_ziv': 0.64,
'entropy_k_block_diff_1': 1.108,
'entropy_k_block_diff_3': 1.108,
'entropy_k_block_diff_5': 1.108,
'entropy_k_block_ratio_1': 1.906,
'entropy_k_block_ratio_3': 1.906,
'entropy_k_block_ratio_5': 1.906,
'entropy_knn_3': 1.932,
'entropy_knn_5': 1.506,
'entropy_knn_7': 1.231,
'variant_entropy': 93.64262454248438,
'normalized_variant_entropy': 0.7258742202126273,
'sequence_entropy': 466.3347685080803,
'normalized_sequence_entropy': 0.27796776430354214,
'sequence_entropy_linear_forgetting': 244.29290431274163,
'normalized_sequence_entropy_linear_forgetting': 0.1456154613225141,
'sequence_entropy_exponential_forgetting': 302.4021423657002,
'normalized_sequence_entropy_exponential_forgetting': 0.18025258486069465
}
```
