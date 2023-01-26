def removeSmallest(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            print("NO")
            return
    print("YES")

testcases = int(input())
arrays = []
for _ in range(testcases):
    lenght = int(input())
    arrays.append(list(map(int, input().split())))

for array in arrays:
    removeSmallest(array)