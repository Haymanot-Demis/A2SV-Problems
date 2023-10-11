class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        


        def dfs(node, parent):
            _splits = 0
            _sum = values[node]

            for adj in graph[node]:
                if adj != parent:
                    splits, Sum = dfs(adj, node)
                    _splits += splits
                    _sum += Sum
            
            if _sum % k == 0:
                _splits += 1
                _sum = 0
            
            return _splits, _sum
        
        return dfs(0, -1)[0]