import inspect
import os
import subprocess

from .feature import Feature

class Entropies(Feature):
    def __init__(self, feature_names='entropies'):
        self.feature_type="entropies"
        self.available_class_methods = dict(inspect.getmembers(Entropies, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [
                "entropy_trace",
                "entropy_prefix",
                "entropy_global_block",
                "entropy_lempel_ziv",
                "entropy_k_block_diff_1",
                "entropy_k_block_diff_3",
                "entropy_k_block_diff_5",
                "entropy_k_block_ratio_1",
                "entropy_k_block_ratio_3",
                "entropy_k_block_ratio_5",
                "entropy_knn_3",
                "entropy_knn_5",
                "entropy_knn_7"
                ]
        else:
            self.feature_names = feature_names

    def default_call(path, arg1, arg2, arg3):
        output = subprocess.run(
            [
                "java",
                "-jar",
                f"{os.getcwd()}/../feeed/feeed/eventropy.jar",
                arg1,
                arg2,
                arg3,
                f"{os.getcwd()}/{path}",
            ],
            capture_output=True,
            text=True,
        )
        try:
            if len(output.stdout) == 0:
                return 0
            return float(output.stdout.strip().split(":")[1])
        except ValueError:
            print(output.stdout)
            return 0

    @classmethod
    def entropy_trace(cls, log_path):
        return Entropies.default_call(log_path, "-f", "", "")

    @classmethod
    def entropy_prefix(cls, log_path):
        return Entropies.default_call(log_path, "-p", "", "")

    @classmethod
    def entropy_global_block(cls, log_path):
        return Entropies.default_call(log_path, "-B", "", "")

    @classmethod
    def entropy_lempel_ziv(cls, log_path):
        return Entropies.default_call(log_path, "-z", "", "")

    @classmethod
    def entropy_k_block_diff_1(cls, log_path):
        return Entropies.default_call(log_path, "-d", "1", "")

    @classmethod
    def entropy_k_block_diff_3(cls, log_path):
        return Entropies.default_call(log_path, "-d", "3", "")

    @classmethod
    def entropy_k_block_diff_5(cls, log_path):
        return Entropies.default_call(log_path, "-d", "5", "")

    @classmethod
    def entropy_k_block_ratio_1(cls, log_path):
        return Entropies.default_call(log_path, "-r", "1", "")

    @classmethod
    def entropy_k_block_ratio_3(cls, log_path):
        return Entropies.default_call(log_path, "-r", "3", "")

    @classmethod
    def entropy_k_block_ratio_5(cls, log_path):
        return Entropies.default_call(log_path, "-r", "5", "")

    @classmethod
    def entropy_knn_3(cls, log_path):
        return Entropies.default_call(log_path, "-k", "3", "1")

    @classmethod
    def entropy_knn_5(cls, log_path):
        return Entropies.default_call(log_path, "-k", "5", "1")

    @classmethod
    def entropy_knn_7(cls, log_path):
        return Entropies.default_call(log_path, "-k", "7", "1")
