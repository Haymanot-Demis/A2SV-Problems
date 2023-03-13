class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canBeShipped(capacity, length, high, low):
            days = 0
            indx = 0
            while indx < length:
                weight = 0
                while indx < length and weight + weights[indx] <= capacity: 
                    weight += weights[indx]
                    indx += 1
                days += 1
            
            return days

        length = len(weights)
        low = max(weights)
        high = sum(weights)
        min_possible_weight = high

        while low <= high:
            mid = low + (high - low) // 2
            days_to_ship = canBeShipped(mid, length, high, low)

            if days_to_ship > days:
                low = mid + 1
            elif days_to_ship <= days:
                min_possible_weight = min(min_possible_weight, mid)
                high = mid - 1

        return min_possible_weight