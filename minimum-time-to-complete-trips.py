class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 1
        high = max(time) * totalTrips

        while low <= high:
            mid = low + (high - low) // 2

            trips = sum([mid // t for t in time])
            if trips >= totalTrips:
                high = mid - 1
            else:
                low = mid + 1
        return low