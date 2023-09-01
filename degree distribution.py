import networkx as nx
import matplotlib.pyplot as plt
import json

import numpy as np
from scipy.optimize import curve_fit


#code used for plotting degree distribution and approximating degree exponent

def json_loader(json_graph_name):
    file = open(json_graph_name)
    json_file = json.load(file)
    return json_file


def json_to_nx(json_graph):
    graph = nx.Graph()

    for node in json_graph['nodes']:
        graph.add_node(
            node['id'],
        )

    for edge in json_graph['edges']:
        graph.add_edge(
            edge['source'],
            edge['target'],
            id=edge['id']
        )
    return graph


def plot_degree_distribution(G, graph_name):
    degrees = [G.degree(node) for node in G.nodes()]
    degree_counts = dict()

    for degree in degrees:
        if degree in degree_counts:
            degree_counts[degree] += 1
        else:
            degree_counts[degree] = 1

    sorted_degrees = sorted(degree_counts.items())
    x = [degree for degree, count in sorted_degrees]
    y = [count for degree, count in sorted_degrees]

    normalized_cumulative_y_degree_counts = [(sum(y[i:]) / sum(y)) for i in range(len(y))]
    approximate_dist_func(x, normalized_cumulative_y_degree_counts)

    bins = np.logspace(np.log10(min(x)), np.log10(max(x)), num=20)  # log spaced bins
    x_binned = np.histogram(x, bins=bins)[0]
    y_binned = np.histogram(x, bins=bins, weights=y)[0] / x_binned

    plt.figure(figsize=(10, 6))
    plt.scatter(bins[:-1], y_binned)
    plt.xlabel('Stupeň vrcholu')
    plt.ylabel('Počet vrcholů')
    plt.title('Rozdělení stupňů vrcholů sítě ' + str(graph_name))

    plt.yscale('log')
    plt.xscale('log')

    plt.show()


# approximate degree exponent using curve fitting
def approximate_dist_func(x_points, y_points):
    def exponent_func(x, y):
        return x ** (-y)

    vals, _ = curve_fit(exponent_func, x_points, y_points)
    exponent = vals[0]
    print('degree exponent is roughly ' + str(exponent))


def degree_distribution(graph_path, graph_name):
    json_graph = json_loader(graph_path)
    graph = json_to_nx(json_graph)
    plot_degree_distribution(graph, graph_name)


degree_distribution('../emailModelingBe/graphData/EuAll.json', 'EuAll')
