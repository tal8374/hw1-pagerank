# https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
import math
from collections import defaultdict

from Node import Node


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self):
        self._graph = defaultdict(set)

    #     self.add_connections(connections)
    #
    # def add_connections(self, connections) -> None:
    #     """
    #
    #     :param connections: The entire edge list
    #     :return: None
    #     """
    #
    #     for node1, node2 in connections:
    #         self.add(Node(node1), Node(node2))

    def calculate_page_rank(self, epsilone=0.001, beta=0.85):
        self.set_init_rank()

        self.set_loop_rank(epsilone, beta)

    def set_loop_rank(self, epsilone=0.001, beta=0.85):
        iteration_number = 0
        while self.is_not_done_ranking(epsilone, iteration_number):
            print(iteration_number)
            iteration_number += 1
            self.temp_to_old_rank()
            self.reset_temp_rank()
            self.do_rank(beta)

    def temp_to_old_rank(self):
        for node in self._graph.keys():
            if node.temp_rank is None:
                continue

            node.old_rank = node.temp_rank

    def reset_temp_rank(self):
        for node in self._graph.keys():
            node.temp_rank = 0

    def do_rank(self, beta=0.85):
        for node in self._graph.keys():
            # if len(self._graph[node]) == 0:  # if in-deg == 0
            #     node.temp_rank = 0
            for neighbour in self._graph[node]:
                if neighbour.temp_rank is None:  # if it is the first time
                    neighbour.temp_rank = beta * (node.old_rank / len(self._graph[node]))
                else:
                    neighbour.temp_rank += beta * (node.old_rank / len(self._graph[node]))

    def is_not_done_ranking(self, epsilone, iteration_number):
        sum_ranks = 0

        for node in self._graph.keys():

            if node.temp_rank is None:
                return True

            sum_ranks += abs(node.temp_rank - node.old_rank)
        print(sum_ranks)
        return sum_ranks > epsilone and iteration_number < 20  # and sum_ranks != float("inf")

    def set_init_rank(self):
        for node in self._graph.keys():
            node.old_rank = 1 / (len(self._graph.keys()))

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        node1 = self.get_or_create(node1)
        node2 = self.get_or_create(node2)

        self._graph[node1].add(node2)

    def get_or_create(self, node_id):
        for node in self._graph.keys():
            if node.str_id == node_id:
                return node

        return Node(node_id)

    def get_neighbors(self, node):
        return self._graph[node]

    # def remove(self, node):
    #     """ Remove all references to node """
    #
    #     for n, cxns in self._graph.iteritems():
    #         try:
    #             cxns.remove(node)
    #         except KeyError:
    #             pass
    #     try:
    #         del self._graph[node]
    #     except KeyError:
    #         pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    # def find_path(self, node1, node2, path=[]):
    #     """ Find any path between node1 and node2 (may not be shortest) """
    #
    #     path = path + [node1]
    #     if node1 == node2:
    #         return path
    #     if node1 not in self._graph:
    #         return None
    #     for node in self._graph[node1]:
    #         if node not in path:
    #             new_path = self.find_path(node, node2, path)
    #             if new_path:
    #                 return new_path
    #     return None

    def get_PageRank(self, node_name):
        for node in self._graph.keys():
            if node.str_id == node_name:
                return node.old_rank
        return -1

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    #
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def by_rank(self, node):
        return node.old_rank

    def Get_top_nodes(self, n):
        nodes = list(self._graph.keys())
        nodes.sort(key=self.by_rank, reverse=True)
        nodes = [(node.str_id, node.old_rank) for node in nodes]

        return nodes[:n]

    def get_all_PageRank(self):
        return [(node.str_id, node.old_rank) for node in list(self._graph.keys())]
