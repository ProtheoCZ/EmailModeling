import json
import networkx as nx


def json_loader(json_graph_name):
    file = open(json_graph_name)
    json_file = json.load(file)
    print("graph loaded")
    return json_file


def json_to_nx(json_graph):
    graph = nx.Graph()

    for node in json_graph['nodes']:
        graph.add_node(
            node['id'],
            x=node['x'],
            y=node['y'],
            size=node['size'],
            displayed_color=node['color'],
            label=node['label'],
            id=node['id'],
            attributes={
                "age": node['attributes']['age'],
                "gender": node['attributes']['gender']
            }
        )

    for edge in json_graph['edges']:
        graph.add_edge(
            edge['source'],
            edge['target'],
            displayed_color=edge['color'],
            size=edge['size'],
            id=edge['id']
        )

    print("graph converted to nx")
    return graph


def set_age(graph):
    for node in graph.nodes:
        full_node = graph.nodes[node]
        if full_node['attributes']['age'] == "0" or full_node['attributes']['age'] == 0:
            sum_age = 0
            number_of_neighbors = 0
            for neighbor in graph.neighbors(node):
                sum_age += int(graph.nodes[neighbor]['attributes']['age'])
                number_of_neighbors += 1
            graph.nodes[node]['attributes']['age'] = round(sum_age/number_of_neighbors)
        else:
            graph.nodes[node]['attributes']['age'] = int(full_node['attributes']['age'])
    print("age_set")
    return graph


def nx_to_json(graph):
    ret_json = {
            "nodes": [],
            "edges": []
        }
    for node in graph.nodes:
        json_node = {
            "label": graph.nodes[node]["label"],
            "x": graph.nodes[node]["x"],
            "y": graph.nodes[node]["y"],
            "id": graph.nodes[node]["id"],
            "attributes": {
                "age": graph.nodes[node]["attributes"]["age"],
                "gender": graph.nodes[node]["attributes"]["gender"]
            },
            "color": graph.nodes[node]["displayed_color"],
            "size": graph.nodes[node]["size"]
        }
        ret_json["nodes"].append(json_node)

    for edge in graph.edges:
        json_edge = {
            "source": edge[0],
            "target": edge[1],
            "id": graph.edges[edge]["id"],
            "color": graph.edges[edge]["displayed_color"],
            "size": graph.edges[edge]["size"],
        }
        ret_json["edges"].append(json_edge)

    print("graph converted to json")
    return ret_json


def write_json_graph(json_graph):
    filename = 'soc-pokec_V4.json'
    with open(filename, "w") as json_file:
        json.dump(json_graph, json_file)

    print("graph written")


def compute_age():
    graph_name = 'soc-pokec_V2.json'
    json_graph = json_loader(graph_name)
    graph = json_to_nx(json_graph)
    graph = set_age(graph)
    json_graph = nx_to_json(graph)
    write_json_graph(json_graph)


compute_age()
