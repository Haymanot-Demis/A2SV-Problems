class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        color = [0] * len(edges)
        for u, v in enumerate(edges):
            if v != -1:
                graph[u].append(v)
        max_cycle_len = -1
        position = [0] * len(edges)
        for node in range(len(edges)):
            if not color[node]:
                res = self.detectCycle(graph, node, color, 0, position)
                if res:
                    max_cycle_len = max(max_cycle_len, res)
        return max_cycle_len
    def detectCycle(self, graph, node, color, length, position):
        if color[node] == 2:
            # not cycle
            return
        if color[node] == 1:
            return length - position[node]
        color[node] = 1
        position[node] = length
        max_cycle_len = -1
        for adj in graph[node]:
            result = self.detectCycle(graph, adj, color, length + 1, position)
            if result:
                max_cycle_len = max(max_cycle_len, result)
        
        color[node] = 2
        return max_cycle_len