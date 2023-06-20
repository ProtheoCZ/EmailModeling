import json
import random

import matplotlib.pyplot as plt
import networkx as nx


def load_dimacs(filename, skip_first_two_lines=True):
    with open(filename) as file:
        graph = nx.Graph()
        counter = 0
        for line in file:
            counter += 1
            if skip_first_two_lines:
                if counter >= 3:
                    temp_arr = line.split()
                    graph.add_edge(temp_arr[0], temp_arr[1])
            else:
                temp_arr = line.split()
                graph.add_edge(temp_arr[0], temp_arr[1])
            if counter % 1000 == 0:
                print(str(counter) + " edges read")
    return graph


def generate_barabasi_albert_graph(n, m, filename):
    graph = nx.barabasi_albert_graph(n, m)
    nx.write_gexf(graph, filename, version="1.2draft")


def set_graph_attributes(g, filename):
    if isinstance(g, nx.Graph):
        counter = 0
        with open(filename, encoding="utf8") as file:
            for line in file:
                attributes_arr = line.split('\t')
                node_id = attributes_arr[0]
                gender = attributes_arr[3]
                # region = attributes_arr[4]
                age = attributes_arr[7]
                if age == 'null' or age is None:
                    age = 0

                attributes_dict = {
                    node_id:
                        {
                            "attributes": {
                                "gender": gender,
                                # "region": region,
                                "age": age
                            }
                        }
                }
                nx.set_node_attributes(g, attributes_dict)
                counter += 1
                if counter % 1000 == 0:
                    print(str(counter) + " nodes had their attrs set")


def reduce_network_size(g, node_count):
    if isinstance(g, nx.Graph):
        start_node_id = str(random.randint(1, g.number_of_nodes()))
        start_node = g.nodes[start_node_id]
        ret_graph = nx.Graph()
        ret_graph.add_node(
            start_node_id,
            # x=start_node['x'],
            # y=start_node['y'],
            # size=start_node['size'],
            # displayed_color=start_node['color'],
            # label=start_node['label'],
            # id=start_node_id,
            age=start_node['age'],
            gender=start_node['gender']
        )

        node_queue = [start_node_id]
        current_node_idx = 0
        edge_id = 1
        while ret_graph.number_of_nodes() < node_count:
            current_node = node_queue[current_node_idx]
            current_node_idx += 1
            for node in g.neighbors(current_node):
                node_queue.append(node)
                node_to_add = g.nodes[current_node]
                ret_graph.add_node(
                    node,
                    # x=node_to_add['x'],
                    # y=node_to_add['y'],
                    # size=node_to_add['size'],
                    # displayed_color=node_to_add['color'],
                    # label=node_to_add['label'],
                    # id=node,
                    age=node_to_add['age'],
                    gender=node_to_add['gender']
                )

                ret_graph.add_edge(current_node,
                                   node,
                                   displayed_color='rgb(0,0,0)',
                                   size=1,
                                   id=edge_id
                                   )
                edge_id += 1

        return ret_graph


def generate_full_graph(size):
    G = nx.complete_graph(size)
    nx.write_gexf(G, "full_graph.gexf")


G = load_dimacs('soc-pokec/soc-pokec-relationships.txt', False)
print("graph loaded")
set_graph_attributes(G, 'soc-pokec/soc-pokec-profiles.txt')

for i in range(1):
    graph = reduce_network_size(G, 300000)
    print("network size reduced")
    nx.write_gexf(graph, "test/soc-pokec-relationships_" + str(i) + ".gexf", version="1.2draft")
    print("network # " + str(i) + " written")

# generate_barabasi_albert_graph(20000, 1, "barabasi-albert_test.gexf")
