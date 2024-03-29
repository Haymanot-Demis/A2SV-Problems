#time 80
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:
                    if j > 0:
                        self.matrix[i][j] += self.matrix[i][j-1]  
                elif j == 0:
                    if i > 0:
                        self.matrix[i][j] += self.matrix[i-1][j]  
                else:
                    self.matrix[i][j] += self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        else:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)