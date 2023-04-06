class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for u,v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        for vertex, adjes in adjacency_list.items():
            if len(adjes) == len(adjacency_list) - 1:
                return vertex