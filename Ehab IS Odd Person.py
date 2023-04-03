n = int(input())
nums = list(map(int, input().split()))
odds = 0
evens = 0
for num in nums:
    if num % 2:
        odds += 1
    else:
        evens += 1
if evens and odds:
    nums.sort()
    for num in nums:
        print(num, end=" ")
else:
    for num in nums:
        print(num, end=" ")