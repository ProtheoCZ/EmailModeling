import json
import os

import numpy as np
from matplotlib import pyplot as plt

GW_PATH = 'c:/Users/Tomas/PycharmProjects/emailModelingBe/fullSimStatsGw/Sim_008/'
WIDTH = 'width'
MEDIAN_NODE_DEPTH = 'median_node_depth'


def plot_stats(gw_path, attr_name):
    all_widths = []
    conditional_widths = []

    for file in os.listdir(gw_path):
        if file != 'Summary.json':
            with open(gw_path + file) as f:
                gw_stats = json.load(f)
                node_count = gw_stats["tree_result_stats"]["node_count"]
                all_widths.append(gw_stats["tree_result_stats"][attr_name])

                if 2442 <= node_count <= 3250:
                    conditional_widths.append(gw_stats["tree_result_stats"]["width"])
                    print(file + ' ' + str(gw_stats["tree_result_stats"]["width"]))

    print(str(len(conditional_widths)))
    print(str(len(set(conditional_widths))))
    print(conditional_widths)
    plt.hist(conditional_widths, bins=14, density=True)

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')

    plt.show()


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
                if node_count >= 2442:
                    node_counts_over_2442.append(node_count)
                if 2442 <= node_count <= 3250:
                    node_counts_between_2442_and_3250.append(node_count)

    print('number of graphs over 2442: ' + str(len(node_counts_over_2442)))
    print('number of graphs between 2442 and 3250: ' + str(len(node_counts_between_2442_and_3250)))
    print("node count percentage over 2442: " + str(len(node_counts_over_2442)/len(node_counts)))
    print("node count percentage between 2442 and 3250: " + str(len(node_counts_between_2442_and_3250)/len(node_counts)))



get_gw_stats(GW_PATH)


plot_stats(GW_PATH, WIDTH)