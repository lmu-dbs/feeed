import inspect
import numpy as np
import editdistance

from pm4py.algo.filtering.log.variants import variants_filter
from .feature import Feature

class Repetitions(Feature):
    def __init__(self, feature_names='repetitions'):
        self.feature_type = "repetitions"
        self.available_class_methods = dict(inspect.getmembers(Repetitions, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def loop_info_per_trace(log):
        # this method is a derivation of the method self_loop_per_trace_overview of the project Fig4PM,
        # found in https://github.com/f-zand/fig4pm/blob/main/general_methods.py
        loop_info = []
        for trace in log:
            loop_sizes = []
            current_index = 0
            while current_index < len(trace):
                current_activity = trace[current_index]["concept:name"]
                peek_distance = 0
                while current_index + peek_distance + 1 < len(trace):
                    peek_activity = trace[current_index + peek_distance + 1]["concept:name"]
                    if current_activity != peek_activity:
                        break
                    peek_distance += 1
                if peek_distance > 0:
                    loop_sizes.append(peek_distance)
                current_index += peek_distance + 1
            loop_info.append(loop_sizes)
        return loop_info

    def repetition_info_per_trace(log):
        # this method is a derivation of the method repetition_per_trace_overview of the project Fig4PM,
        # found in https://github.com/f-zand/fig4pm/blob/main/general_methods.py
        rep_overview = []
        for trace in log:
            window = []
            rep_size_list = []
            rep_size = 0
            for event_index in range(len(trace)):
                event = trace[event_index]["concept:name"]
                if event not in window:
                    # no repetition detected yet, add element to the current window
                    window.append(event)
                else:
                    # we found a repetition!
                    # get the last position where the event occurred
                    position = len(window) - 1 - window[::-1].index(event)
                    # do not consider this a repetition if it is a loop
                    if position == len(window) - 1:
                        window.append(event)
                    else:
                        # get the size of the repetition
                        rep_size += len(window[position: len(window) + 1])
                        rep_size_list.append(rep_size)
                        # delete the repetition, since we have already counted it
                        del window[position: len(window) + 1]
                        window.append(event)
            rep_overview.append(rep_size_list)
        return rep_overview

    @classmethod
    def n_traces_with_loop(cls, log):
        return len([loop_size for loop_size in Repetitions.loop_info_per_trace(log) if len(loop_size) > 0])

    @classmethod
    def avg_traces_with_loop(cls, log):
        return Repetitions.n_traces_with_loop(log) / len(log)

    @classmethod
    def avg_loops_per_trace(cls, log):
        return sum([len(loop_size) for loop_size in Repetitions.loop_info_per_trace(log)]) / len(log)

    @classmethod
    def max_loops_per_trace(cls, log):
        return max([len(loop_size) for loop_size in Repetitions.loop_info_per_trace(log)] + [0])

    @classmethod
    def avg_loop_size_per_trace(cls, log):
        number_of_traces_with_loop = Repetitions.n_traces_with_loop(log)
        if number_of_traces_with_loop == 0:
            return 0
        all_loop_sizes = [loop_size[i] for loop_size in Repetitions.loop_info_per_trace(log) for i in range(0,len(loop_size))]
        return sum(all_loop_sizes) / number_of_traces_with_loop

    @classmethod
    def max_loop_size_per_trace(cls, log):
        all_loop_sizes = [loop_size[i] for loop_size in Repetitions.loop_info_per_trace(log) for i in range(0,len(loop_size))]
        return max(all_loop_sizes + [0])

    @classmethod
    def n_traces_with_repetition(cls, log):
        return len([reps for reps in Repetitions.repetition_info_per_trace(log) if len(reps) > 0])

    @classmethod
    def avg_traces_with_repetition(cls, log):
        return Repetitions.n_traces_with_repetition(log) / len(log)
