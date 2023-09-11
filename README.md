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

The output data containg a `feature_type` and a `summary` value obtained by certain aggregatino fucntions. The schema looks like:
```python
{
'log': 'Sepsis'
'featureType_summary': value
}
```
<!-- ```python
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
``` -->



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
'execution_time_time_coefficient_variation': 8.499578843161144
'execution_time_time_entropy': 6.221052534222753
'execution_time_time_geometric_mean': 199.88320191111325
'execution_time_time_geometric_std': 127.92792986844444
'execution_time_time_harmonic_mean': 0.0
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

### Overview

In order to colaborate and include new features in this repo, consider:

* defining if the proposed feature is log-level, opposed to single event, trace, activity level.
* Next, check for dependency and Python version compatibility with this current repo (see `setup.py`).
* The class/method needs to be called by including it in the list of feeed/feature_extractor.py and importing the new method accordingly. Furthermore, the "feature type" needs to be included in the exception of feeed/feature_extractor.py
* The new "feature type" and its features (i.e. summary obtained by aggregation/statistic functions) need to be included in the README.md table
* The output of the newFeature class needs to be a dict of the sort: `{"featureType_summary1": value1, "featureType_summary2": value2}`

### Example 

As an example for this tutorial, let us we focus on the example of time-based features. The `feeed/time.py` is a script that currently contains the class `Timestamp`, which extracts knowledge from timestamps. In summary, features could be extracted from groups (i.e., cases) or from the whole log (e.g., time within the day).

<!-- Implementing each time-based feature as `@classmethods` within this class allows us to easily scale and manage features. A tiny botleneck is that each class method should accept `**kwargs` regardless of the other arguments (but this can be internaly handled in the future). Each class method is accessed by inspecting the object using `inspect.getmembers`.  -->

All the time features are currently measured in seconds, and they include:

- `execution_time`: execution time of an event w.r.t. to the previous one
- `accumulated_time`: accumulated time of an event w.r.t. to the first one from a trace
- `remaining_time`: remaining time of an event w.r.t. to the last one from a trace
- `within_day`: time within the day 

Essentially, there are methods that accept `group` or `X` as arguments. The former consists of a trace (i.e., grouped by case id) since we evaluate, for instance, the event timestamp with the previous one. The latter consists of the whole event log, since some operations can be performed element-wise (e.g., extracting the weekday from a timestamp column).

### Implementing any `NewFeature` class

Below, see an example of pseudo code of how to implement a new (generic) feature extraction class:

```python
import inspect

class NewFeature:
    @classmethod
    def foo(cls, **kwargs):
        return kwargs["event_attribute"] ** 2
    
    @classmethod
    def bar(cls, **kwargs):
        return kwargs["event_attribute"] + 1

def extract_new_feature():
    available_class_methods = inspect.getmembers(NewFeature, predicate=inspect.ismethod)
    output = {}
    for feature_name, feature_fn in available_class_methods:
        arr_values = feature_fn(log)
        output[f"NewFeature_{feature_name}"] = summarize(arr_values)

    return output
```
### Testing the new implementation

After implementing the new feature and including it in the list of `feeed/feature_extractor.py` and importing the new method accordingly, you can quickly test it by running:

```bash
python -c "from feeed.feature_extractor import extract_features; print(extract_features('/home/seidi/datasets/logs/sepsis/SEPSIS.xes', ['extract_new_feature']))"
```