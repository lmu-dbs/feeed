import pandas as pd
import subprocess
import math
import pm4py


class Event:
    __slots__ = "case_id", "activity", "timestamp", "predecessor", "event_id"
    _counter = 0

    def __init__(self, id, a, ts, p=None):
        self.case_id = id
        self.activity = a
        self.timestamp = ts
        self.predecessor = p
        Event._counter += 1
        self.event_id = Event._counter


class Node:
    def __init__(self, name):
        self.name = name
        self.successors = {}
        self.c = 0
        self.j = 0


class ActivityType(Node):
    def __init__(self, activity, predecessor, c, accepting=True):
        self.activity = activity
        self.sequence = []
        self.predecessor = predecessor
        self.successors = {}
        self.c = c
        self.j = predecessor.j + 1
        self.label = (
            "<"
            + "s"
            + "<sup>"
            + str(c)
            + "</sup>"
            + "<sub>"
            + str(self.j)
            + "</sub>"
            + ">"
        )
        self.name = activity + "Type" + str(c) + "_" + str(self.j)
        self.accepting = accepting

    def getPrefix(self):
        prefix = self.activity
        if self.predecessor.name != "root":
            prefix = self.predecessor.getPrefix() + "," + prefix
        return prefix


class Graph:
    def __init__(self):
        self.c = 1
        self.root = Node("root")
        self.nodes = [self.root]
        self.activity_types = dict()
        self.last_at = dict()
        self.c_index = {}

    def addNode(self, activity, predecessor, c, accepting=True, verbose=False):
        node = ActivityType(activity, predecessor, c, accepting)
        node.predecessor.successors[activity] = node
        self.nodes.append(node)
        if activity not in self.activity_types:
            self.activity_types[activity] = []
        self.activity_types[activity].append(node)
        if verbose:
            print("Adding activity type: " + node.name)
        return node

    def draw(self, subg=False, accepting=False):
        dot_string = """digraph G {
    rankdir=LR;
    node [shape=circle fontsize=30.0];
    edge [fontsize=30.0];
    subgraph Rel1 {
"""
        for node in self.nodes:
            if node != self.root:
                dot_string += '\t\t"' + node.name + '" [label=' + node.label + "];\n"
                dot_string += (
                    '\t\t"'
                    + node.predecessor.name
                    + '" -> "'
                    + node.name
                    + '" [label="'
                    + node.activity
                    + '"]'
                    + ";\n"
                )
        dot_string += "\t}"
        if subg:
            dot_string += """\n\tsubgraph Rel2 {
        edge [dir=none]
        node [shape=rectangle]
"""
            for node in self.nodes:
                if node != self.root:
                    dot_string += (
                        "\t\t" + '"' + str(node.sequence[0].event_id) + '"'
                    )
                    dot_string += (
                        " [label=<"
                        + ",".join(
                            [
                                event.activity
                                + "<sup>"
                                + str(event.case_id)
                                + "</sup>"
                                + "<sub>"
                                + str(event.event_id)
                                + "</sub>"
                                for event in node.sequence
                            ]
                        )
                        + ">];\n"
                    )
                    dot_string += (
                        '\t\t"'
                        + node.name
                        + '" -> '
                        + '"'
                        + str(node.sequence[0].event_id)
                        + '";\n'
                    )
            dot_string += "\t}\n"
        if accepting:
            for node in self.nodes:
                if node != self.root and hasattr(node, "accepting") and node.accepting:
                    dot_string += '\n\t"' + node.name + '" [shape=doublecircle]'
        dot_string += "\n}"
        return dot_string

    def get_first_timestamp(self):
        return min(
            [
                min([event.timestamp for event in node.sequence])
                for node in self.nodes
                if node != self.root
            ]
        )

    def get_last_timestamp(self):
        return max(
            [
                max([event.timestamp for event in node.sequence])
                for node in self.nodes
                if node != self.root
            ]
        )

    def get_timespan(self):
        return (self.get_last_timestamp() - self.get_first_timestamp()).total_seconds()

    def to_plain_log(self):
        return sorted(
            flatten([node.sequence for node in self.nodes if node != self.root]),
            key=lambda event: event.timestamp,
        )

    def to_pm4py_log(self):
        traces = {}
        for event in sorted(
            self.to_plain_log(), key=lambda event: (event.case_id, event.timestamp)
        ):
            if event.predecessor and (event.case_id not in traces):
                raise Exception("Could not convert to PM4Py log")
            if event.case_id not in traces:
                traces[event.case_id] = pm4py.objects.log.obj.Trace()
            pm4py_event = pm4py.objects.log.obj.Event()
            pm4py_event["concept:name"] = event.activity
            pm4py_event["time:timestamp"] = event.timestamp
            traces[event.case_id].append(pm4py_event)
        return pm4py.objects.log.obj.EventLog(traces.values())

