class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        safe = []

        for node in range(len(graph)):
            self.dfs(graph, color, node, safe)
                
        return sorted(safe)

    
    def dfs(self, graph, color, node, safe):
        if color[node] == 1:
            return False   

        if color[node] == 2:
            return True   
            
        color[node] = 1
       
        isSafe = True
        for adj in graph[node]:
            if not self.dfs(graph, color, adj, safe):
                isSafe = False

        if not isSafe:
            return False
        
        color[node] = 2
        safe.append(node)
        return True