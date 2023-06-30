import json

# nodes = []
# edges = []
# line_no = 0
# with open('email-EuAll.txt') as file:
#     for line in file:
#         line_no += 1
#         temp_array = line.split()
#         for node in temp_array:
#             if node not in nodes:
#                 nodes.append(node)
#
#         if [temp_array[0], temp_array[1]] not in edges and [temp_array[1], temp_array[0]] not in edges:
#             edges.append(temp_array)
#         if line_no % 100000 == 0:
#             print(str(line_no))
#
# print("nodes: " + str(len(nodes)) + " lines: " + str(line_no))
# print("edges: " + str(len(edges)))


with open('c:/Users/Tomas/PycharmProjects/emailModelingBe/graphData/emailEuCore.json') as json_file:
    json_graph = json.load(json_file)
    print(len(json_graph['edges']))
