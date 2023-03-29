def BishopMaxAttack(board):
    row = len(board)
    col = len(board[0])
    left_diagonal_sum = {}
    right_diagonal_sum = {}
    for i in range(row):
        for j in range(col):
            left_diagonal_sum[i -
                              j] = left_diagonal_sum.get(i - j, 0) + board[i][j]
            right_diagonal_sum[i +
                               j] = right_diagonal_sum.get(i + j, 0) + board[i][j]
    maxAttack = 0
    for i in range(row):
        for j in range(col):
            maxAttack = max(
                maxAttack, left_diagonal_sum[i - j] + right_diagonal_sum[i + j] - board[i][j])
    return maxAttack


testcases = int(input())
chessboards = [[] for i in range(testcases)]
for i in range(testcases):
    m, n = map(int, input().split())
    for _ in range(m):
        chessboards[i].append(list(map(int, input().split())))

for chess in chessboards:
    print(BishopMaxAttack(chess))
