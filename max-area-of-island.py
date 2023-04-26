class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
    def dfs(self, grid, row, col):
        grid[row][col] = 0
        area = 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for x, y in directions:
            new_x = x + row
            new_y = y + col
            inbound = 0 <=  new_x < len(grid) and 0 <= new_y < len(grid[0])
            if inbound and grid[new_x][new_y]:
                area += self.dfs(grid, new_x, new_y)
        return area