def dropStones(grid):
    rowLen = len(grid) - 1
    colLen = len(grid[0])
    for col in range(colLen):
        down = rowLen
        for top in range(rowLen, -1, -1):
            print(grid[top][col], end="")
            if grid[top][col] == "o":
                down = top - 1
            elif grid[top][col] == "*":
                grid[down][col], grid[top][col] = grid[top][col], grid[down][col]
                down -= 1
        print()

    for i in range(rowLen + 1):
        print("".join(grid[i]))


testcases = int(input())
grids = [[] for i in range(testcases)]
for i in range(testcases):
    dimesion = list(map(int, input().split()))
    for _ in range(dimesion[0]):
        grids[i].append(list(input()))
for grid in grids:
    dropStones(grid)
