m, n = list(map(int, input().split()))
array = []
for _ in range(m):
    array.append(list(input()))
cols = list(zip(*array))
print(cols)
top = -1
down = -1
left = -1
right = -1

itr = 0
while itr < n and (left == -1 or right == -1):
    if left == -1 and "B" in cols[itr]:
        left = itr
    if right == -1 and "B" in cols[n - 1 - itr]:
        right = n - 1 - itr
    itr += 1

itr = 0
while itr < m and (top == -1 or down == -1):
    if top == -1 and "B" in array[itr]:
        top = itr
    if down == -1 and "B" in array[m - 1 - itr]:
        down = m - 1 - itr
    itr += 1
sideLength = max(down - top, right - left) + 1
print(sideLength, top, down, left, right)
if top + down + left + right == -4:  # if all are -1 no black painted cell so the square is 1 length
    print(1)
elif sideLength <= n and sideLength <= m:
    count = 0
    for i in range(top, down + 1):
        for j in range(left, right + 1):
            print(array[i][j], end=" ")
            if array[i][j] == "W":
                count += 1
        print()
    print(count)
else:
    print(-1)
