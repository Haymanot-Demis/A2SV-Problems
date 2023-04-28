from collections import defaultdict
from collections import deque

def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())

def BFSShortestPath(adj_list, a, b):
    path = {a:None}
    queue = deque([a])
    visited = set([a])
    found = False

    while queue:
        length = len(queue) 
        for i in range(length):
            curr = queue.popleft()
            if curr == b:
                last = curr
                found = True
                
            for adj in adj_list[curr]:
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                    path[adj] = curr
    if found:
        shortest_path = []
        vertice = b

        while vertice:
            shortest_path.append(vertice)
            vertice = path[vertice]
        print(len(shortest_path) - 1)
        for p in shortest_path[::-1]:
            print(p, end=" ")

    else:
        print(-1)
    
v, e = MI()
a, b = MI()
adj_list = defaultdict(list)
for _ in range(e):
    u, v = MI()
    adj_list[u].append(v)
    adj_list[v].append(u)

BFSShortestPath(adj_list, a, b)