from collections import Counter


def canIncreasing(arr):
    frequencies = set(Counter(arr).values())
    for freq in frequencies:
        if freq >= 2:
            print("NO")
            return

    print("YES")


testcases = int(input())
nums = []
for _ in range(testcases):
    length = input()
    nums.append(list(map(int, input().split())))
for num in nums:
    canIncreasing(num)
