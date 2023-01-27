def goodPairIndices(arr):
    left = 0
    right = 0
    counter = 0
    length = len(arr)
    while right < length:
        while right < length and arr[right] >= right + 1:
            right += 1
        if right >= length:
            n = length - left
            for i in range(n):
                counter += n - i
            print(counter)
            return
        else:
            if arr[right] > 0:
                n = right - left
                for i in range(n):
                    counter += n - i
                counter += arr[right] - 1
                if right + 1 == length:
                    counter += 1
            left = right
            right += 1

    print(counter)


testcases = int(input())
arrays = []
for _ in range(testcases):
    length = int(input())
    arrays.append(list(map(int, input().split())))

for array in arrays:
    goodPairIndices(array)
