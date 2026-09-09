import inspect
import numpy as np
from lempel_ziv_complexity import lempel_ziv_complexity
import editdistance

from ..feature import Feature
from ..activities import Activities
from ..simple_stats import SimpleStats

class ComparisonBased(Feature):
    def __init__(self, feature_names='comparison_based'):
        self.feature_type = "comparison_based"
        self.available_class_methods = dict(inspect.getmembers(ComparisonBased, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def consecutive_pairs(trace):
        return [(trace[i-1]["concept:name"], trace[i]["concept:name"]) for i in range(1, len(trace))]

    @classmethod
    def number_of_successions(cls, log):
        set_of_successions = set()
        for trace in log:
            set_of_successions.update(ComparisonBased.consecutive_pairs(trace))
        return len(set_of_successions)

    @classmethod
    def number_of_ties(cls, log):
        # check if the event log contains any traces
        if len(log) == 0:
            return 0
        # define symbols for the causal footprint relations
        follows = '->' # e1 is followed by e2 in some trace, but e2 is never followed by e1 in a trace
        precedes = '<-' # e2 is followed by e1 in some trace, but e1 is never followed by e2 in a trace
        parallel = '||' # e1 is followed by e2 in some trace, and e2 is followed by e1 in some trace
        incomparable = '#' # e1 is never followed by e2 in a trace, and e2 is never followed by e1 in a trace
        # get the set of events
        events = set(Activities.activities(log).keys())
        # initialize the causal footprint with only 'incomparable'-entries
        causal_footprint = {}
        for event in events:
            causal_footprint[event] = {}
            for other_event in events:
                causal_footprint[event][other_event] = incomparable
        # enrich the causal footprint with the correct relations between events
        for trace in log:
            for e1, e2 in ComparisonBased.consecutive_pairs(trace):
                if e1 == e2:
                    causal_footprint[e1][e2] = parallel
                elif causal_footprint[e1][e2] == precedes:
                    causal_footprint[e1][e2] = parallel
                    causal_footprint[e2][e1] = parallel
                elif causal_footprint[e1][e2] == incomparable:
                    causal_footprint[e1][e2] = follows
                    causal_footprint[e2][e1] = precedes
        # count the number of follows relations in the causal footprint
        number_of_ties = 0
        for event1 in events:
            for event2 in events:
                if causal_footprint[event1][event2] == follows:
                    number_of_ties += 1
        return number_of_ties

    @classmethod
    def structure(cls, log):
        return 1 - (ComparisonBased.number_of_ties(log) / (SimpleStats.n_variants(log) ** 2))

    @classmethod
    def average_affinity(cls, log):
        # check if the event log contains any traces
        if len(log) == 0:
            return 0
        # collect the event neighborhoods of every trace once, instead of per pair
        neighborhoods = [set(ComparisonBased.consecutive_pairs(trace)) for trace in log]
        # affinity(trace1, trace2) == affinity(trace2, trace1), so only the pairs with
        # i < j need to be computed; the diagonal (a trace compared to itself) is
        # excluded entirely, since the original formula subtracts it out anyway
        sum_of_affinity_values = 0
        n = len(log)
        for i in range(n):
            for j in range(i + 1, n):
                union = neighborhoods[i] | neighborhoods[j]
                if len(union) > 0:
                    sum_of_affinity_values += len(neighborhoods[i] & neighborhoods[j]) / len(union)
        return (2 * sum_of_affinity_values) / (n * (n - 1))

    @classmethod
    def lempel_ziv_complexity(cls, log):
        # check if the event log contains any traces
        if len(log) == 0:
            return 0
        # calculate the Lempel-Ziv complexity of the event log
        log_sequence = []
        for trace in log:
            for event in trace:
                log_sequence += [event["concept:name"]]
        return lempel_ziv_complexity(tuple(log_sequence))

    @classmethod
    def deviation_from_random(cls, log):
        activity_names = set(Activities.activities(log).keys())
        # initialize a dictionary that collects how often events follow each other
        neighborhood_frequencies = dict()
        for event1 in activity_names:
            neighborhood_frequencies[event1] = dict()
            for event2 in activity_names:
                neighborhood_frequencies[event1][event2] = 0
        # go through the event log and fill the previously initialized dictionary
        total_number_of_neighborhoods = 0
        for trace in log:
            for event1, event2 in ComparisonBased.consecutive_pairs(trace):
                neighborhood_frequencies[event1][event2] += 1
                total_number_of_neighborhoods += 1
        # calculate the inverse deviation from random
        random_neighborhood_frequencies = total_number_of_neighborhoods / (len(activity_names)**2)
        inverse_dev_random = 0
        for event1 in activity_names:
            for event2 in activity_names:
                inverse_dev_random += ((abs(neighborhood_frequencies[event1][event2] - random_neighborhood_frequencies)) / (total_number_of_neighborhoods))**2
        inverse_dev_random = np.sqrt(inverse_dev_random)
        return 1 - inverse_dev_random

    @classmethod
    def average_edit_distance(cls, log):
        # editdistance.eval(a, b) == editdistance.eval(b, a), so only the pairs with
        # i < j need to be computed; the diagonal is always 0 and thus excluded
        traces = list(log)
        n = len(traces)
        sum_of_edit_distances = 0
        for i in range(n):
            for j in range(i + 1, n):
                sum_of_edit_distances += editdistance.eval(traces[i], traces[j])
        return (2 * sum_of_edit_distances) / (n * (n - 1))
