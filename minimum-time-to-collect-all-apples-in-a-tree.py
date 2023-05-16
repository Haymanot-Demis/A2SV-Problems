class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        return self.dfs(adj_list, 0, -1, hasApple)[1]
    
    def dfs(self, adj_list, node, parent, hasApple):
        time = 0
        got_apple = False

        for adj in adj_list[node]:
            if adj != parent:
                res = self.dfs(adj_list, adj, node, hasApple)
                if res[0]:
                    time += res[1] + 2
                    got_apple = True

        if got_apple:
            return [True, time]
        
        return [hasApple[node], 0]