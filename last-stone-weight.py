class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        the concept bbehind this is build a max heap then heappop the top 2 largest numbers and subtract them if the difference is more than 0 heappushit again, do this until one or no value remained in the list, then return the result, we should map the stones to -ve to make it max heap
        """
        if len(stones) == 1:
            return stones[0]
        stones = list(map(lambda x : -x, stones))
        heapify(stones)
        while len(stones) > 1:
            max1 = heappop(stones)
            max2 = heappop(stones)
            if max1 - max2:
                heappush(stones, max1 - max2)
                
        return -stones[0] if stones else 0