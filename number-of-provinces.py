class Solution:
    def init_union_find(self, size):
        self.province = {i:i for i in range(size)}
        self.size = [1] * size
    def find(self, u):
        if u == self.province[u]:
            return u
        self.province[u] = self.find(self.province[u])
        return self.province[u]
    
    def union(self, u, v):
        prov_u = self.find(u)
        prov_v = self.find(v)

        if prov_v != prov_u:
            if self.size[prov_v] > self.size[prov_u]:
                self.province[prov_v] = prov_u
                self.size[prov_u] += self.size[prov_v]
            else:
                self.province[prov_u] = prov_v
                self.size[prov_v] += self.size[prov_u]
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.init_union_find(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    self.union(i, j)

        provinces = set()
        for city in range(len(isConnected)):
            prov = self.find(city)
            provinces.add(prov)
        
        return len(provinces)