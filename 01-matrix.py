class Solution:
    def __init__(self):
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        done = set()
        max_path = max(len(mat), len(mat[0]))
        answer = [ [max_path - 1 for _ in range(len(mat[0]))] for j in range(len(mat)) ]

        for i in range(len(mat)): 
            for j in range(len(mat[0])):
                if (i, j) not in done:
                    path, cell = self.BFS(mat, i, j)
                    answer[cell[0]][cell[1]] = 0
                    done.add(cell)
                    while path[(cell[0], cell[1])]:
                        prev = path[(cell[0], cell[1])]
                        done.add(prev)
                        answer[prev[0]][prev[1]] = answer[cell[0]][cell[1]] + 1
                        cell = prev
        return answer
    
    def BFS(self, mat, row, col):
        path = {(row, col):None}
        queue = deque([(row, col)])
        visited = set([(row, col)])
        found = False
        last = None

        while queue:
            curr = queue.popleft()
            if not mat[curr[0]][curr[1]]:
                found = True
                last = curr
                break
            for x, y in self.directions:
                new_row = curr[0] + x
                new_col = curr[1] + y
                inbound = 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0])
                if inbound and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    path[(new_row, new_col)] = (curr[0], curr[1])

        return path, last