length = int(input())
array = list(map(int, input().split()))
# length = len(array)
for i in range(length - 1):
    flag = array[i] % 2 == 0
    minValIndx = i
    for j in range(i + 1, length - 1):
        if (array[j] % 2 == 0) is not flag and array[j] < array[minValIndx]:
            minValIndx = j
        if minValIndx != i:
            array[i], array[minValIndx] = array[minValIndx], array[i]
for i in range(length):
    print(array[i], end=" ")