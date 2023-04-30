from collections import defaultdict

def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def MS(): return map(str,input().split())

def isBicolorable(adj_list, node, color, visited):
    visited[node] = color
    for adj in adj_list[node]:
        if adj not in visited:
            new_color = 1 if color == 2 else 2
            if not isBicolorable(adj_list, adj, new_color, visited):
                return False
        elif visited[adj] == color:
            return False
    
    return True
    

v = II()
while v:
    edges = II()
    adj_list = defaultdict(list)
    for _ in range(edges):
        a, b = MI()
        adj_list[a].append(b)
    
    result = isBicolorable(adj_list, 1, 1, defaultdict(int))
    if result:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
    v = II()