class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        answer = []
        visited = set()

        while heap and len(answer) < k:
            sum, u, v = heappop(heap)
            answer.append([nums1[u], nums2[v]])
            next = [(u + 1, v), (u, v + 1), (u + 1, v + 1)]
            for u, v in next:
                inbound = u < len(nums1) and v < len(nums2)
                if inbound and (u, v) not in visited:
                    heappush(heap, (nums1[u] + nums2[v], u, v))
                    visited.add((u, v))
        return answer