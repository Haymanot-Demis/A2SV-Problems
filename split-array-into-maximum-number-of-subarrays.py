class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        """
        the minimum bitwise AND we could get is the AND of all the numbers 
        , to a min sum of score we need to have a minScore of zero so that the sum couldn't greater than the minScore, otherwise we have to keep all the numbers in one subarray 
        """

        min_score = nums[0]

        for num in nums:
            min_score &= num

        if min_score != 0:
            return 1

        prefix = nums[0]
        splits = 0
        i = 0
     
        while i < len(nums) - 1:
            prefix &= nums[i]
            if prefix == 0:
                splits += 1
                prefix = nums[i + 1]
            i += 1

        prefix &= nums[i]
        if prefix == 0:
            splits += 1

        return splits