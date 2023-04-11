class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        for i in range(len(roads)):
            adj_list[roads[i][0]].add(roads[i][1])
            adj_list[roads[i][1]].add(roads[i][0])
        max_network = 0
        for u in adj_list:
            for v in adj_list:
                if u != v:
                    if u not in adj_list[v]:
                        max_network = max(max_network, len(adj_list[v]) + len(adj_list[u]))
                    else:
                        max_network = max(max_network, len(adj_list[v]) + len(adj_list[u]) - 1)

        return max_network