class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.init_union_find(row, col)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        last_day = len(cells) - 1
        lands = set()

        while last_day >= 0 and self.find((1, 1)) != self.find((row, 1)):
            r = cells[last_day][0]
            c = cells[last_day][1]
            lands.add((r, c))

            for i, j in directions:
                new_row = r + i
                new_col = c + j
                if (new_row, new_col) in lands:
                    self.union((new_row, new_col), (r, c))
            last_day -= 1

        return last_day + 1
            

    def init_union_find(self, n, m):
        self.rep = defaultdict(tuple)
        self.size = defaultdict(lambda : 1)
        for i in range(1, m + 1):
            self.rep[(1, i)] = (1, 1)

        for i in range(1, m + 1):
            self.rep[(n, i)] = (n, 1)

    def find(self, u):
        if u == self.rep[u]:
            return u
        self.rep[u] = self.find(self.rep[u])
        return  self.rep[u]
    
    def union(self, u, v):
        if u not in self.rep:
            self.rep[u] = u

        if v not in self.rep:
            self.rep[v] = v

        rep_u = self.find(u)
        rep_v = self.find(v)
        
        if rep_u != rep_v:
            if self.size[rep_u] >= self.size[rep_v]:
                self.rep[rep_v] = rep_u
                self.size[rep_u] += self.size[rep_v]
            else:
                self.rep[rep_u] = rep_v
                self.size[rep_v] += self.size[rep_u]