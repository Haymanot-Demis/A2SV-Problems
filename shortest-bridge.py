class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    island_edges = set()
                    visited = set()

                    self.islandEdgesBFS(grid, i, j, visited, island_edges)
                    
                    min_flips = self.minimumFlips(grid, island_edges, visited)
                    return min_flips

    def islandEdgesBFS(self, grid, row, col, visited, island_edges):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(row, col)])
        visited.add((row, col))
        island_edges.add((row, col))

        while queue:
            x, y = queue.popleft()
            for i, j in directions:
                new_x = x + i
                new_y = y + j
                inbound = 0 <= new_x < len(grid) and 0 <= new_y < len(grid)
                
                if inbound and grid[new_x][new_y] and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
                
                if not inbound or grid[new_x][new_y] == 0:
                    island_edges.add((x, y))

            
    def minimumFlips(self, grid, boundaries,island_one):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque(boundaries)
        visited = set()
        min_flip = 0

        while queue:
            length = len(queue)
            
            for _ in range(length):
                x, y = queue.popleft()
                for i, j in directions:
                    new_x = x + i
                    new_y = y + j

                    inbound = 0 <= new_x < len(grid) and 0 <= new_y < len(grid)

                    if inbound and (new_x, new_y) not in island_one and (new_x, new_y) not in visited:
                        if not grid[new_x][new_y]:
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
                        else:
                            return min_flip
            min_flip += 1