import json
import os

import numpy as np
from matplotlib import pyplot as plt

GW_PATH = 'c:/Users/Tomas/PycharmProjects/emailModelingBe/fullSimStatsGw/Sim_008/'
WIDTH = 'width'
MEDIAN_NODE_DEPTH = 'median_node_depth'


def merge_columns(unconditional_attrs):
    merged_columns = [0 for _ in range(round(max(unconditional_attrs)/50)+1)]
    ret_attrs = []
    for value in unconditional_attrs:
        merged_columns[round(value / 50)] += 1

    for i in range(len(merged_columns)):
        for j in range(merged_columns[i]):
            ret_attrs.append(i*50)

    return ret_attrs


def plot_stats(gw_path, attr_name):
    unconditional_attrs = []
    conditional_attrs = []

    for file in os.listdir(gw_path):
        if file != 'Summary.json':
            with open(gw_path + file) as f:
                gw_stats = json.load(f)
                node_count = gw_stats["tree_result_stats"]["node_count"]
                unconditional_attrs.append(gw_stats["tree_result_stats"][attr_name])

                if 2442 <= node_count <= 3250:
                    conditional_attrs.append(gw_stats["tree_result_stats"][attr_name])
                    # print(file + ' ' + str(gw_stats["tree_result_stats"]["width"]))

    merged_columns = merge_columns(unconditional_attrs)

    # print(str(len(conditional_attrs)))
    # print(str(len(set(conditional_attrs))))
    # conditional_attrs.sort()
    # print(conditional_attrs)

    print(str(len(merged_columns)))
    print(str(len(set(merged_columns))))
    merged_columns.sort()
    print(merged_columns)


    # bin_width = 10
    # num_bins =int((max(unconditional_attrs) - min(unconditional_attrs)) / bin_width)

    # plt.ylim(plt.ylim()[0], plt.ylim()[1])

    plt.xlim(0, 2000)
    plt.hist(merged_columns, bins=62)


    # print(max(unconditional_attrs))

    plt.xlabel('Medián hloubky vrcholů stromu')
    plt.ylabel('Počet stromů s danoým mediánem hloubky stromu')
    plt.title('Histogram mediánu hloubek všech stromů')
    plt.show()


def get_gw_stats(gw_path):
    node_counts = []
    node_counts_over_2442 = []
    node_counts_between_2442_and_3250 = []

    widths = []
    widths_over_2442 = []
    widths_between_2442_and_3250 = []

    median_node_depths = []
    median_node_depths_over_2442 = []
    median_node_depths_between_2442_and_3250 = []

    for file in os.listdir(gw_path):
        if file != 'Summary.json':
            with open(gw_path + file) as f:
                gw_stats = json.load(f)
                node_count = gw_stats["tree_result_stats"]["node_count"]
                node_counts.append(node_count)

                width = gw_stats["tree_result_stats"]["width"]
                widths.append(width)

                median_node_depth = gw_stats["tree_result_stats"]["median_node_depth"]
                median_node_depths.append(median_node_depth)

                if node_count >= 2442:
                    node_counts_over_2442.append(node_count)
                    widths_over_2442.append(width)
                    median_node_depths_over_2442.append(median_node_depth)

                if 2442 <= node_count <= 3250:
                    node_counts_between_2442_and_3250.append(node_count)
                    widths_between_2442_and_3250.append(width)
                    median_node_depths_between_2442_and_3250.append(median_node_depth)

    width_count_over_threshhold = 0
    for width in widths_between_2442_and_3250:
        if 12 < width < 16:
            width_count_over_threshhold += 1

    median_node_depth_count_over_threshhold = 0
    for median_node_depth in median_node_depths_between_2442_and_3250:
        if 199 < median_node_depth < 301:
            median_node_depth_count_over_threshhold += 1


    print('number of graphs over 2442: ' + str(len(node_counts_over_2442)))
    print('number of graphs between 2442 and 3250: ' + str(len(node_counts_between_2442_and_3250)))
    print("node count percentage over 2442: " + str(len(node_counts_over_2442)/len(node_counts)))
    print("node count percentage between 2442 and 3250: " + str(len(node_counts_between_2442_and_3250)/len(node_counts)))

    print('width count over threshold: ' + str(width_count_over_threshhold))

    print('median node depth over threshold: ' + str(median_node_depth_count_over_threshhold))

    print('max node count: ' + str(max(node_counts)))
    print('max width: ' + str(max(widths)))
    print('max median node depth: ' + str(max(median_node_depths)))







get_gw_stats(GW_PATH)

plot_stats(GW_PATH, MEDIAN_NODE_DEPTH)