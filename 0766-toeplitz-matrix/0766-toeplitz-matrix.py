class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        for i in range(rowLen-1):
            for k in range(1, colLen):
                if matrix[i][k - 1] != matrix[i + 1][k]:
                    return False
        return True