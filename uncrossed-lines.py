class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    memo[(i, j)] = memo[(i - 1, j - 1)] + 1
                else:
                    memo[(i, j)] = max(memo[(i - 1, j)], memo[(i, j - 1)])
                
        return memo[(len(nums1) - 1, len(nums2) - 1)]