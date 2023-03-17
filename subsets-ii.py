class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(indx, subset, subsets):
            if len(nums) == indx:
                subsets.append(subset)
                return
            backtrack(indx + 1, subset + [nums[indx]], subsets)
            while indx< len(nums) - 1 and nums[indx] == nums[indx + 1]:
                indx += 1
            backtrack(indx + 1, subset, subsets)
        subsets = []
        backtrack(0, [], subsets)
        return subsets