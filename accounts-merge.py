class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.init_union_find(len(accounts))
        acc_dict = defaultdict(str)

        for i in range(len(accounts)):
            acc_dict[i] = set(accounts[i][1:])

        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                if len((acc_dict[i] & acc_dict[j])) >= 1:
                    self.union(i, j)

        accnts = defaultdict(set)
        owner = [""]*len(accounts)

        for i in range(len(accounts)):
            rep = self.find(i)
            owner[rep] = accounts[i][0]
            accnts[rep] |= acc_dict[i]

        ans = []
        for rep, emails in accnts.items():
            ans.append([owner[rep]] + sorted(emails))
            
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