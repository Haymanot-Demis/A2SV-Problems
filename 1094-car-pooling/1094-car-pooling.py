from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        by iterating from the first start point up to the last destination add when we get the passenger to be picked up and subtract when the passenger drop off
        """
        pickingUpPoints = defaultdict(int)
        dropOffPoints = defaultdict(int)
        for trip in trips:
            pickingUpPoints[trip[1]] += trip[0]    
            dropOffPoints[trip[2]] += trip[0]
        currentPassengers = 0
        for point in  sorted(set(pickingUpPoints.keys()) | set(dropOffPoints.keys())):
            if pickingUpPoints.get(point, 0) != 0:
                currentPassengers += pickingUpPoints[point]
            if dropOffPoints.get(point, 0) != 0:
                currentPassengers -= dropOffPoints[point]
            if currentPassengers > capacity:
                return False
            
            
        return True