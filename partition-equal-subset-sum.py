class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        memo = set([nums[0], -nums[0]])

        for i in range(1, len(nums)):
            temp_memo = set()
            for value in memo:
                temp_memo.add(value + nums[i])     
                temp_memo.add(value - nums[i])
            memo = temp_memo
        return 0 in memo