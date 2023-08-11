class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        fair_pair_count = 0

        length = len(nums)
        nums.sort()
        
        for i in range(1, length):
            # min num I can use
            num = lower - nums[i]
            bottom = min(bisect_left(nums, num), i)
           
            # max num I can use
            num = upper - nums[i]
            top = min(i, bisect_right(nums, num))
            fair_pair_count += (top - bottom)

        return fair_pair_count