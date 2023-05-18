class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.init_union_find(n)
        min_score = float("inf")
        for u, v, dist in roads:
            rep_u_v = self.union(u, v)

        for u, v, dist in roads:
            rep_u_v = self.find(u)
            rep_1 = self.find(1)
            if rep_u_v == rep_1:
                min_score = min(min_score, dist)
        return min_score
    def init_union_find(self, size):
        self.rep = {i:i for i in range(1, size + 1)}
        self.size = defaultdict(lambda : 1)

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
        return self.rep[rep_v]