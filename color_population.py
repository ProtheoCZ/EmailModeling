import json
import random

GRAPH_FOLDER = '../emailModelingBe/graphData/'


# www.irozhlas.cz/zpravy-domov/spolecnost-neduvery-informacni-datova-gramotnost-konspirace-dezinformace-vliv_2306140500_pik

# skupiny
'''
silni odpurci - 17%
mirni odpurci - 20%    
nezapojeni odpurci - 17%
apaticti - 6%
neco na tom je - 13%
mirni priznivci migrace - 10%
mirni priznivci covid - 12%
silni priznivci - 6%
'''


def color_population(graph_name):
    population_groups = ['opponent', 'neutral', 'supporter']
    population_group_distribution = \
        [17 + 20 + 17,
         6 + 13,
         10 + 12 + 6]

    with open(GRAPH_FOLDER + graph_name + '.json') as file:
        json_file = json.load(file)
        for node in json_file['nodes']:
            node['population_group'] = random.choices(population_groups, weights=population_group_distribution, k=1)[0]


        json.dump(json_file, open(GRAPH_FOLDER + graph_name + '_with_pop_groups.json', 'w'))


def population_distribution_check(graph_name):
    population_groups = ['opponent', 'neutral', 'supporter']
    population_group_distribution = \
        [17 + 20 + 17,
         6 + 13,
         10 + 12 + 6]

    with open(GRAPH_FOLDER + graph_name + '_with_pop_groups.json') as file:
        json_file = json.load(file)
        population_groups_count = [0, 0, 0]
        for node in json_file['nodes']:
            population_groups_count[population_groups.index(node['population_group'])] += 1

        print(population_groups_count)

        for i in range(len(population_groups_count)):
            population_groups_count[i] /= len(json_file['nodes'])

        print(population_groups_count)
        print(population_group_distribution)


color_population('emailEuCore')
population_distribution_check('emailEuCore')
