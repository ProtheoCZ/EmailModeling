import json
import os


def find_largest_run(sim_path):
    runs = os.listdir(sim_path)
    max_node_count = 0
    largest_run_name = ""
    for file in runs:
        if file != "Summary.json":
            with open(sim_path + '/' + file) as run_file:
                json_file = json.load(run_file)
                if json_file['full_graph_stats']['node_count'] + json_file['full_graph_stats']['group_reply_node_count'] > max_node_count:
                    max_node_count = json_file['full_graph_stats']['node_count'] + json_file['full_graph_stats']['group_reply_node_count']
                    largest_run_name = file

    print("largest run is " + largest_run_name + " with " + str(max_node_count) + " nodes")
    return largest_run_name


find_largest_run("c:/Users/Tomas/PycharmProjects/emailModelingBe/fullSimStats/Sim_049")

