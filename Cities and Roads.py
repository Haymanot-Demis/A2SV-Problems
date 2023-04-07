from collections import defaultdict, deque
vertices = int(input())
adj_list = defaultdict(list)
for u in range(1, vertices + 1):
    row = list(map(int, input().split()))
    for v, weight in enumerate(row):
        if weight:
            adj_list[u].append(v + 1)
roads = 0
visited = set()
for start, destinations in adj_list.items():
    for dest in destinations:
        if (min(start, dest), max(start, dest)) not in visited:
            roads += 1
            visited.add((min(start, dest), max(start, dest)))
print(roads)    