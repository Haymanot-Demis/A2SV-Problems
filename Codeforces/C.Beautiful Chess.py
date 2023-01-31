def FindBishop(chess):
    for i in range(1,7):
        if chess[i].count("#") == 1:
            row, col = i,chess[i].index("#")
            if chess[row - 1][col - 1] == "#" and chess[row - 1][col + 1] == "#" and chess[row + 1][col + 1] == "#" and chess[row + 1][col - 1] == "#":
                print(row + 1, col + 1)
                return
testcase = int(input())
chesses = [[] for _ in range(testcase)]
for i in range(testcase):
    input()
    for _ in range(8):
        chesses[i].append(input())
for chess in chesses:
    FindBishop(chess)