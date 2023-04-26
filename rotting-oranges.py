class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        zeroes = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i, j))

        seconds = -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            seconds += 1
            length = len(queue)
            for i in range(length):
                row, col = queue.popleft()
                for x, y in directions:
                    new_row = row + x
                    new_col = col + y
                    inbound = 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])
                    if inbound and grid[new_row][new_col]:
                        grid[new_row][new_col] = 0
                        queue.append((new_row, new_col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return seconds if seconds != -1 else 0