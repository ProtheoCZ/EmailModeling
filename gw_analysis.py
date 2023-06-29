import json
import os

GW_PATH = 'c:/Users/Tomas/PycharmProjects/emailModelingBe/fullSimStatsGw/Sim_004/'


def get_gw_stats(gw_path):
    node_counts = []
    node_counts_over_2442 = []
    node_counts_between_2442_and_3250 = []
    for file in os.listdir(gw_path):
        if file != 'Summary.json':
            with open(gw_path + file) as f:
                gw_stats = json.load(f)
                node_count = gw_stats["tree_result_stats"]["node_count"]
                node_counts.append(node_count)
                if node_count > 2442:
                    node_counts_over_2442.append(node_count)
                if 2442 <= node_count <= 3250:
                    node_counts_between_2442_and_3250.append(node_count)

    print("node count percentage over 2442: " + str(len(node_counts_over_2442)/len(node_counts)))
    print("node count percentage between 2442 and 3250: " + str(len(node_counts_between_2442_and_3250)/len(node_counts)))


get_gw_stats(GW_PATH)
