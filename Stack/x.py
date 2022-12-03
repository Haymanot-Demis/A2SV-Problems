class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        minLength = len(nums)
        none = True
        minSubarray = []
        while len(nums) != 0:
            length = 0
            subarraySum = 0
            subarray = []
            while subarraySum < k and len(nums) != 0:
                length += 1
                subarraySum += nums[-1]
                subarray.append(nums[-1])
                nums.pop()
            if minLength > length and subarraySum >= k:
                minLength = length
                minSubarray = subarray
                none = False

        if len(minSubarray) ==0:
            return -1
        return minLength
        # return [{"minsize" : minLength}, {"minSubarray" : minSubarray}]
    
mySolution = Solution()
print(mySolution.shortestSubarray([1],1))