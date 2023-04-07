class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return self.dfs(source, adj_list, set(), destination)
    def dfs(self, node, adj_list, visited, dest):
        if node == dest:
            return True
        visited.add(node)
        for v in adj_list[node]:
            if v not in visited:
                if self.dfs(v, adj_list, visited, dest):
                    return True
                
        return False