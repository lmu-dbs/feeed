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
pip install feed
```
Run:
```shell
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_logs/Sepsis.xes'))"
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

features = extract_features("test_logs/Sepsis.xes", ['trace_variant', 'start_activities'])
```

Output should look like:
```python
{
'log': 'Sepsis'
'ratio_most_common_variant': 0.03333333333333333
'ratio_top_1_variants': 0.12
'ratio_top_5_variants': 0.21523809523809523
'ratio_top_10_variants': 0.2742857142857143
'ratio_top_20_variants': 0.35523809523809524
'ratio_top_50_variants': 0.5971428571428572
'ratio_top_75_variants': 0.7980952380952381
'mean_variant_occurrence': 1.2411347517730495
'std_variant_occurrence': 1.7594085182491936
'skewness_variant_occurrence': 13.637101374069475
'kurtosis_variant_occurrence': 217.44268017168216
'n_unique_start_activities': 6
'start_activities_min': 6
'start_activities_max': 995
'start_activities_mean': 175.0
'start_activities_median': 12.0
'start_activities_std': 366.73787187399483
'start_activities_variance': 134496.66666666666
'start_activities_q1': 7.75
'start_activities_q3': 17.0
'start_activities_iqr': 9.25
'start_activities_skewness': 1.7883562472303318
'start_activities_kurtosis': 1.199106773708694
}
```



#### Example 2:
Get a full list of all feature values
```python
from feeed.feature_extractor import extract_features

features = extract_features("test_logs/Sepsis.xes")

```
Output should look like:
```python
{
'log': 'Sepsis'
'n_traces': 1050
'n_unique_traces': 846
'ratio_unique_traces_per_trace': 0.8057142857142857
'trace_len_min': 3
'trace_len_max': 185
'trace_len_mean': 14.48952380952381
'trace_len_median': 13.0
'trace_len_mode': 8
'trace_len_std': 11.470474925273926
'trace_len_variance': 131.57179501133788
'trace_len_q1': 9.0
'trace_len_q3': 16.0
'trace_len_iqr': 7.0
'trace_len_geometric_mean': 12.281860759040903
'trace_len_geometric_std': 1.7464004837799154
'trace_len_harmonic_mean': 10.47731701485374
'trace_len_skewness': 7.250526815880918
'trace_len_kurtosis': 87.0376906898399
'trace_len_coefficient_variation': 0.7916391922924689
'trace_len_entropy': 6.769403523350811
'trace_len_hist1': 0.048613291470434326
'trace_len_hist2': 0.005285190999476714
'trace_len_hist3': 0.0005756148613291472
'trace_len_hist4': 0.0002093144950287807
'trace_len_hist5': 0.00010465724751439036
'trace_len_hist6': 0.0
'trace_len_hist7': 5.232862375719522e-05
'trace_len_hist8': 0.0
'trace_len_hist9': 0.0
'trace_len_hist10': 0.00010465724751439027
'trace_len_skewness_hist': 7.250526815880918
'trace_len_kurtosis_hist': 87.0376906898399
'ratio_most_common_variant': 0.03333333333333333
'ratio_top_1_variants': 0.12
'ratio_top_5_variants': 0.21523809523809523
'ratio_top_10_variants': 0.2742857142857143
'ratio_top_20_variants': 0.35523809523809524
'ratio_top_50_variants': 0.5971428571428572
'ratio_top_75_variants': 0.7980952380952381
'mean_variant_occurrence': 1.2411347517730495
'std_variant_occurrence': 1.7594085182491936
'skewness_variant_occurrence': 13.637101374069475
'kurtosis_variant_occurrence': 217.44268017168216
'n_unique_activities': 16
'activities_min': 6
'activities_max': 3383
'activities_mean': 950.875
'activities_median': 788.0
'activities_std': 1008.5815457239935
'activities_variance': 1017236.734375
'activities_q1': 101.75
'activities_q3': 1085.25
'activities_iqr': 983.5
'activities_skewness': 1.3912385607018212
'activities_kurtosis': 1.05777753209275
'n_unique_start_activities': 6
'start_activities_min': 6
'start_activities_max': 995
'start_activities_mean': 175.0
'start_activities_median': 12.0
'start_activities_std': 366.73787187399483
'start_activities_variance': 134496.66666666666
'start_activities_q1': 7.75
'start_activities_q3': 17.0
'start_activities_iqr': 9.25
'start_activities_skewness': 1.7883562472303318
'start_activities_kurtosis': 1.199106773708694
'n_unique_end_activities': 14
'end_activities_min': 2
'end_activities_max': 393
'end_activities_mean': 75.0
'end_activities_median': 32.5
'end_activities_std': 112.91400014423114
'end_activities_variance': 12749.57142857143
'end_activities_q1': 14.0
'end_activities_q3': 53.5
'end_activities_iqr': 39.5
'end_activities_skewness': 2.004413358907822
'end_activities_kurtosis': 2.5007579343413617
'entropy_trace': 9.334
'entropy_prefix': 10.227
'entropy_global_block': 14.501
'entropy_lempel_ziv': 1.727
'entropy_k_block_diff_1': -0.019
'entropy_k_block_diff_3': 1.837
'entropy_k_block_diff_5': 1.712
'entropy_k_block_ratio_1': 2.262
'entropy_k_block_ratio_3': 3.238
'entropy_k_block_ratio_5': 2.538
'entropy_knn_3': 4.956
'entropy_knn_5': 4.49
'entropy_knn_7': 4.191
'variant_entropy': 40624.49329803771
'normalized_variant_entropy': 0.6957588422064969
'sequence_entropy': 76528.6794749776
'normalized_sequence_entropy': 0.5223430410751398
'sequence_entropy_linear_forgetting': 32139.284589305265
'normalized_sequence_entropy_linear_forgetting': 0.21936523360299368
'sequence_entropy_exponential_forgetting': 43880.53919110408
'normalized_sequence_entropy_exponential_forgetting': 0.29950463593968696
}