def generate_pm4py_log(filename=None, verbose=False):
    if filename == None:
        raise Exception("No file specified")

    if filename.split(".")[-1] == "xes":
        input_file = filename
        from pm4py.objects.log.importer.xes import importer as xes_importer

        pm4py_log = xes_importer.apply(input_file)
    elif filename.split(".")[-1] == "csv":
        subprocess.call(["head", filename])
        i_h = input("Does the file have a header? [y/N]:") or "n"
        h = 0 if i_h != "n" else None
        i_d = input("What is the delimiter? [,]:") or ","
        i_c = input("What is the column number of case ID? [0]:")
        i_c = 0 if i_c == "" else int(i_c)
        i_a = input("What is the column number of activity name? [1]:")
        i_a = 1 if i_a == "" else int(i_a)
        i_t = input("What is the column number of timestamp? [2]:")
        i_t = 2 if i_t == "" else int(i_t)

        from pm4py.objects.conversion.log import converter as log_converter
        from pm4py.objects.log.util import dataframe_utils

        log_csv = pd.read_csv(filename, sep=i_d, header=h)
        log_csv.rename(
            columns={
                log_csv.columns[i_c]: "case",
                log_csv.columns[i_a]: "concept:name",
                log_csv.columns[i_t]: "time:timestamp",
            },
            inplace=True,
        )
        for col in log_csv.columns:
            if isinstance(col, int):
                log_csv.rename(columns={col: "column" + str(col)}, inplace=True)
        log_csv = dataframe_utils.convert_timestamp_columns_in_df(log_csv)
        log_csv = log_csv.sort_values("time:timestamp")
        parameters = {
            log_converter.Variants.TO_EVENT_LOG.value.Parameters.CASE_ID_KEY: "case"
        }
        if verbose:
            print(log_csv)
        pm4py_log = log_converter.apply(
            log_csv, parameters=parameters, variant=log_converter.Variants.TO_EVENT_LOG
        )

    else:
        raise Exception("File type not recognized, should be xes or csv")

    return pm4py_log


def generate_log(pm4py_log, verbose=False):
    log = []
    for trace in pm4py_log:
        for event in trace:
            log.append(
                Event(
                    trace.attributes["concept:name"],
                    event["concept:name"],
                    event["time:timestamp"],
                )
            )

    log.sort(key=lambda event: event.timestamp)

    last_event = {}
    for event in log:
        if event.case_id in last_event:
            event.predecessor = last_event[event.case_id]
        last_event[event.case_id] = event

    if verbose:
        print("Case ID, Activity, Timestamp, Predecessor, Event ID")
        for event in log:
            print(
                ",".join(
                    [
                        str(event.case_id),
                        event.activity,
                        str(event.timestamp),
                        (
                            event.predecessor.activity
                            + "-"
                            + str(event.predecessor.event_id)
                            if event.predecessor
                            else "-"
                        ),
                        str(event.event_id),
                    ]
                )
            )

    return log

def flatten(in_list):
    out_list = []
    for item in in_list:
        if isinstance(item, list):
            out_list.extend(flatten(item))
        else:
            out_list.append(item)
    return out_list


def build_graph(log, verbose=False, accepting=False):
    if len(log) == 0:
        raise Exception("Cannot build EPA from an empty log")
    if verbose:
        print("Building the prefix automaton...")

    pa = Graph()
    pa = add_events_to_graph(pa, log, verbose=verbose)
    if accepting:
        pa = mark_accepting_states(pa)
    return pa


def find_predecessor(event, pa, verbose=False):
    if event.predecessor:
        if event.predecessor != pa.root:
            if (
                event.case_id in pa.last_at
                and event.predecessor in pa.last_at[event.case_id].sequence
            ):  # doesnt affect speed
                pred_activity_type = pa.last_at[event.case_id]
            else:
                raise Exception("Error")
    else:
        pred_activity_type = pa.root

    return pred_activity_type


