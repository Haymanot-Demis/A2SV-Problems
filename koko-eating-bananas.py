class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isFeasible(k, h):
            hours = 0
            for pile in piles:
                if pile <= k:
                    hours += 1
                else:
                    hours += ceil(pile / k)
                if hours > h:
                    return False
            return True

        low = 1
        high = max(piles)
        while low <= high:
            mid = low + (high - low) // 2
            if isFeasible(mid, h):
                high = mid - 1
            else:
                low = mid + 1
        return low