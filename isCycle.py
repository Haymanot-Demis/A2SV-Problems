from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        visited = set()
        for node in range(len(adj)):
            if node not in visited and self.dfs(adj, node, None, visited):
                return True
        return False
            
    def dfs(self, graph, node, parent,visited):
        if node in visited:
            return True
        visited.add(node)
        
        for adj in graph[node]:
            if adj != parent:
                if self.dfs(graph, adj, node, visited):
                    return True
        return False