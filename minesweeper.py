class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.ReavelCellDFS(board, click[0], click[1])
        return board

    def ReavelCellDFS(self, grid, row, col):
        if grid[row][col] == "M":
            grid[row][col] = "X"
            return True # game over
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        adjacents = []
        mine_count = 0
        for x, y in directions:
            new_row = row + x
            new_col = col + y
            inbound = 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])
            if not inbound:
                continue
            if grid[new_row][new_col] == "E":
                adjacents.append((new_row, new_col))
            
            if grid[new_row][new_col] == "M":
                mine_count += 1
            
        if mine_count:
            grid[row][col] = str(mine_count)
        else:
            grid[row][col] = "B"
            for adj in adjacents:
                self.ReavelCellDFS(grid, adj[0], adj[1])