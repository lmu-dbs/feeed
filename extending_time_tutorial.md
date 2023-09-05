# Tutorial for extending time-based features

The `feeed/time.py` is a script that contains the class `Timestamp`. This class extracts knowledge from timestamps. In summary, each feature should be extracted from each group (i.e., case id) or from the whole log (e.g., time within the day).

Implementing time-based features as `@classmethods` within this class allows us to easily scale and manage features. A tiny botleneck is that each class method should accept `**kwargs` regardless of the other arguments. Each class method is accessed by inspecting the object using `inspect.getmembers`. 

All features are currently measured in seconds. The current features include:

- `execution_time`: execution time of an event w.r.t. to the previous one
- `accumulated_time`: accumulated time of an event w.r.t. to the first one from a trace
- `remaining_time`: remaining time of an event w.r.t. to the last one from a trace
- `within_day`: time within the day 

## Extending the `Timestamp` class

As an example of how to extand the class, we could just include a new class method to extract a categorical value containing the weekday:

```python
@classmethod
def weekday(cls, X, time_col="time:timestamp", **kwargs):
    return X[time_col].dt.dayofweek.astype(np.float32)
```

**NOTE**: 

- the current implementation assumes that we are passing a DataFrame containing a timedelta object identified by the `time_col` variable
- there are methods that accept `group` and `X` as arguments. The former consists of a trace since we evaluate, for instance, the event timestamp with the previous one. The latter does not take depend on the trace level since we simply transform any `timedeta` data into, for instance, a categorical containing the weekday.
- the aforementioned example was not tested