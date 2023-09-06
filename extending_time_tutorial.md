# Tutorial for extending time-based features

The `feeed/time.py` is a script that currently contains the class `Timestamp`. This class extracts knowledge from timestamps. In summary, features should be extracted from groups (i.e., cases) or from the whole log (e.g., time within the day).

Implementing time-based features as `@classmethods` within this class allows us to easily scale and manage features. A tiny botleneck is that each class method should accept `**kwargs` regardless of the other arguments (but this can be internaly handled in the future). Each class method is accessed by inspecting the object using `inspect.getmembers`. 

All features are currently measured in seconds. The current features include:

- `execution_time`: execution time of an event w.r.t. to the previous one
- `accumulated_time`: accumulated time of an event w.r.t. to the first one from a trace
- `remaining_time`: remaining time of an event w.r.t. to the last one from a trace
- `within_day`: time within the day 

**NOTE**: 

- the current implementation assumes that we are passing a DataFrame containing a timedelta object identified by the `time_col` variable
- there are methods that accept `group` and `X` as arguments. The former consists of a trace since we evaluate, for instance, the event timestamp with the previous one. The latter does not take depend on the trace level since we simply transform any `timedeta` data into, for instance, a categorical containing the weekday.
- the aforementioned example was not tested

## Implementing any `NewFeature` class

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
