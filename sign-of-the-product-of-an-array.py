class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = prod(nums)
        if product > 0:
            return 1
        if product < 0:
            return -1
        return 0