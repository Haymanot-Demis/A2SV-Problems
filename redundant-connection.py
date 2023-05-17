class Solution:
    def init_union_find(self, size):
        self.group = {i:i for i in range(1, size + 1)}
        self.size = defaultdict(lambda : 1)
    def find(self, pos):
        if pos == self.group[pos]:
            return pos
        self.group[pos] = self.find(self.group[pos])
        return self.group[pos]
    
    def union(self, A, B):
        gr_A = self.find(A)
        gr_B = self.find(B)

        if gr_A != gr_B:
            if self.size[gr_A] >= self.size[gr_B]:
                self.group[gr_B] = gr_A
                self.size[gr_A] += self.size[gr_B]
            else:
                self.group[gr_A] = gr_B
                self.size[gr_B] += self.size[gr_A]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.init_union_find(len(edges))
        for u, v in edges:
            if self.find(u) == self.find(v):
                return [u, v]
            self.union(u, v)