from collections import defaultdict
def countSwapsToMakeBeautiful(arr):
    length = len(arr)
    counter = 0
    for i in range(length - 1):
        for j in range(i, length - 1 - i):
            r,c = i,j
            hashmap = defaultdict(int)
            for k in range(4):
                hashmap[arr[r][c]] += 1
                r,c = c, length - 1 - r
            if hashmap[0] != 4 or hashmap[1] != 4:
                counter += min(hashmap[0], hashmap[1])
    print(counter)

testcases = int(input())
grids = [[] for _ in range(testcases)]
for i in range(testcases):
    length = int(input())
    for _ in range(length):
        arr = list(map(int, list(input())))
        grids[i].append(arr)

for grid in grids:
    countSwapsToMakeBeautiful(grid)
