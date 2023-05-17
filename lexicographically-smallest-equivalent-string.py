class Solution:
    def __init__(self):
        self.group = {chr(i + 97) : chr(i + 97)  for i in range(26)}
    def find(self, pos):
        if pos == self.group[pos]:
            return pos
        self.group[pos] = self.find(self.group[pos])
        return self.group[pos]
    
    def union(self, A, B):
        gr_A = self.find(A)
        gr_B = self.find(B)

        if gr_A != gr_B:
            if gr_B >= gr_A:
                self.group[gr_B] = gr_A
            else:
                self.group[gr_A] = gr_B

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        for i in range(len(s1)):
            self.union(s1[i], s2[i])
        ans = ""
        for i in range(len(baseStr)):
            ans += self.find(baseStr[i])
        return ans