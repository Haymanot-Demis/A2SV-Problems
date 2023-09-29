class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = defaultdict(lambda : inf)
        m = len(grid)
        n = len(grid[0])

        memo[(0, 0)] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0):
                    continue
                top = memo[(i - 1, j)]
                left = memo[(i, j - 1)]

                prev = min(top, left)
                memo[(i, j)] = prev + grid[i][j]
        
        return memo[(m - 1, n - 1)]