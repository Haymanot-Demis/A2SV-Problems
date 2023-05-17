class Solution:
    def init_union_find(self, n, m):
        self.group = {}
        self.size = defaultdict(lambda : 1)
        for i  in range(n):
            for j in range(m):
                self.group[(i, j)]= (i, j)
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
    def areConnected(self, A, B):
        return self.find(A) == self.find(B)
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        self.init_union_find(n, m)
        directions = {1:[(0, -1), (0, 1)], 2:[(-1, 0), (1, 0)], 3:[(0, -1),(1, 0)], 4:[(1, 0), (0, 1)], 5:[(0, -1), (-1, 0)], 6:[(-1, 0), (0, 1)]}

        for row in range(n):
            for col in range(m):
                for i , j in directions[grid[row][col]]:
                    new_row = row + i
                    new_col = col + j
                    inbound = 0 <= new_row < n and 0 <= new_col < m
                    if inbound and grid[new_row][new_col] and (-i, -j) in directions[grid[new_row][new_col]]:
                        self.union((row, col), (new_row, new_col))
        return self.areConnected((0, 0), (n - 1, m - 1))