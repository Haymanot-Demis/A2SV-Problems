class Solution:
    def __init__(self):
        self.group = {chr(i + 97) : chr(i + 97)  for i in range(26)}
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
            if self.size[gr_B] >= self.size[gr_A]:
                self.group[gr_A] = gr_B
                self.size[gr_B] += self.size[gr_A]
            else:
                self.group[gr_B] = gr_A
                self.size[gr_A] += self.size[gr_B]

    def equationsPossible(self, equations: List[str]) -> bool:
        disjoints = set()
        for var1, op, eq, var2 in equations:
            if op == "=" and ( (var1, var2) not in disjoints or (var2, var1) not in disjoints):
                self.union(var1, var2)
            elif op == "!" and self.find(var1) != self.find(var2):
                disjoints.add((var1, var2))
            else:
                return False
                
        for var1, var2 in disjoints:
            if self.find(var1) == self.find(var2):
                return False
        return True