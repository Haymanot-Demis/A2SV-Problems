class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int, {(m - 1, n - 1):1})

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not memo[(i, j)]:
                    memo[(i, j)] = memo[(i + 1, j)] + memo[(i, j + 1)]

        return memo[(0, 0)]