class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        heap = [(0, (0, 0))]
        processed = set()
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m
        
        while heap:
            max_sofar, (i, j) = heappop(heap)
            if (i, j) == (n - 1, m - 1):
                return max_sofar
            if (i, j) in processed:
                continue
            processed.add((i, j))
            for r, c in direc:
                new_i = i + r 
                new_j = j + c 

                if inbound(new_i, new_j) and (new_i, new_j) not in processed:
                    effort = max(max_sofar, abs(heights[i][j] - heights[new_i][new_j]))
                    heappush(heap, (effort, (new_i, new_j)))