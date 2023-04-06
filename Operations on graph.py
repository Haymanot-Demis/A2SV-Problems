from collections import defaultdict
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    def AddEdge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
    def vertices(self, u):
        for v in self.adjacency_list[u]:
            print(v, end=' ')
vertices = int(input())
no_of_ops = int(input())
undirected = Graph()
for _ in range(no_of_ops):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        undirected.AddEdge(operation[1], operation[2])
    else:
        undirected.vertices(operation[1])