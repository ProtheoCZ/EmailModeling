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


# G = nx.Graph()
# G.add_nodes_from([1, 2, 3, 4, 5])
# G.add_edges_from([(3, 2), (2, 3), (2, 4), (4, 5), (1, 4), (1, 2)])
# print(G.number_of_edges(), G.number_of_nodes())
# print(list(G.nodes))
# print(list(G.edges))
# nx.set_node_attributes(G, {2: "red", 1: "blue"}, name="color")
# print(nx.get_node_attributes(G, 'color')[2])


G = load_dimacs('C125-9.mtx')
nx.draw_networkx(G, None, True, True)
plt.show()
