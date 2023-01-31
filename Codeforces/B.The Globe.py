from collections import Counter
testcases = int(input())
for _ in range(testcases):
    length, cost = list(map(int, input().split()))
    planetOribits = list(map(int, input().split()))
    counter = Counter(planetOribits)
    totalCost = 0
    for orbit, freq in counter.items():
        if freq >= cost:
            totalCost += cost
        else:
            totalCost += freq
    print(totalCost)
