class Solution:
    def __init__(self):
        self.rep = {}

    def init_union_find(self, size):
        self.rep = {i:i for i in range(size)}
        self.size = [1] * size

    def find(self, u):
        if u == self.rep[u]:
            return u
        self.rep[u] = self.find(self.rep[u])
        return  self.rep[u]
    
    def union(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)

        if rep_u != rep_v:
            if self.size[rep_u] >= self.size[rep_v]:
                self.rep[rep_v] = rep_u
                self.size[rep_u] += self.size[rep_v]
            else:
                self.rep[rep_u] = rep_v
                self.size[rep_v] += self.size[rep_u]
    def areConnected(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)

        return rep_u == rep_v


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.init_union_find(n)
        for u, v in edges:
            self.union(u, v)
        
        return self.areConnected(source, destination)