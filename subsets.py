class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(indx, subset, subsets):
            if indx == len(nums):
                subsets.append(subset.copy())
                return 
            backtrack(indx + 1, subset + [nums[indx]], subsets)
            backtrack(indx + 1, subset, subsets)
        subsets = []
        backtrack(0, [], subsets)
        return subsets