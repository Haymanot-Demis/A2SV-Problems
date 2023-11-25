class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        for i in range(1, n):
            prefix[i] += (nums[i] - nums[i - 1]) * i + prefix[i - 1]
            suffix[n - i - 1] += abs(nums[n - i - 1] - nums[n - i]) * i + suffix[n - i]
      
      
        result = []

        for i in range(n):
            result.append(prefix[i] + suffix[i])
        
        return result