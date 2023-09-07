# FEEED
**Fe**ature **E**xtraction for **E**vent **D**ata

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Extending](#extending)

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
| complexity       | variant_entropy, normalized_variant_entropy, sequence_entropy, normalized_sequence_entropy, sequence_entropy_linear_forgetting, normalized_sequence_entropy_linear_forgetting, sequence_entropy_exponential_forgetting, normalized_sequence_entropy_exponential_forgetting                                                                                                                                                                                                                                                              
| time_based     | time_based_min, time_based_max, time_based_mean, time_based_median, time_based_mode, time_based_std, time_based_variance, time_based_q1, time_based_q3, time_based_iqr, time_based_geometric_mean, time_based_geometric_std, time_based_harmonic_mean, time_based_skewness, time_based_kurtosis, time_based_coefficient_variation, time_based_entropy, time_based_hist1, time_based_hist2, time_based_hist3, time_based_hist4, time_based_hist5, time_based_hist6, time_based_hist7, time_based_hist8, time_based_hist9, time_based_hist10, time_based_skewness_hist, time_based_kurtosis_hist |

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
'accumulated_time_time_coefficient_variation': 4.039353340541942
'accumulated_time_time_entropy': 7.7513093893416505
'accumulated_time_time_geometric_mean': 10904.332835327972
'accumulated_time_time_geometric_std': 44.90292804116573
'accumulated_time_time_harmonic_mean': 0.0
'accumulated_time_time_hist0': 2.6951738756336187e-07
'accumulated_time_time_hist1': 2.17962865226352e-09
'accumulated_time_time_hist2': 1.080807596163729e-09
'accumulated_time_time_hist3': 3.9629611859336717e-10
'accumulated_time_time_hist4': 3.242422788491186e-10
'accumulated_time_time_hist5': 2.34174979168808e-10
'accumulated_time_time_hist6': 1.2609421955243496e-10
'accumulated_time_time_hist7': 5.4040379808186465e-11
'accumulated_time_time_hist8': 5.4040379808186465e-11
'accumulated_time_time_hist9': 9.006729968031069e-11
'accumulated_time_time_iqr': 272655.0
'accumulated_time_time_kurtosis': 172.57258047803998
'accumulated_time_time_kurtosis_hist': 5.1101603988544575
'accumulated_time_time_max': 36488789.0
'accumulated_time_time_mean': 396893.5456158801
'accumulated_time_time_median': 11924.0
'accumulated_time_time_min': 0.0
'accumulated_time_time_mode': 0.0
'accumulated_time_time_q1': 1138.5
'accumulated_time_time_q3': 273793.5
'accumulated_time_time_skewness': 11.401470845961653
'accumulated_time_time_skewness_hist': 2.6663623098416838
'accumulated_time_time_std': 1603193.2693230559
'accumulated_time_time_variance': 2570228658802.748
'activities_iqr': 983.5
'activities_kurtosis': 1.05777753209275
'activities_max': 3383
'activities_mean': 950.875
'activities_median': 788.0
'activities_min': 6
'activities_q1': 101.75
'activities_q3': 1085.25
'activities_skewness': 1.3912385607018212
'activities_std': 1008.5815457239935
'activities_variance': 1017236.734375
'end_activities_iqr': 39.5
'end_activities_kurtosis': 2.5007579343413617
'end_activities_max': 393
'end_activities_mean': 75.0
'end_activities_median': 32.5
'end_activities_min': 2
'end_activities_q1': 14.0
'end_activities_q3': 53.5
'end_activities_skewness': 2.004413358907822
'end_activities_std': 112.91400014423114
'end_activities_variance': 12749.57142857143
'execution_time_time_coefficient_variation': 8.499578843161144
'execution_time_time_entropy': 6.221052534222753
'execution_time_time_geometric_mean': 199.88320191111325
'execution_time_time_geometric_std': 127.92792986844444
'execution_time_time_harmonic_mean': 0.0
'execution_time_time_hist0': 2.7448347367316943e-07
'execution_time_time_hist1': 1.002762607241735e-09
'execution_time_time_hist2': 6.928178013670171e-10
'execution_time_time_hist3': 3.2817685327911313e-10
'execution_time_time_hist4': 3.2817685327911313e-10
'execution_time_time_hist5': 2.552486636615327e-10
'execution_time_time_hist6': 9.116023702197587e-11
'execution_time_time_hist7': 5.469614221318552e-11
'execution_time_time_hist8': 7.292818961758069e-11
'execution_time_time_hist9': 7.292818961758069e-11
'execution_time_time_iqr': 18623.25
'execution_time_time_kurtosis': 250.48825320470718
'execution_time_time_kurtosis_hist': 5.110914600502133
'execution_time_time_max': 36051318.0
'execution_time_time_mean': 169759.47397134217
'execution_time_time_median': 188.0
'execution_time_time_min': 0.0
'execution_time_time_mode': 0.0
'execution_time_time_q1': 0.0
'execution_time_time_q3': 18623.25
'execution_time_time_skewness': 14.528527518337814
'execution_time_time_skewness_hist': 2.666603580180752
'execution_time_time_std': 1442884.0333930943
'execution_time_time_variance': 2081914333820.724
'kurtosis_variant_occurrence': 217.44268017168216
'log': 'SEPSIS'
'mean_variant_occurrence': 1.2411347517730495
'n_traces': 1050
'n_unique_activities': 16
'n_unique_end_activities': 14
'n_unique_start_activities': 6
'n_unique_traces': 846
'ratio_most_common_variant': 0.03333333333333333
'ratio_top_10_variants': 0.2742857142857143
'ratio_top_1_variants': 0.12
'ratio_top_20_variants': 0.35523809523809524
'ratio_top_50_variants': 0.5971428571428572
'ratio_top_5_variants': 0.21523809523809523
'ratio_top_75_variants': 0.7980952380952381
'ratio_unique_traces_per_trace': 0.8057142857142857
'remaining_time_time_coefficient_variation': 1.8886403422401359
'remaining_time_time_entropy': 8.55331137332654
'remaining_time_time_geometric_mean': 224736.22203397762
'remaining_time_time_geometric_std': 70.1715364379747
'remaining_time_time_harmonic_mean': 0.0
'remaining_time_time_hist0': 2.1808895944590443e-07
'remaining_time_time_hist1': 2.1580125003402454e-08
'remaining_time_time_hist2': 1.4590902548210341e-08
'remaining_time_time_hist3': 6.8991551555118015e-09
'remaining_time_time_hist4': 4.503364984015537e-09
'remaining_time_time_hist5': 3.818853506445177e-09
'remaining_time_time_hist6': 1.6572383141177165e-09
'remaining_time_time_hist7': 9.006729968031077e-10
'remaining_time_time_hist8': 7.385518573785483e-10
'remaining_time_time_hist9': 1.2789556554604117e-09
'remaining_time_time_iqr': 2284557.5
'remaining_time_time_kurtosis': 11.66672043634066
'remaining_time_time_kurtosis_hist': 4.950830339077765
'remaining_time_time_max': 36488789.0
'remaining_time_time_mean': 2796232.825161036
'remaining_time_time_median': 619470.0
'remaining_time_time_min': 0.0
'remaining_time_time_mode': 0.0
'remaining_time_time_q1': 202862.5
'remaining_time_time_q3': 2487420.0
'remaining_time_time_skewness': 3.1659682263680318
'remaining_time_time_skewness_hist': 2.61693528788402
'remaining_time_time_std': 5281078.119895157
'remaining_time_time_variance': 27889786108435.367
'skewness_variant_occurrence': 13.637101374069475
'start_activities_iqr': 9.25
'start_activities_kurtosis': 1.199106773708694
'start_activities_max': 995
'start_activities_mean': 175.0
'start_activities_median': 12.0
'start_activities_min': 6
'start_activities_q1': 7.75
'start_activities_q3': 17.0
'start_activities_skewness': 1.7883562472303318
'start_activities_std': 366.73787187399483
'start_activities_variance': 134496.66666666666
'std_variant_occurrence': 1.7594085182491936
'trace_len_coefficient_variation': 0.7916391922924689
'trace_len_entropy': 6.769403523350811
'trace_len_geometric_mean': 12.281860759040898
'trace_len_geometric_std': 1.7464004837799154
'trace_len_harmonic_mean': 10.47731701485374
'trace_len_hist1': 0.048613291470434326
'trace_len_hist10': 0.00010465724751439027
'trace_len_hist2': 0.005285190999476714
'trace_len_hist3': 0.0005756148613291472
'trace_len_hist4': 0.0002093144950287807
'trace_len_hist5': 0.00010465724751439036
'trace_len_hist6': 0.0
'trace_len_hist7': 5.232862375719522e-05
'trace_len_hist8': 0.0
'trace_len_hist9': 0.0
'trace_len_iqr': 7.0
'trace_len_kurtosis': 87.03769068983992
'trace_len_kurtosis_hist': 87.03769068983992
'trace_len_max': 185
'trace_len_mean': 14.48952380952381
'trace_len_median': 13.0
'trace_len_min': 3
'trace_len_mode': 8
'trace_len_q1': 9.0
'trace_len_q3': 16.0
'trace_len_skewness': 7.250526815880918
'trace_len_skewness_hist': 7.250526815880918
'trace_len_std': 11.470474925273926
'trace_len_variance': 131.57179501133788
'within_day_time_coefficient_variation': 0.49820042247168106
'within_day_time_entropy': 9.501009299480838
'within_day_time_geometric_mean': 35069.233548115764
'within_day_time_geometric_std': 1.9726454507370417
'within_day_time_harmonic_mean': 0.0
'within_day_time_hist0': 3.2487851331575074e-06
'within_day_time_hist1': 2.617288257157336e-06
'within_day_time_hist2': 3.474754497220219e-05
'within_day_time_hist3': 1.1808230741593563e-05
'within_day_time_hist4': 1.2667979500485362e-05
'within_day_time_hist5': 1.3687504577401301e-05
'within_day_time_hist6': 1.1876706306461051e-05
'within_day_time_hist7': 9.822439360436398e-06
'within_day_time_hist8': 9.297460029785654e-06
'within_day_time_hist9': 5.980199331760658e-06
'within_day_time_iqr': 34486.25
'within_day_time_kurtosis': -0.9142275965359783
'within_day_time_kurtosis_hist': 2.6115894228132266
'within_day_time_max': 86390.0
'within_day_time_mean': 41330.543183909555
'within_day_time_median': 37800.0
'within_day_time_min': 0.0
'within_day_time_mode': 21600.0
'within_day_time_q1': 23113.75
'within_day_time_q3': 57600.0
'within_day_time_skewness': 0.3603519661740256
'within_day_time_skewness_hist': 1.7511033515349685
'within_day_time_std': 20590.894075207754
'within_day_time_variance': 423984918.81642574
}
```

## Tutorial for extending to additional features (e.g. time-based)

For this tutorial, we focus on the example of time-based features. The `feeed/time.py` is a script that currently contains the class `Timestamp`, which extracts knowledge from timestamps. In summary, features could be extracted from groups (i.e., cases) or from the whole log (e.g., time within the day).

Implementing each time-based feature as `@classmethods` within this class allows us to easily scale and manage features. A tiny botleneck is that each class method should accept `**kwargs` regardless of the other arguments (but this can be internaly handled in the future). Each class method is accessed by inspecting the object using `inspect.getmembers`. 

All the features are currently measured in seconds, and they include include:

- `execution_time`: execution time of an event w.r.t. to the previous one
- `accumulated_time`: accumulated time of an event w.r.t. to the first one from a trace
- `remaining_time`: remaining time of an event w.r.t. to the last one from a trace
- `within_day`: time within the day 

There are methods that accept `group` or `X` as arguments. The former consists of a trace (i.e., grouped by case id) since we evaluate, for instance, the event timestamp with the previous one. The latter consists of the whole event log, since some operations can be performed element-wise (e.g., extracting the weekday from a timestamp column).

### Implementing any `NewFeature` class

See an example of how to implement a new feature extraction class:

```python
class NewFeature:
    @classmethod
    def foo(cls, **kwargs):
        return kwargs["X"] ** 2
    
    @classmethod
    def bar(cls, **kwargs):
        return kwargs["group"] + 1
```
