class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        safe_states = []
        def dfs(node):
            if color[node] == 1:
                return False
            
            if color[node] == 2:
                return True
            color[node] = 1
            for neighbour in graph[node]:
                is_safe = dfs(neighbour)
                if not is_safe:
                    return False
            color[node] = 2
            safe_states.append(node)
            return True
        
        for i in range(len(graph)):
            dfs(i)
        safe_states.sort()
        return safe_states