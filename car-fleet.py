class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPositionVsSpeed = zip(position, speed)
        carPositionVsSpeed = sorted(carPositionVsSpeed, reverse=True)
        prevArrivalTime = -1
        fleets = 0
        for pair in carPositionVsSpeed:
            currArrivalTime = (target - pair[0])/pair[1]
            if currArrivalTime > prevArrivalTime:
                fleets += 1
                prevArrivalTime = currArrivalTime
        
        return fleets


        return 0