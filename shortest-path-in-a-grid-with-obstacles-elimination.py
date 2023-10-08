class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        hashMap = defaultdict(lambda : inf, {(0, 0) : grid[0][0]})
        visited = set([(0, 0)])
        processed = set()
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        steps = 0

        while queue:
            length = len(queue)

            for _ in range(length):
                i, j = queue.popleft()
                obstacles = hashMap[(i, j)]

                if (i, j) == (n - 1, m - 1):
                    return steps
                
                processed.add((i, j))

                for r, c in direc:
                    new_i, new_j = i + r, j + c
                    if inbound(new_i, new_j):
                        one = obstacles + grid[new_i][new_j] <= k
                        two = (new_i, new_j) in visited
                        three = (new_i, new_j) in processed
                        four = hashMap[(new_i,new_j)] > obstacles + grid[new_i][new_j]
                        
                        hashMap[(new_i,new_j)] = min(hashMap[(new_i,new_j)], obstacles + grid[new_i][new_j])
                        
                        if one and not two:
                            queue.append((new_i, new_j))
                            visited.add((new_i, new_j))
                        elif one and two and three and four:
                            queue.append((new_i, new_j))
                
            steps += 1

        return -1