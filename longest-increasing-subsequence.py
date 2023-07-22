class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = defaultdict(lambda : 1)

        for i in range(len(nums)):
            temp_memo = defaultdict(lambda : 1, memo)
            temp_memo[i] = 1
            for indx, count in memo.items():
                if nums[i] > nums[indx]:
                    temp_memo[i] = max(temp_memo[i], count + 1)
            memo = temp_memo
        
        lengths = temp_memo.values()
        return max(lengths)