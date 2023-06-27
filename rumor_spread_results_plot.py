import json
import os
import pandas as pd
import seaborn as sns
import random

from matplotlib import pyplot as plt

AVG_NODE_COUNT = "avg_node_count"
MEDIAN_NODE_COUNT = "median_node_count"


def plot_heat_map(param_name):
    delta_values = [round(delta, 1) for delta in list(pd.np.arange(0.0, 1.1, 0.1))]
    alfa_values = [round(alfa, 1) for alfa in list(pd.np.arange(0.0, 1.1, 0.1))]

    df = pd.DataFrame(0.0, index=delta_values, columns=alfa_values)

    result_folder_path = '../emailModelingBe/fullSimStats'
    folder_id = 0
    for i in range(11):
        for j in range(11):
            alfa = round(0.1 * j, 1)
            delta = round(0.1 * i, 1)
            folder = os.listdir(result_folder_path)[folder_id]
            folder_id += 1

            current_summary_path = result_folder_path + '/' + folder + '/Summary.json'

            with open(current_summary_path) as file:
                summary = json.load(file)
                node_count = round(summary["summary_graph_stats"][param_name], 1)
                df.at[delta, alfa] = node_count

    print(df)
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(df, vmin=0, vmax=500)
    ax.invert_yaxis()
    ax.set_xlabel('Spreader to stifler probability - alfa')  # alfa
    ax.set_ylabel('Cessation probability - delta')  # delta
    title = 'Heat map of ' + param_name.replace('_', ' ') + ' for different alfa and delta values'
    ax.set_title(title)
    # sns.set(font_scale=2.5)

    plt.show()


plot_heat_map(AVG_NODE_COUNT)

