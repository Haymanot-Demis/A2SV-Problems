class Solution:
    def __init__(self):
        self.adj_list = defaultdict(list)
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        return self.dfs(source, set(), destination)
    def dfs(self, node, visited, dest):
        if node == dest:
            return True
        visited.add(node)
        for v in self.adj_list[node]:
            if v not in visited:
                if self.dfs(v, visited, dest):
                    return True
                
        return False