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