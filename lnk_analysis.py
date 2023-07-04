import json
import os

PATH = 'c:/Users/Tomas/PycharmProjects/emailModelingBe/fullSimStats0/Sim_013/'

def runs_over_thresholds(path, threshold1, threshold2):
    thresholds1_count = 0
    tresholds2_count = 0

    max_graph_size = 0
    max_graph_id = 0

    for file in os.listdir(path):
        if file != 'Summary.json':
            with open(path + file) as f:
                result = json.load(f)
                node_count = result["full_graph_stats"]["node_count"]

                if node_count >= threshold1:
                    thresholds1_count += 1
                if node_count >= threshold2:
                    tresholds2_count += 1

                if node_count > max_graph_size:
                    max_graph_size = node_count
                    max_graph_id = result['run_id']

    print('max graph size: ' + str(max_graph_size) + ' id: ' + str(max_graph_id))
    print('number of graphs over ' + str(threshold1) + ': ' + str(thresholds1_count))
    print('number of graphs over ' + str(threshold2) + ': ' + str(tresholds2_count))


runs_over_thresholds(PATH, 100, 300)