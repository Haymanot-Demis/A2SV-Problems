class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        sub_islands = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]:
                    if self.dfs(grid1, grid2, i, j):
                        print(i, j)
                        sub_islands += 1
        return sub_islands
    def dfs(self, grid1, grid2, row, col):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        answer = True
        if not grid1[row][col]:
            answer = False
                
        grid2[row][col] = 0
        for x, y in directions:
            new_row = row + x
            new_col = col + y
            inbound = 0 <= new_row < len(grid2) and 0 <= new_col < len(grid2[0])
            if inbound and grid2[new_row][new_col]:
                if not self.dfs(grid1, grid2, new_row, new_col):
                    answer = False
                   
        return answer