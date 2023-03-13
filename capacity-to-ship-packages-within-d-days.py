class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canBeShipped(capacity, expected):
            days = 1
            indx = 0
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > capacity:
                    days += 1
                    curr_weight = 0
                curr_weight += weight
                if days > expected:
                    return days

            return days

        low = max(weights)
        high = sum(weights)
        min_possible_weight = high

        while low <= high:
            mid = low + (high - low) // 2
            days_to_ship = canBeShipped(mid, days)

            if days_to_ship > days:
                low = mid + 1
            elif days_to_ship <= days:
                min_possible_weight = min(min_possible_weight, mid)
                high = mid - 1

        return min_possible_weight