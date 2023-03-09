class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        prefix_sum = copy.deepcopy(grid)

        for col in range(1, colLen):
            prefix_sum[0][col] += prefix_sum[0][col - 1]
            prefix_sum[1][col] += prefix_sum[1][col - 1]

        for col in range(colLen):
            if prefix_sum[0][-1] - prefix_sum[0][col] < prefix_sum[1][col]:
                return max(prefix_sum[0][-1] - prefix_sum[0][col], prefix_sum[1][col] - grid[1][col])
            grid[0][col] = 0

        return max(prefix_sum[0][-1] - prefix_sum[0][col], prefix_sum[1][col] - grid[1][col])