def add_event_to_graph(event, pa, verbose=False):
    pred_activity_type = find_predecessor(event, pa, verbose=verbose)
    current_activity_type = None
    if event.activity in pred_activity_type.successors:  # keys
        current_activity_type = pred_activity_type.successors[event.activity]
    else:
        if len(pred_activity_type.successors) > 0:
            pa.c += 1
            curr_c = pa.c
        else:
            curr_c = pred_activity_type.c if pred_activity_type != pa.root else pa.c
        current_activity_type = pa.addNode(
            event.activity, pred_activity_type, curr_c, verbose=verbose
        )

    current_activity_type.sequence.append(event)
    pa.last_at[event.case_id] = current_activity_type

    return current_activity_type


def add_events_to_graph(pa, log, verbose=False):
    for event in log:
        add_event_to_graph(event, pa, verbose=verbose)
    pa.nodes.sort(key=lambda node: (node.c, node.j))
    return pa


def create_c_index(pa):
    c_index = {}
    for node in pa.nodes:
        if node.c not in c_index:
            c_index[node.c] = []
        c_index[node.c].append(node)

    for key in c_index:
        c_index[key].sort(key=lambda node: node.j)

    return c_index


def graph_complexity(pa):
    pa.c_index = create_c_index(pa)
    graph_complexity = math.log(len(pa.nodes) - 1) * (len(pa.nodes) - 1)
    normalize = graph_complexity
    for i in list(pa.c_index.keys())[1:]:
        e = len(pa.c_index[i])
        graph_complexity -= math.log(e) * e

    return graph_complexity, (graph_complexity / normalize)


def log_complexity(pa, forgetting=None, k=1):
    pa.c_index = create_c_index(pa)
    normalize = sum([len(AT.sequence) for AT in flatten(pa.activity_types.values())])
    normalize = normalize * math.log(normalize)
    if not forgetting:
        length = 0
        for AT in flatten(pa.activity_types.values()):
            length += len(AT.sequence)
        log_complexity = math.log(length) * length
        for i in list(pa.c_index.keys())[1:]:
            e = sum([len(AT.sequence) for AT in pa.c_index[i]])
            log_complexity -= math.log(e) * e

        return log_complexity, (log_complexity / normalize)
    elif forgetting == "linear":
        last_timestamp = pa.get_last_timestamp()
        timespan = pa.get_timespan()
        log_complexity_linear = 0
        for AT in flatten(pa.activity_types.values()):
            for event in AT.sequence:
                log_complexity_linear += (
                    1 - (last_timestamp - event.timestamp).total_seconds() / timespan
                )

        log_complexity_linear = math.log(log_complexity_linear) * log_complexity_linear

        for i in list(pa.c_index.keys())[1:]:
            e = 0
            for AT in pa.c_index[i]:
                for event in AT.sequence:
                    e += (
                        1
                        - (last_timestamp - event.timestamp).total_seconds() / timespan
                    )
            log_complexity_linear -= math.log(e) * e

        return log_complexity_linear, (log_complexity_linear / normalize)

    elif forgetting == "exp":
        last_timestamp = pa.get_last_timestamp()
        timespan = pa.get_timespan()
        log_complexity_exp = 0
        for AT in flatten(pa.activity_types.values()):
            for event in AT.sequence:
                log_complexity_exp += math.exp(
                    (-(last_timestamp - event.timestamp).total_seconds() / timespan) * k
                )

        log_complexity_exp = math.log(log_complexity_exp) * log_complexity_exp

        for i in list(pa.c_index.keys())[1:]:
            e = 0
            for AT in pa.c_index[i]:
                for event in AT.sequence:
                    e += math.exp(
                        (-(last_timestamp - event.timestamp).total_seconds() / timespan)
                        * k
                    )
            log_complexity_exp -= math.log(e) * e
        return log_complexity_exp, (log_complexity_exp / normalize)
    else:
        return None, None

def complexity(path):
    pm4py_log = generate_pm4py_log(path)
    log = generate_log(pm4py_log)
    epa = build_graph(log)

    var_ent = graph_complexity(epa)
    seq_ent = log_complexity(epa)
    seq_ent_lin = log_complexity(epa, "linear")
    seq_ent_exp = log_complexity(epa, "exp")

    results = {
        "variant_entropy": var_ent[0],
        "normalized_variant_entropy": var_ent[1],
        "sequence_entropy": seq_ent[0],
        "normalized_sequence_entropy": seq_ent[1],
        "sequence_entropy_linear_forgetting": seq_ent_lin[0],
        "normalized_sequence_entropy_linear_forgetting": seq_ent_lin[1],
        "sequence_entropy_exponential_forgetting": seq_ent_exp[0],
        "normalized_sequence_entropy_exponential_forgetting": seq_ent_exp[1],
    }
    return results
