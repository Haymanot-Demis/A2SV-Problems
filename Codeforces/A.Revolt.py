def makeNonDecreasing(arr):
    count = 0
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and arr[left] != 1:
            left += 1
        while right > left and arr[right] != 0:
            right -= 1
        if left < right:
            count += 1
            left += 1
            right -= 1

    print(count)


testcases = int(input())
arrays = []
for _ in range(testcases):
    length = int(input())
    arrays.append(list(map(int, input().split())))

for array in arrays:
    makeNonDecreasing(array)
