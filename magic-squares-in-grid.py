class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        one_up_nine = set(range(1,10))
        rowLen = len(grid)
        colLen = len(grid[0])
        if rowLen < 3 or colLen < 3:
            return 0
        else:
            distincts = set()
            left_diagonal_sum  = 0
            right_diagonal_sum  = 0
            rowSum = []
            colSum = [0]*3
            magicCount = 0
            for i in range(3):
                distincts |= set(grid[i][0:3])
                left_diagonal_sum += grid[i][i]
                right_diagonal_sum += grid[i][2 - i]
                rowSum.append(sum(grid[i][0:3]))
                colSum[0] += grid[i][0]
                colSum[1] += grid[i][1]
                colSum[2] += grid[i][2]
            

            if distincts == one_up_nine and left_diagonal_sum == right_diagonal_sum == rowSum[0] == rowSum[1] == rowSum[2] == colSum[0] == colSum[1] == colSum[2]:
                magicCount += 1
            for j in range(1, colLen - 2):
                distincts = set()
                distincts = distincts.union(set(grid[0][j:j+3]))
                distincts = distincts.union(set(grid[1][j:j+3]))
                distincts = distincts.union(set(grid[2][j:j+3]))
                left_diagonal_sum = grid[0][j] + grid[1][j + 1] + grid[2][j + 2]
                right_diagonal_sum = grid[0][j + 2] + grid[1][j + 1] + grid[2][j]
                rowSum[0] = rowSum[0] - grid[0][j - 1] + grid[0][j + 2]
                rowSum[1] = rowSum[1] - grid[1][j - 1] + grid[1][j + 2]
                rowSum[2] = rowSum[2] - grid[2][j - 1] + grid[2][j + 2]
                colSum[0] = colSum[1]
                colSum[1] = colSum[2]
                colSum[2] = grid[0][j + 2] + grid[1][j + 2] + grid[2][j + 2]

                if distincts == one_up_nine and left_diagonal_sum == right_diagonal_sum == rowSum[0] == rowSum[1] == rowSum[2] == colSum[0] == colSum[1] == colSum[2]:
                    magicCount += 1
            left_diagonal_sum = right_diagonal_sum = rowSum[0] = rowSum[1] = rowSum[2] = colSum[0] = colSum[1] = colSum[2] = 0
            for i in range(1, rowLen - 2):
                distincts = set()
                for n in range(3):
                    distincts |= set(grid[i + n][0:3])
                    left_diagonal_sum += grid[i + n][n]
                    right_diagonal_sum += grid[i + n][2 - n]
                    rowSum[n] = sum(grid[i + n][0:3])
                    colSum[0] += grid[i + n][0]
                    colSum[1] += grid[i + n][1]
                    colSum[2] += grid[i + n][2]
                if distincts == one_up_nine and left_diagonal_sum == right_diagonal_sum == rowSum[0] == rowSum[1] == rowSum[2] == colSum[0] == colSum[1] == colSum[2]:
                    magicCount += 1
                for j in range(1, colLen - 2):
                    distincts = set()
                    distincts = distincts.union(set(grid[i][j:j+3]))
                    distincts = distincts.union(set(grid[i + 1][j:j+3]))
                    distincts = distincts.union(set(grid[i + 2][j:j+3]))
                    left_diagonal_sum = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                    right_diagonal_sum = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
                    rowSum[0] = rowSum[0] - grid[i][j - 1] + grid[i][j + 2]
                    rowSum[1] = rowSum[1] - grid[i + 1][j - 1] + grid[i + 1][j + 2]
                    rowSum[2] = rowSum[2] - grid[i + 2][j - 1] + grid[i + 2][j + 2]
                    colSum[0] = colSum[1]
                    colSum[1] = colSum[2]
                    colSum[2] = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
                    if ( distincts == one_up_nine and left_diagonal_sum == right_diagonal_sum == rowSum[0] == rowSum[1] == rowSum[2] == colSum[0] == colSum[1] == colSum[2]):
                        magicCount += 1
                left_diagonal_sum = right_diagonal_sum = rowSum[0] = rowSum[1] = rowSum[2] = colSum[0] = colSum[1] = colSum[2] = 0
            return magicCount