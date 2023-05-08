class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left_diagonal = 0
        right_diagonal = 0
        i = j = 0
        k = 0
        m = len(mat) - 1
        while i < len(mat):
            left_diagonal += mat[i][j]
            i += 1
            j += 1

            right_diagonal += mat[m][k]
            k += 1
            m -= 1
        if len(mat) % 2:
            return left_diagonal + right_diagonal - mat[len(mat) // 2][len(mat) // 2]
        return left_diagonal + right_diagonal