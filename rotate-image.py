class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(i, length - 1 - i):
                r,c = i,j
                next = matrix[i][j]
                for _ in range(4):
                    next, matrix[c][length - 1 - r] = matrix[c][length - 1 - r], next
                    r, c = c, length - 1 - r