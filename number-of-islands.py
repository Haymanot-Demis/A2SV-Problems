class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, row, col):
        inbound = 0 <= row < len(grid) and 0 <= col < len(grid[0]) 
        if not inbound or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        for r,c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.dfs(grid, row + r, col + c)