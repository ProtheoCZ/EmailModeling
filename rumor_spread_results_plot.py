import json
import os
import pandas as pd
import seaborn as sns
import random

from matplotlib import pyplot as plt

AVG_NODE_COUNT = "avg_node_count"
MEDIAN_NODE_COUNT = "median_node_count"
AVG_PATH_LENGTH = "avg_path_length"
AVG_PATH_LENGTH_FROM_START = "avg_path_length_from_start"
MAX_NODE_COUNT = "max_node_count"

RESULT_FOLDER_PATH_DEFAULT = '../emailModelingBe/fullSimStats'
RESULT_FOLDER_PATH_F = 'f:/emailModelingSimDataArchive/rumor spread emaileu core - lambda = rozhodne souhlasi/'
RESULT_FOLDER_PATH0 = '../emailModelingBe/fullSimStats0'
RESULT_FOLDER_PATH1 = '../emailModelingBe/fullSimStats1'
RESULT_FOLDER_PATH2 = '../emailModelingBe/fullSimStats2'
RESULT_FOLDER_PATH3 = '../emailModelingBe/fullSimStats3'
RESULT_FOLDER_PATH4 = '../emailModelingBe/fullSimStats4'
RESULT_FOLDER_PATH5 = '../emailModelingBe/fullSimStats5'
TIME_EVOLUTION_RESULT_FOLDER_PATH = '../emailModelingBe/rumourTimeEvolution/Sim_007/'
TIME_EVOLUTION_FILE_NAME = 'd01a03.json'
TIME_EVOLUTION_MAX_FILE_NAME = 'd01a03_max.json'



def plot_heat_map(param_name, result_folder_path, graph_size):
    delta_values = [round(delta, 1) for delta in list(pd.np.arange(0.1, 1.1, 0.1))]
    alfa_values = [round(alfa, 1) for alfa in list(pd.np.arange(0.1, 1.1, 0.1))]

    df = pd.DataFrame(0.1, index=delta_values, columns=alfa_values)

    folder_id = 0
    for i in range(10):
        for j in range(10):
            alfa = round((0.1 * j)+0.1, 1)
            delta = round((0.1 * i) + 0.1, 1)
            folder = os.listdir(result_folder_path)[folder_id]
            folder_id += 1

            current_summary_path = result_folder_path + '/' + folder + '/Summary.json'

            with open(current_summary_path) as file:
                summary = json.load(file)
                node_count = round(summary["summary_graph_stats"][param_name], 1)
                df.at[delta, alfa] = node_count

    print(df)
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(df, vmin=0, vmax=200)
    ax.invert_yaxis()
    ax.set_xlabel('Pravděpodobnost změny stavu z šiřitele na potlačovatele - alfa')  # alfa
    ax.set_ylabel('Pravděpodobnost spontánního zastavení šíření  - delta')  # delta
    title = 'Heat map of ' + param_name.replace('_', ' ') + ' for different alfa and delta values (N = ' + str(graph_size) + ')'
    ax.set_title(title)
    # sns.set(font_scale=2.5)

    plt.show()


def plot_population_evolution(evolutions_file_path, run_count, is_max_run=False):
    if is_max_run:
        evolutions_file_path.replace('.json', '_max.json')
    with open(evolutions_file_path) as file:
        evolutions = json.load(file)
        if is_max_run:
            spreader_lens = evolutions["spreader_lens"]
            stifler_lens = evolutions["stifler_lens"]
        else:
            spreader_lens = [spreader_len/run_count for spreader_len in evolutions["spreader_lens"]]
            stifler_lens = [stifler_len/run_count for stifler_len in evolutions["stifler_lens"]]

        time = [i for i in range(len(spreader_lens))]

        delta = str(round(evolutions["cessation_chance"], 1))
        alfa = str(round(evolutions["spreader_to_stifler_chance"], 1))

        fig, ax = plt.subplots()
        ax.plot(time, spreader_lens)
        ax.set_xlim(left=0)
        ax.set_ylim(bottom=0)
        plt.xlabel('Čas')
        plt.ylabel('Počet šiřitelů')
        plt.title('Vývoj počtu šiřitelů v čase pro delta = ' + delta + ' a alfa = ' + alfa)

        plt.show()

        fig, ax = plt.subplots()
        ax.plot(time, stifler_lens)
        ax.set_xlim(left=0)
        ax.set_ylim(bottom=0)
        plt.xlabel('Čas')
        plt.ylabel('Počet potlačovatelů')
        plt.title('Vývoj počtu potlačovatelů v čase pro delta = ' + delta + ' a alfa = ' + alfa)
        plt.show()


# plot_heat_map(MAX_NODE_COUNT, RESULT_FOLDER_PATH3, 1000)
# plot_heat_map(AVG_NODE_COUNT, RESULT_FOLDER_PATH3, 1000)

plot_population_evolution(TIME_EVOLUTION_RESULT_FOLDER_PATH + TIME_EVOLUTION_FILE_NAME, 100)
# plot_population_evolution(TIME_EVOLUTION_RESULT_FOLDER_PATH + TIME_EVOLUTION_MAX_FILE_NAME, 100)
# plot_population_evolution(TIME_EVOLUTION_RESULT_FOLDER_PATH + 'd01a10.json', 100)





