class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.init_union_find(len(points))
        def cost(xi, yi, xj, yj):
            return abs(xi - xj) + abs(yi - yj)

        graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                graph.append((cost(*points[i], *points[j]), i, j))
            
        
        graph.sort()
        min_cost = 0
        for cost, start, dest in graph:
            if self.union(start, dest):
                min_cost += cost                   
        
        return min_cost

    def init_union_find(self, size):
        self.rep = {i:i for i in range(size)}
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
            return True
        return False