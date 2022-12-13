class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # sort the cars based on their position with their respective speed
        # print(self.insertionSort(position, speed))
        posSpeedDict = zip(position, speed)
        sortedDict = dict(sorted(posSpeedDict, reverse=True))

        lastArrivalTime = 0
        numOfFleets = 0
        for pos, speed in sortedDict.items():
           currentArrivalTime = (target - pos)/speed
           if currentArrivalTime > lastArrivalTime:
               numOfFleets += 1     
               lastArrivalTime = currentArrivalTime
            
        return numOfFleets

    def insertionSort(self, pos:list[int], speed:list[int])-> list[int]:

        for step in range(1, len(pos)):
            key = pos[step]
            currSpeed = speed[step]
            j = step - 1 
            while j >= 0 and key > pos[j]:
                pos[j + 1] = pos[j]
                speed[j + 1] = speed[j]
                j = j - 1
            
            pos[j + 1] = key
            speed[j + 1] = currSpeed
        return [pos, speed]

    
mySolution = Solution()
print(mySolution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
    