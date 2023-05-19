class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        self.init_union_find(len(source))
        for a, b in allowedSwaps:
            self.union(a, b)

        group = defaultdict(lambda : defaultdict(int))

        for i in range(len(source)):
            group[self.find(i)][source[i]] += 1

        similar = 0
        for i in range(len(target)):
            g = self.find(i)
            if group[g][target[i]]:
                group[g][target[i]] -= 1
                similar += 1
        hamming_distance = len(source) - similar
                    
        return hamming_distance

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