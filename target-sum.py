class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        memo[nums[0]] = 1
        memo[-nums[0]] += 1

        for i in range(1, len(nums)):
            temp_memo = defaultdict(int)
            for sum, count in memo.items():
                temp_memo[sum + nums[i]] += count
                temp_memo[sum - nums[i]] += count
            memo = temp_memo
        
        return memo[target]