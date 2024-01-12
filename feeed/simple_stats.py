from pm4py.algo.filtering.log.variants import variants_filter

class SimpleStats:
    def __init__(self, log):
        self.log = log
        #print("INIT", self.n_traces(self.log))

    @classmethod
    def n_traces(self, log):
        return len(log)

    @classmethod
    def n_unique_traces(self, log):
        variants = variants_filter.get_variants(log)
        return len(variants)

    @classmethod
    def ratio_unique_traces_per_trace(self, log):
        variants = variants_filter.get_variants(log)


def simple_stats(log):
    simplestats = SimpleStats(log)
    print("TEST")

    result = {
            "n_traces": simplestats.n_traces(log),
            "n_unique_traces": simplestats.n_unique_traces(log),
            "ratio_unique_traces_per_trace": simplestats.n_unique_traces(log)/ simplestats.n_traces(log)
            }

    return result
