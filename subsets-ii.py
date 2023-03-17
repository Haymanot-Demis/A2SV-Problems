class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(indx, subset, subsets):
            if len(nums) == indx:
                subsets.add(tuple(subset))
                return
            backtrack(indx + 1, subset + [nums[indx]], subsets)
            backtrack(indx + 1, subset, subsets)
        subsets = set()
        backtrack(0, [], subsets)
        return subsets