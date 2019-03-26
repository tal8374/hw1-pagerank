import csv
from pprint import pprint

from Graph import Graph

graph = Graph()


def load_graph(path: str) -> None:
    index = 0

    with open(path) as file:
        reader = csv.reader(file)  # Wikipedia_votes.csv
        for row in reader:
            index += 1
            graph.add(row[0], row[1])

            # if index == 30000:
            #     break
        print('node count %d' % len(graph._graph.keys()))


def calculate_page_rank():
    graph.calculate_page_rank()
    # print(graph)

def get_PageRank(node_name):
    return graph.get_PageRank(node_name)

def Get_top_nodes(n):
    return graph.Get_top_nodes(n)


def get_all_PageRank():
    return graph.get_all_PageRank()


#load_graph('Wikipedia_votes.csv')
# load_graph('el_d_tmp_rt.csv')
load_graph('facebook_combined.csv')
#calculate_page_rank()
#print(Get_top_nodes(10))

# from pprint import pprint
#
# from Graph import Graph
#
# connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
#                    ('C', 'D'), ('E', 'F'), ('F', 'C')]
#
# g = Graph(connections, directed=True)
# pprint(g._graph)
