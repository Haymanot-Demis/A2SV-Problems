class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([tuple(entrance)])
        visited = set([tuple(entrance)])
        path = {tuple(entrance):None}

        while queue:
            row, col = queue.popleft()

            for x, y in directions:
                new_row = row + x
                new_col = col + y
                inbound = 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0])
                if not inbound and (row, col) != tuple(entrance):
                    cell = (row, col)
                    path_length = 0
                    while path[cell]:
                        path_length += 1
                        cell = path[cell]

                    return path_length 

                if not inbound or maze[new_row][new_col] == "+":
                    continue
                
                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    path[(new_row, new_col)] = (row, col)
        
        return -1