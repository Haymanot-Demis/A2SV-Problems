class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj_list = defaultdict(list)
        for child, parent in enumerate(parent):
            adj_list[parent].append(child)

        ans = [0]
        result = self.dfs(adj_list, 0, s, ans)
        ans[0] = max(ans[0], result[0])
        return ans[0]
    
    def dfs(self, adj_list, node, s, ans):
        if node not in adj_list:
            return (1, s[node])
        longest = 0
        for adj in adj_list[node]:
            result = self.dfs(adj_list, adj, s, ans)
            if s[node] != result[1]:
                ans[0] = max(ans[0], longest + result[0] + 1)
                longest = max(longest, result[0])
            else:
                ans[0] = max(ans[0], longest + 1, result[0])

        return (longest + 1, s[node])