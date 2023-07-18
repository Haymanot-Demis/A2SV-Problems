class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        subsequences = defaultdict(lambda: 1, {(1, nums[1] - nums[0]):2})
        for right in range(2, len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                subsequences[(right, diff)] = subsequences[(left, diff)] + 1 
        subseq_lengths = subsequences.values()
        return max(subseq_lengths)