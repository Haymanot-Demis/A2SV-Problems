class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        length = len(houses)
        radiuses = [inf] * length 
        for i in range(length):
            pos = bisect_left(heaters, houses[i])
            radiuses[i] = min(abs(heaters[(pos) % len(heaters)] - houses[i]), abs(heaters[(pos - 1) % len(heaters)] - houses[i]))

        return max(radiuses)