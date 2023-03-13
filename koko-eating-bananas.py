class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:         
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            hours = 0
            hours += sum([ceil(pile / mid) for pile in piles])
            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low