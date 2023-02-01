def findK(arr, nk):
    n, k = nk
    arr.sort()
    left = 0
    for right in range(1, n):
        if arr[right] - arr[left] > k:
            left += 1
        elif arr[right] - arr[left] == k:
            print("YES")
            return
    print("NO")


testcases = int(input())
arrays = []
for _ in range(testcases):
    n, k = map(int, input().split())
    arrays.append([[n, k], list(map(int, input().split()))])

for nk, array in arrays:
    print(array, nk)
