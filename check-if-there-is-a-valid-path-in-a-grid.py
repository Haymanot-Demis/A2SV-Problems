class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        return self.dfs(grid, 0, 0)
    def dfs(self, grid, row, col):
        directions = {1:[(0, -1), (0, 1)], 2:[(-1, 0), (1, 0)], 3:[(0, -1),(1, 0)], 4:[(1, 0), (0, 1)], 5:[(0, -1), (-1, 0)], 6:[(-1, 0), (0, 1)]}
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return True
        curr = grid[row][col]
        grid[row][col] = 0
        # valid_neighbour = {1:set()}

        for i , j in directions[curr]:
            new_row = row + i
            new_col = col + j
            inbound = 0 <= new_row < len(grid)  and 0 <= new_col < len(grid[0])
            if inbound and grid[new_row][new_col] and (-i, -j) in directions[grid[new_row][new_col]]:
                if self.dfs(grid, new_row, new_col):
                    return True
        grid[row][col]=curr 
        return False