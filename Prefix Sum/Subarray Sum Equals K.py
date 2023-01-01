#time 60
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefixSum = [nums[0]]
        length = len(nums)
        count = 0
        countDict = dict()
        countDict[prefixSum[0]] = 1
        if prefixSum[0] == k:
            count += 1
        for i in range(1, length):
            prefixSum.append(prefixSum[i-1] + nums[i])
            if prefixSum[i] == k:
                count += 1
            count += countDict.get(prefixSum[i] - k, 0)
            countDict[prefixSum[i]] = countDict.get(prefixSum[i], 0) + 1
        
        return count
