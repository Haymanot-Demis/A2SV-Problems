class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = list(map(lambda pile : -pile, piles))
        heapify(heap)

        for _ in range(k):
            pile = heappop(heap) 
            pile += (-pile // 2)
            if pile:
                heappush(heap, pile)

        return sum([-pile for pile in heap])