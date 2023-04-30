class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i  in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    visited = set()
                    if self.dfs(board, i, j, visited):
                        for x, y in visited:
                            board[x][y] = "X"
                    print(visited)

            
    def dfs(self, board, row, col, visited):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited.add((row, col))
        for x, y in directions:
            new_x = row + x
            new_y = col + y
            inbound = 0 <= new_x < len(board) and 0 <= new_y < len(board[0])
            if not inbound:
                return False
            if (new_x, new_y) not in visited and board[new_x][new_y] == "O":
                if not self.dfs(board, new_x, new_y, visited):
                    return False
        
        return True