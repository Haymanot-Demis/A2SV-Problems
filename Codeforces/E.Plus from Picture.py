m, n = list(map(int, input().split()))
array = []
for _ in range(m):
    array.append(list(input()))

row = 0
while row < m:
    count = array[row].count("*")
    if count != 0:
        break
    row += 1
if row >= m:
    print("NO")
    exit(0)
centerCol = array[row].index("*")
cols = list(zip(*array))
for i in range(n):
    count = cols[i].count("*")
    if count != 0:
        break
if i >= n:
    print("NO")
    exit(0)
centerRow = cols[i].index("*")
print(centerRow, centerCol)

if centerRow == 0 or centerRow == m - 1 or centerCol == 0 or centerCol == n - 1 or array[centerRow][centerCol] != "*" or array[centerRow][centerCol - 1] != "*" or array[centerRow][centerCol + 1] != "*" or array[centerRow + 1][centerCol] != "*" or array[centerRow][centerCol + 1] != "*":
    print("NO")
    exit(0)
col = centerCol
while col >= 0 and array[centerRow][col] != ".":
    array[centerRow][col] = "."
    col -= 1
print("left end", (centerRow, col))
col = centerCol + 1
while col < n and array[centerRow][col] != ".":
    array[centerRow][col] = "."
    col += 1
print("right end", (centerRow, col))
print(array[centerRow])
rowSet = set(array[centerRow])
if "*" in rowSet:
    print("NO")
    exit(0)

rowindx = centerRow - 1
while rowindx >= 0 and array[rowindx][centerCol] != ".":
    array[rowindx][centerCol] = "."
    rowSet = set(array[rowindx])
    if "*" in rowSet:
        print("NO")
        exit(0)
    rowindx -= 1
print("top end", (rowindx, centerCol))
while rowindx >= 0:
    rowSet = set(array[rowindx])
    if "*" in rowSet:
        print("NO")
        exit(0)
    rowindx -= 1

rowindx = centerRow + 1
while rowindx < m and array[rowindx][centerCol] != ".":
    array[rowindx][centerCol] = "."
    rowSet = set(array[rowindx])
    if "*" in rowSet:
        print("NO")
        exit(0)
    rowindx += 1
print("bottom end", (rowindx, centerCol))
while rowindx < m:
    rowSet = set(array[rowindx])
    if "*" in rowSet:
        print("NO")
        exit(0)
    rowindx += 1
print("YES")

# while row < m:
#     count = array[row].count("*")
#     if count != 0:
#         centerCol = array[row].index("*")
#         if centerCol == 0 or centerCol == n - 1:
#             print("NO")
#             exit(0)
#         col = centerCol
#         while row < m and array[row][col - 1] == "." and array[row][col + 1] == ".":
#             array[row][col] = "."
#             rowSet = set(array[row])
#             if "*" in rowSet:
#                 print("NO")
#                 exit(0)
#             row += 1
#         if row >= m or array[row][col] != "*" or array[row][col - 1] != "*" or array[row][col + 1] != "*" or array[row + 1][col] != "*" or array[row][col + 1] != "*":
#             print("NO")
#             exit(0)
#         centerRow = row

#         while col >= 0 and array[row][col] != ".":
#             array[centerRow][col] = "."
#             col -= 1
#         col = centerCol + 1
#         while col < n and array[row][col] != ".":
#             array[centerRow][col] = "."
#             col += 1
#         centerRowSet = set(array[centerRow])
#         if "*" in centerRowSet:
#             print("NO")
#             exit(0)

#         while row < m:
#             array[row][centerCol] = "."
#             rowSet = set(array[row])
#             if "*" in rowSet:
#                 print("NO")
#                 exit(0)
#             row += 1
#         print("YES")
#         exit(0)
#     row += 1
# print("NO")
