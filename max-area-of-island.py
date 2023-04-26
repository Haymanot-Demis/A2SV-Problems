class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    stack = []
                    stack.append((i, j))
                    grid[i][j] = 0
                    area = 0
                    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
                    while stack:
                        area += 1
                        curr = stack.pop()
                        for x, y in directions:
                            new_x = x + curr[0]
                            new_y = y + curr[1]
                            inbound = 0 <=  new_x < len(grid) and 0 <= new_y < len(grid[0])
                            if inbound and grid[new_x][new_y]:
                                grid[new_x][new_y] = 0
                                stack.append((new_x, new_y))
                    
                    max_area = max(max_area, area)
        return max_area