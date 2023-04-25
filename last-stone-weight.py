class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        while stones[-2]:
            stones[-1] -= stones[-2]
            stones[-2] = 0
            stones.sort()
        return stones[-1]