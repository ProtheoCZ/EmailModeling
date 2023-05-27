import networkx as nx
import matplotlib.pyplot as plt
import json


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


def plot_degree_distribution(G):
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

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.xlabel('Degree')
    plt.ylabel('Count')
    plt.title('Degree Distribution')
    plt.show()


def degree_distribution(graph_name):
    json_graph = json_loader(graph_name)
    graph = json_to_nx(json_graph)
    plot_degree_distribution(graph)


degree_distribution('editedGraph.json')
