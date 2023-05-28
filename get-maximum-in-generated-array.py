class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(1, (n + 1) // 2 + 1):
            if 2 * i < (n + 1):
                nums[2 * i] = nums[i]
            if 2 * i + 1 < (n + 1):
                nums[2 * i + 1] = nums[i] + nums[i + 1]
                
        return max(nums)