class Solution:
    def shortestSubarray2(self, nums: list[int], k: int) -> int: #time limit exceeded
        minLength = 100001
        none = True
        listLength = len(nums)
        for i in range(listLength):
            length = 0
            subarraySum = 0
            j = i
            while j < listLength and subarraySum < k:
                length += 1
                subarraySum += nums[j]
                j += 1
            if minLength > length and subarraySum >= k:
                minLength = length
                none = False
            listLength = len(nums)
       
            
        if none:
            return -1
        else:
            return minLength
        
    def shortestSubarray(self, nums: list[int], k: int) -> int: #time limit exceeded
        minLength = len(nums) + 1
        for i in range(len(nums)):
            if i == 0:
                pass
            else:
                nums[i] += nums[i-1]
            subarraySum = nums[i]
            minSubarraySum = nums[i]
            length = i + 1
            j = 0
            curr = nums[j]
            while j < i:
                if subarraySum - curr >= k:
                    length = i - j
                    minSubarraySum = subarraySum - curr
                j += 1
                curr = nums[j]
            if length < minLength and minSubarraySum >= k:
                minLength = length
        
        if minLength == len(nums) + 1:
            return -1
        else:
            return minLength

    
mySolution = Solution()
print(mySolution.shortestSubarray([1,2,3],4))