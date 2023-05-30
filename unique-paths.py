class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(0, 0):1, (0, 1):1, (1, 0) : 1}

        return self.countUniquePaths(m, n, (m-1, n-1), memo)
    def countUniquePaths(self, m, n, curr,memo):
        if curr in memo:
            return memo[curr]
        
        paths = 0
        for i, j in [(-1, 0), (0, -1)]:
            new_x = i + curr[0]
            new_y = j + curr[1]
            inbound = 0 <= new_x < m and 0 <= new_y < n
            if inbound:
               paths += self.countUniquePaths(m, n, (new_x, new_y), memo)
        
        memo[curr] = paths
        return paths