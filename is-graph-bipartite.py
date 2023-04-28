class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        unvisited = set(range(0, len(graph)))
        result = True

        while unvisited:
            visited = set()
            result = self.dfs(graph, unvisited.pop(), 1, visited)
            nodes, color = list(zip(*visited))
            if not result:
                return False
            unvisited = unvisited.difference(set(nodes))
        
        return result

    
    def dfs(self, graph, node, color, visited):
        visited.add((node, color))
        for adj in graph[node]:
            if (adj, color) in visited:
                return False
            next_color = 1 if not color else 0
            if (adj, next_color) not in visited:
                if not self.dfs(graph, adj, next_color, visited):
                    return False
            
        return True