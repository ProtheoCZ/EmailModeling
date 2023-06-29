import json
import os
from statistics import median

RESULT_FOLDER_PATH_DEFAULT = '../emailModelingBe/fullSimStats'
RESULT_FOLDER_PATH_F = 'f:/emailModelingSimDataArchive/rumor spread emaileu core - lambda = rozhodne souhlasi/'
RESULT_FOLDER_PATH0 = '../emailModelingBe/fullSimStats0'
RESULT_FOLDER_PATH1 = '../emailModelingBe/fullSimStats1'
RESULT_FOLDER_PATH2 = '../emailModelingBe/fullSimStats2'
RESULT_FOLDER_PATH3 = '../emailModelingBe/fullSimStats3'
RESULT_FOLDER_PATH4 = '../emailModelingBe/fullSimStats4'
RESULT_FOLDER_PATH5 = '../emailModelingBe/fullSimStats5'


def add_median_node_stat(result_folder_path):
    # result_folder_path = '../emailModelingBe/fullSimStats0'

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


add_median_node_stat(RESULT_FOLDER_PATH3)
