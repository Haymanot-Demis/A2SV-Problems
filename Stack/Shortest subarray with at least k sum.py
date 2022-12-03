class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        minLength = 100001
        none = True
        minSubarray = []

        for i in range(len(nums)):
            length = 0
            subarraySum = 0
            subarray = []
            j = i
            while j < len(nums) and subarraySum < k:
                length += 1
                subarraySum += nums[j]
                subarray.append(nums[j])
                j += 1
            if minLength > length and subarraySum >= k:
                minLength = length
                minSubarray = subarray
                none = False
        
        if none:
            return -1
        else:
            return [{"minsize" : minLength}, {"minSubarray" : minSubarray}]
    
mySolution = Solution()
print(mySolution.shortestSubarray([1,2,3],4))