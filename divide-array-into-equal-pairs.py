class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        binary = 0
        for num in nums:
            binary ^= (1 << num)
        return binary == 0