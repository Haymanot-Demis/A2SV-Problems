class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))

        valid_splits = 0
        for i in range(len(nums) - 1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                valid_splits += 1
        return valid_splits