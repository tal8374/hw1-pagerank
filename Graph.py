from collections import defaultdict

from Node import Node


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self):
        self._graph = defaultdict(set)

    def calculate_page_rank(self, epsilone=0.001, beta=0.85):
        """
        Responsible for calculating the page rank for each node.
        Starting with initilazing th page rank (1/N)
        Running and calculating the page rank for each iteration untill or reached to 20 iterations or the sub between
        sum the sub the old rank and the new is less than epsilone
        :param epsilone:
        :param beta:
        :return:
        """
        self.set_init_rank()

        self.set_loop_rank(epsilone, beta)

    def set_loop_rank(self, epsilone=0.001, beta=0.85):
        """
        The main loop of the algorithm
        :param epsilone:
        :param beta:
        :return:
        """
        iteration_number = 0
        while self.is_not_done_ranking(epsilone, iteration_number):
            # print(iteration_number)
            iteration_number += 1
            self.reset_temp_rank()
            self.do_rank(beta)
            self.restore_leaked_score()

    def restore_leaked_score(self):
        """
        The spider trap prevention method
        :return:
        """

        s = sum([node.temp_rank for node in self._graph.keys()])

        for node in self._graph.keys():
            if node.old_rank is None:
                pass
            else:
                node.prev_rank = node.old_rank

            node.old_rank = node.temp_rank + ((1 - s) / len(self._graph.keys()))

    def reset_temp_rank(self):
        for node in self._graph.keys():
            node.temp_rank = 0

    def do_rank(self, beta=0.85):
        """
        'spreading' node's rank to it's neighbours
        :param beta:
        :return:
        """
        for node in self._graph.keys():
            for neighbour in self._graph[node]:
                if neighbour.temp_rank is None:  # if it is the first time
                    neighbour.temp_rank = beta * (node.prev_rank / len(self._graph[node]))
                else:
                    neighbour.temp_rank += beta * (node.prev_rank / len(self._graph[node]))

    def is_not_done_ranking(self, epsilone, iteration_number):
        """
        boolean method that determin if the algorithm is done
        :param epsilone:
        :param iteration_number:
        :return:
        """
        sum_ranks = 0

        for node in self._graph.keys():

            if node.temp_rank is None:
                return True

            sum_ranks += abs(node.temp_rank - node.prev_rank)
        return sum_ranks > epsilone and iteration_number < 20

    def set_init_rank(self):
        """
        set the 1/N rank to all the nodes
        :return:
        """
        for node in self._graph.keys():
            node.prev_rank = 1 / (len(self._graph.keys()))

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        node1 = self.get_or_create(node1)
        node2 = self.get_or_create(node2)

        self._graph[node1].add(node2)

    def get_or_create(self, node_id):
        """
        adding nodes to the graph - private method
        :param node_id:
        :return:
        """
        for node in self._graph.keys():
            if node.str_id == node_id:
                return node

        return Node(node_id)

    def get_neighbors(self, node):
        """
        return the neighbours of node
        :param node:
        :return:
        """
        return self._graph[node]

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def get_PageRank(self, node_name):
        """
        public method that return the pagerank of a node
        :param node_name:
        :return:
        """
        for node in self._graph.keys():
            if node.str_id == node_name:
                return node.old_rank
        return -1

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    #
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def _by_rank(self, node):
        return node.old_rank

    def Get_top_nodes(self, n):
        """
        :param n:
        :return: list of (id, rank) of the top n nodes by the PageRank sorted in descending order
        """
        nodes = list(self._graph.keys())
        nodes.sort(key=self._by_rank, reverse=True)
        nodes = [(node.str_id, node.old_rank) for node in nodes]

        return nodes[:n]

    def get_all_PageRank(self):
        """

        :return: list of (id, rank) of all the nodes ordered by PageRank in descending order
        """
        return [(node.str_id, node.old_rank) for node in list(self._graph.keys())]
