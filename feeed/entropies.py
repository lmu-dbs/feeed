import os
import subprocess


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

def entropies(path):
    single_args = ["-f", "-p", "-B", "-z"]
    double_args = ["-d", "-r"]

    entrops = []
    for arg in single_args:
        entrops.append(default_call(path, arg, "", ""))
    for arg in double_args:
        for i in ["1", "3", "5"]:
            entrops.append(default_call(path, arg, i, ""))
    for i in ["3", "5", "7"]:
        entrops.append(default_call(path, "-k", i, "1"))

    results ={
			"entropy_trace": entrops[0],
			"entropy_prefix": entrops[1],
			"entropy_global_block": entrops[2],
			"entropy_lempel_ziv": entrops[3],
			"entropy_k_block_diff_1": entrops[4],
			"entropy_k_block_diff_3": entrops[5],
			"entropy_k_block_diff_5": entrops[6],
			"entropy_k_block_ratio_1": entrops[7],
			"entropy_k_block_ratio_3": entrops[8],
			"entropy_k_block_ratio_5": entrops[9],
			"entropy_knn_3": entrops[10],
			"entropy_knn_5": entrops[11],
			"entropy_knn_7": entrops[12]
			}
    return results
