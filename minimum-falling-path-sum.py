class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        directions = [[-1, -1], [-1, 0], [-1, 1]]
        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
                path_sum = inf
                for i, j in directions:
                    prev_x = row + i
                    prev_y = col + j
                    inbound =  0 <= prev_x < len(matrix) and 0 <= prev_y < len(matrix)

                    if inbound:
                        path_sum = min(path_sum, matrix[row][col] + matrix[prev_x][prev_y])
                matrix[row][col] = path_sum

        return min(matrix[-1])