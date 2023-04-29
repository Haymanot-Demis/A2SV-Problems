class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikes_list = defaultdict(list)
        for u,v in dislikes:
            dislikes_list[u].append(v)
            dislikes_list[v].append(u)

        visited = set()
        nodes = list(dislikes_list.keys())
        for u in nodes: 
            if (u, 1) in visited or (u, 0) in visited:
                continue
            if not self.dfs(dislikes_list, u, 1, visited):
                return False
        return True
    def dfs(self, dislikes_list, node, color, visited):
        visited.add((node, color))
        
        for adj in dislikes_list[node]:
            if (adj, color) in visited:
                return False
            new_color = 0 if color else 1
            if (adj, new_color) not in visited:
                if not self.dfs(dislikes_list, adj, new_color, visited):
                    return False

        return True