length1, length2 = list(map(int, input().split()))
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
p1 = 0
p2 = 0
result = [0]*length2
while p1 < length1 and p2 < length2:
    if array1[p1] < array2[p2]:
        result[p2] += 1 
        p1 += 1
    else:
        p2 += 1
for i in range(1, length2):
    result[i] += result[i - 1]
for num in result:
    print(num, end=" ")
