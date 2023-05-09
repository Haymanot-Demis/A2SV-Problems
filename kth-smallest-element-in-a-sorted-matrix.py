class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][0], 0, 0)]
        first_k_smallest = []

        visited = set((0, 0))

        while heap and len(first_k_smallest) < k:
            value, i, j = heappop(heap)
            first_k_smallest.append(value)
            if i + 1 < len(matrix) and (i + 1, j) not in visited:
                heappush(heap, (matrix[i + 1][j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(matrix) and (i, j + 1) not in visited:
                heappush(heap, (matrix[i][j + 1], i, j + 1))
                visited.add((i, j + 1))

        return first_k_smallest[-1]