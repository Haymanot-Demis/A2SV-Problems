class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.init_union_find(len(accounts))
        for i in range(len(accounts)):
            accounts[i] = set(accounts[i])
        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                if len((accounts[i] & accounts[j])) >= 2:
                    self.union(i, j)
        accnts = defaultdict(set)
        for i in range(len(accounts)):
            accnts[self.find(i)] |= accounts[i]
        ans = []
        for rep, emails in accnts.items():
            ans.append(sorted(emails))
        return ans

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