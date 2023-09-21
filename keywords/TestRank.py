



class UndirectedWeightedgraph():

    def __init__(self, iter_num=15):
        self.iter_num = iter_num
        self.graph = {}
        self.d = 0.85




    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = []
        if end not in self.graph:
            self.graph[end] = []
        self.graph[start].append((start, end, weight))
        self.graph[end].append((end, start, weight))



    def rank(self):
        node_ranks = {}
        node_edge_sum_weight = {}

        init_rank = 1.0 / (len(self.graph) or 1.0)
        for node, edges in self.graph.items():
            node_ranks[node] = init_rank
            node_edge_sum_weight[node] = sum([edge[2] for edge in edges])
        nodes = sorted(self.graph.keys())

        for iter_i in range(self.iter_num):
            for node in nodes:
                _sum = 0
                for (_,neighbor_node, weight) in self.graph[node]:
                    _sum += weight / node_edge_sum_weight[neighbor_node] * node_ranks[neighbor_node]
                node_ranks[node] = (1 - self.d) + self.d * _sum

        min_rank, max_rank = min(node_ranks.values()), max(node_ranks.values())
        for node, rank_val in node_ranks.items():
            node_ranks[node] = (rank_val - min_rank / (max_rank - min_rank))
        return node_ranks


class Textrank():
    @staticmethod
    def _calculate_graph(element_relation):
        graph = UndirectedWeightedgraph()

        for (word1,word2), freq in element_relation.item():
            graph.add_edge(word1, word2, freq)

        nodes_rank = graph.rank()

        results = sorted(nodes_rank.items(), key=lambda x: x[1], reverse=True)

        return results

    def textrank(self, elements, window_size = 10):

        elements_relation = {}

        for i, ele in enumerate(elements):
            for j in range(i + 1, min(i + window_size, len(elements))):
                term = (ele, elements[j])
                elements_relation[term] = elements_relation.get(term, 0) + 1

        result = self._calculate_graph(elements_relation)

        return result


