def valley(arr: list):
    left = 0
    right = len(arr) - 1
    while left < right and arr[left] >= arr[left + 1]:
        left += 1
    while left < right and arr[right] >= arr[right - 1]:
        right -= 1
    if left == right:
        print("YES")
    else:
        print("NO")


testcases = int(input())
arrays = []
for _ in range(testcases):
    length = (input())
    arrays.append(list(map(int, input().split())))
print(arrays)

for arr in arrays:
    valley(arr)
