import json

import matplotlib.pyplot as plt
import networkx as nx
import os

def load_site():
    pass


def add_node_params():
    pass
    # output/input trust, dict s neighbor nodes


def load_dimacs(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    graph = nx.Graph()
    counter = 0
    for line in lines:
        counter += 1
        if counter >= 3:
            temp_arr = line.split()
            graph.add_edge(temp_arr[0], temp_arr[1])
    return graph

def generate_barabasi_albert_graph(n, m, filepath):
    graph = nx.barabasi_albert_graph(n, m)
    json_graph = networkx_to_json(graph)
    out_file = open(filepath, "w")
    json.dump(json_graph, out_file)

def networkx_to_json(graph):
    #Todo rewrite
    ret_json = {
        "nodes": [],
        "edges": []
    }
    for node in graph.nodes:
        # print(node)
        json_node = {
            "label": graph.nodes[node]["label"],
            "x": graph.nodes[node]["x"],
            "y": graph.nodes[node]["y"],
            "id": graph.nodes[node]["id"],
            "attributes": {},
            "color": graph.nodes[node]["displayed_color"],
            "size": graph.nodes[node]["size"]
        }
        ret_json["nodes"].append(json_node)

    for edge in graph.edges:
        # print(edge[0])
        # print(edge)
        json_edge = {
            "source": edge[0],
            "target": edge[1],
            "id": graph.edges[edge]["id"],
            "attributes": {},
            "color": graph.edges[edge]["displayed_color"],
            "size": graph.edges[edge]["size"],
        }
        ret_json["edges"].append(json_edge)

    return ret_json

# G = nx.Graph()
# G.add_nodes_from([1, 2, 3, 4, 5])
# G.add_edges_from([(3, 2), (2, 3), (2, 4), (4, 5), (1, 4), (1, 2)])
# print(G.number_of_edges(), G.number_of_nodes())
# print(list(G.nodes))
# print(list(G.edges))
# nx.set_node_attributes(G, {2: "red", 1: "blue"}, name="color")
# print(nx.get_node_attributes(G, 'color')[2])


# G = load_dimacs('C125-9.mtx')
# nx.draw_networkx(G, None, True, True)
# plt.show()
