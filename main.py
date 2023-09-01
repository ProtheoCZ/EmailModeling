import networkx as nx

#code for loading graphs in dimacs format

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


G = load_dimacs('email-Eu-core.txt', False)
print("graph loaded")
nx.write_gexf(G, "email-Eu-core.gexf", version="1.2draft")




