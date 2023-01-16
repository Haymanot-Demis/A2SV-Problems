class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        maxLocal =[ [0 for _ in range(length - 2)] for _ in range(length - 2) ]
        for i in range(length - 2):
            for j in range(length - 2):
                maxVal = grid[i][j]
                for k in range(3):
                    maxVal = max(maxVal, max(grid[i + k][j:j + 3]))
                maxLocal[i][j] = maxVal

        return maxLocal