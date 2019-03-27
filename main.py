import csv

from Graph import Graph

graph = Graph()


def load_graph(path: str) -> None:
    index = 0

    with open(path) as file:
        reader = csv.reader(file)  # Wikipedia_votes.csv

        index = 0

        for row in reader:

            # if index == 20000:
            #     break
            index += 1

            graph.add(row[0], row[1])


def calculate_page_rank():
    graph.calculate_page_rank()
    # print(graph)


def get_PageRank(node_name):
    return graph.get_PageRank(node_name)


def Get_top_nodes(n):
    return graph.Get_top_nodes(n)


def get_all_PageRank():
    return graph.get_all_PageRank()


# load_graph('Wikipedia_votes.csv')
load_graph('el_d_tmp_rt.csv')
# load_graph('facebook_combined.csv')
calculate_page_rank()
# print(get_all_PageRank())
print(Get_top_nodes(10))


