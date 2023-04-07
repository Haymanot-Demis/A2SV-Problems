class Solution:
    def __init__(self):
        self.grid = None
        self.visited = None
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j]:
                    return self.dfs(i, j)
            
    def dfs(self, row, col):
        directions = [(0,1),(0,-1),(1,0),(-1, 0)]
        def inbound(i, j):
            return (0 <= i < len(self.grid)) and (0 <= j < len(self.grid[0]))
        if not self.grid[row][col]:
            return 1

        self.visited.add((row, col))
        count = 0
        for horiz, vertic in directions:
            new_row = row + horiz
            new_col = col + vertic
            if not inbound(new_row, new_col):
                count += 1
            if inbound(new_row, new_col) and (new_row, new_col) not in self.visited:
                count += self.dfs(new_row, new_col)
            
        return count