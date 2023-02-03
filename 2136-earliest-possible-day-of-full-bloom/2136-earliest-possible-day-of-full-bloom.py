class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantingVsGrowingTime = list(zip(plantTime, growTime))
        plantingVsGrowingTime.sort(key=lambda x : x[1], reverse=True)

        totalPlantingTime = 0
        bloomingTime = 0
        for indx in range(len(plantTime)):
            totalPlantingTime += plantingVsGrowingTime[indx][0]
            bloomingTime = max(totalPlantingTime + plantingVsGrowingTime[indx][1], bloomingTime)
        
        return bloomingTime
        