class Solution:
    def init_union_find(self, stones):
        self.rep = {tuple(stone):tuple(stone) for stone in stones}
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
    def removeStones(self, stones: List[List[int]]) -> int:
        self.init_union_find(stones)
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(tuple(stones[i]), tuple(stones[j]))
        groups = defaultdict(int)
        for i in range(len(stones)):
            groups[self.find(tuple(stones[i]))] += 1
        return sum(groups.values()) - len(groups)