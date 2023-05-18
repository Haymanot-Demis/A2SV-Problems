class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.init_union_find(len(s))
        for i, j in pairs:
            self.union(i, j)

        members = defaultdict(set)
        for i, j in pairs:
            rep = self.find(i)
            members[rep].add(i)
            members[rep].add(j)

        ans = list(s)
        
        m_copy = defaultdict(list)
        for rep, mems in members.items():
            members[rep] = sorted(mems)
            s[0]
            print(members[rep])
            m_copy[rep] = sorted(mems, key=lambda i : s[i])
            print(m_copy[rep])
            for i, indx in enumerate(members[rep]):
                ans[indx] = s[m_copy[rep][i]]
        
        return "".join(ans)
        


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