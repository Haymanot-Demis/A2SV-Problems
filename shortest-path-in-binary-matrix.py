class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[len(grid) - 1][len(grid[0]) - 1]:
            return -1
        return self.BFS(grid, 0, 0)
    def BFS(self, grid, row, col):        
        directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        queue = deque([(0, 0)])
        grid[0][0] = 1
        shortest_path = 0
        while queue:
            shortest_path += 1
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                if curr[0] == len(grid) - 1 and curr[1] == len(grid[0]) - 1:
                    return shortest_path
                for i, j in directions:
                    new_row = curr[0] + i
                    new_col = curr[1] + j
                    inbound = 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])
                    if inbound and grid[new_row][new_col] == 0:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 1
        return -1