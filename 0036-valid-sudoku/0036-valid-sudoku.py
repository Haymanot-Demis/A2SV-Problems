class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colValues = [set() for _ in range(9)]
        subboxes =[ [set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            rowValues = {}
            for j in range(9):
                if board[i][j] != ".":
                    if rowValues.get(board[i][j], -1) != -1:
                        return False
                    rowValues[board[i][j]] = j
                    if board[i][j] in colValues[j]:
                        return False
                    colValues[j].add(board[i][j]) 
                    if board[i][j] in subboxes[i//3][j//3]:
                        return False
                    subboxes[i//3][j//3].add(board[i][j]) 
        return True