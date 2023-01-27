from collections import Counter
import random
length = int(input())
shuffled = list(map(int, input().split()))
if len(shuffled) == 1:
    print("YES")
    print(1)
    print(shuffled[0])
    print(0)
    print("")
else:
    counter = Counter(shuffled)
    for num, count in counter.items():
        if count > 2:
            print("NO")
            exit(0)
    if 2 in counter.values():
        shuffled.sort()
        increasing = [shuffled[0]]
        decreasing = []

        for i in range(1, length):
            if shuffled[i] == shuffled[i - 1]:
                decreasing.append(shuffled[i])
            else:
                increasing.append(shuffled[i])
        print(len(increasing))
        for el in increasing:
            print(el, end=" ")
        print()
        print(len(decreasing))
        for el in decreasing[::-1]:
            print(el, end=" ")
    else:
        shuffled.sort()
        incresingLen = random.randrange(1, length + 1)
        print("YES")
        print(incresingLen)
        for el in shuffled[:incresingLen]:
            print(el, end=" ")
        print()
        print(length - incresingLen)
        for el in shuffled[incresingLen:][::-1]:
            print(el, end=" ")