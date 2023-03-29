class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        rowLen = len(matrix)
        colLen = len(matrix[0])
        for i in range(rowLen):
            for j in range(colLen):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row in rows:
            matrix[row] = [0]*colLen
        
        for row in range(rowLen):
            if row not in rows:
                for col in cols:
                    matrix[row][col] = 0