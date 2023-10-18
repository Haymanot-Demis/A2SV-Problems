class Solution:
    def __init__(self):
        self.rep = [i for i in range(26)]
    def find(self, x):
        if x != self.rep[x]:
            r = self.find(self.rep[x]) 
            self.rep[x] = r
        return self.rep[x]
    
    def union(self, x, y):
        rep_x = self.find(x)
        rep_y = self.find(y)

        if rep_x <= rep_y:
            self.rep[rep_y] = rep_x
        else:
            self.rep[rep_x] = rep_y
        
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        for i in range(len(s1)):
            self.union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        
        ans = ""

        for ch in baseStr:
            ans += chr(self.find(ord(ch) - 97) + 97)
        
        return ans