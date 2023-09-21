class UndirectedWeightedgraph:

    def __init__(self, iter_num=15):
        self.iter_num = iter_num
        self.graph = {}
        self.d = 0.85

    def add_edge(self, start_node, end_node, weight):
        if start_node not in self.graph:
            self.graph[start_node] = []
        if end_node not in self.graph:
            self.graph[end_node] = []
        self.graph[start_node].append((start_node, end_node, weight))
        self.graph[end_node].append((end_node, start_node, weight))

    def rank(self):
        node_ranks = {}
        node_edge_sum_weight = {}

        init_rank = 1.0 / (len(self.graph) or 1.0)
        for node, edges in self.graph.items():
            node_ranks[node] = init_rank
            node_edge_sum_weight[node] = sum((edge[2] for edge in edges))

        nodes = sorted(self.graph.keys())
        for iter_i in range(self.iter_num):
            for node in nodes:
                _sum = 0
                for (_, neighbor_node, weight) in self.graph[node]:
                    _sum += weight / node_edge_sum_weight[neighbor_node] * node_ranks[neighbor_node]
                node_ranks[node] = (1 - self.d) + self.d * _sum

        if node_ranks:
            max_rank = max(node_ranks.values())
            min_rank = min(node_ranks.values())
            for node, rank_val in node_ranks.items():
                node_ranks[node] = (rank_val - min_rank) / (max_rank - min_rank)


        # max_rank = max(node_ranks.values())
        # min_rank = min(node_ranks.values())
        # for node, rank_val in node_ranks.items():
        #     node_ranks[node] = (rank_val - min_rank / (max_rank - min_rank))

        return node_ranks


class Textrank:
    @staticmethod
    def _calculate_graph(elements_relation):
        graph = UndirectedWeightedgraph()

        for (word1, word2), freq in elements_relation.items():
            graph.add_edge(word1, word2, freq)

        nodes_rank = graph.rank()

        results = sorted(nodes_rank.items(), key=lambda item: item[1], reverse=True)
        return results

    def textrank(self, elements, window_size=3):

        elements_relation = {}

        for i, ele in enumerate(elements):
            for j in range(i + 1, min(i + window_size, len(elements))):
                term = (ele, elements[j])
                elements_relation[term] = elements_relation.get(term, 0) + 1

        result = self._calculate_graph(elements_relation)

        return result

c = UndirectedWeightedgraph()
c.rank()