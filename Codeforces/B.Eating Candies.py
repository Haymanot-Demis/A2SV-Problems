def totalNumberOfCandies(candies):
    length = len(candies)
    left = -1
    right = length
    LeftCandies = 0
    rightCandies = 0
    count = 0
    while left < right:
        if LeftCandies > rightCandies:
            while right > left and rightCandies < LeftCandies:
                right -= 1
                rightCandies += candies[right]
        elif LeftCandies < rightCandies:
            while left < right and LeftCandies < rightCandies:
                left += 1
                LeftCandies += candies[left]
        else:
            left += 1
            count = left + length - right
            LeftCandies += candies[left]
    print(count)


testcases = int(input())
arrays = []
for _ in range(testcases):
    length = (input())
    arrays.append(list(map(int, input().split())))
print(arrays)
for arr in arrays:
    totalNumberOfCandies(arr)
