import json

import matplotlib.pyplot as plt
import networkx as nx
from fa2 import ForceAtlas2


def add_node_params(site):
    pass
    # output/input trust, dict s neighbor nodes


def load_dimacs(filename, skip_first_two_lines=True):
    with open(filename) as file:
    # file = open(filename, 'r')
    # lines = file.readlines()
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
                        "gender": gender,
                         # "region": region,
                         "age": age
                         }
                }
                nx.set_node_attributes(g, attributes_dict)
                counter += 1
                if counter % 1000 == 0:
                    print(str(counter) + " nodes had their attrs set")


# G = nx.Graph()
# G.add_nodes_from([1, 2, 3, 4, 5])
# G.add_edges_from([(3, 2), (2, 3), (2, 4), (4, 5), (1, 4), (1, 2)])
# print(G.number_of_edges(), G.number_of_nodes())
# print(list(G.nodes))
# print(list(G.edges))
# nx.set_node_attributes(G, {2: "red", 1: "blue"}, name="color")
# print(nx.get_node_attributes(G, 'color')[2])

# forceatlas2 = ForceAtlas2(
#                         # Behavior alternatives
#                         outboundAttractionDistribution=True,  # Dissuade hubs
#                         linLogMode=False,  # NOT IMPLEMENTED
#                         adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
#                         edgeWeightInfluence=1.0,
#
#                         # Performance
#                         jitterTolerance=1.0,  # Tolerance
#                         barnesHutOptimize=True,
#                         barnesHutTheta=1.2,
#                         multiThreaded=False,  # NOT IMPLEMENTED
#
#                         # Tuning
#                         scalingRatio=2.0,
#                         strongGravityMode=False,
#                         gravity=1.0,
#
#                         # Log
#                         verbose=True)

G = load_dimacs('soc-pokec/soc-pokec-relationships.txt', False)
print("graph loaded")
set_graph_attributes(G, 'soc-pokec/soc-pokec-profiles.txt')

# print(nx.nodes(G))
# positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=2000)
nx.write_gexf(G, "test/soc-pokec-relationships.gexf", version="1.2draft")

# nx.draw_networkx(G, None, True, True)
# plt.show()

# generate_barabasi_albert_graph(20000, 1, "barabasi-albert_test.gexf")
