length1, length2 = list(map(int, input().split()))
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
p1 = 0
p2 = 0
result = []
while p1 < length1 and p2 < length2:
    if array1[p1] < array2[p2]:
        result.append(array1[p1])
        p1 += 1
    else:
        result.append(array2[p2])
        p2 += 1

result.extend(array2[p2:])
result.extend(array1[p1:])

for num in result:
    print(num, end=" ")
