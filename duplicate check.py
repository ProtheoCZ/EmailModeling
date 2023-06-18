

nodes = []
line_no = 0
with open('soc-pokec/soc-pokec-relationships.txt') as file:
    for line in file:
        line_no += 1
        temp_array = line.split()
        for node in temp_array:
            if node not in nodes:
                nodes.append(node)
        if line_no % 100000 == 0:
            print(str(line_no))
print("nodes: " + str(len(nodes)) + " lines: " + str(line_no))