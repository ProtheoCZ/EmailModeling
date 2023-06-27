import json
import os
from statistics import median


def add_median_node_stat():
    result_folder_path = '../emailModelingBe/fullSimStats'

    for folder in os.listdir(result_folder_path):
        node_counts = []
        for run in os.listdir(result_folder_path + '/' + folder):
            if run != 'Summary.json':
                with open(result_folder_path + '/' + folder + '/' + run) as file:
                    run_stats = json.load(file)
                    node_counts.append(run_stats["full_graph_stats"]["node_count"])

        median_node_count = median(node_counts)
        with open(result_folder_path + '/' + folder + '/Summary.json') as file:
            summary = json.load(file)
            summary["summary_graph_stats"]["median_node_count"] = median_node_count
            with open(result_folder_path + '/' + folder + '/Summary.json', 'w') as outfile:
                json.dump(summary, outfile, indent=4)


add_median_node_stat()
