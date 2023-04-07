class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        stack = [source]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            for v in adj_list[curr]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        return False