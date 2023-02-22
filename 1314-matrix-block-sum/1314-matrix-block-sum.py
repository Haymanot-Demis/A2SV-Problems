class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rowLen = len(mat)
        colLen = len(mat[0])
        matrix_prefix_sum = [ [0]*(colLen + 1) for _ in range(rowLen + 1)]
        for i in range(rowLen):
            for j in range(colLen):
                matrix_prefix_sum[i + 1][j + 1] = mat[i][j] + matrix_prefix_sum[i][j + 1] + matrix_prefix_sum[i + 1][j] - matrix_prefix_sum[i][j]
        mat_block_sum = [ [0]*colLen for _ in range(rowLen)]
        print(matrix_prefix_sum)
        for i in range(rowLen):
            for j in range(colLen):
                row1 = max(i - k, 0)
                row2 = min(i + k, rowLen - 1)
                col1 = max(j - k, 0)
                col2 = min(j + k, colLen - 1)
                mat_block_sum[i][j] = matrix_prefix_sum[row2 + 1][col2 + 1] - matrix_prefix_sum[row2 + 1][col1] - matrix_prefix_sum[row1][col2 + 1] + matrix_prefix_sum[row1][col1]
                    
        return mat_block_sum