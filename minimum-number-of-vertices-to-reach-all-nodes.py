class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = [1] * n
        answer = []
        for u, v in edges:
            vertices[v] = 0
        for i in range(n):
            if vertices[i]:
                answer.append(i)
        return answer