class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    adj_list[i].append(j)

        for city, adjacents in adj_list.items():
            if city not in visited:
                self.dfs(adj_list, city, visited)
                provinces += 1
        
        return provinces

    def dfs(self, adj_list, curr, visited):
        visited.add(curr)
        for adj in adj_list[curr]:
            if adj not in visited:
                self.dfs(adj_list, adj, visited)