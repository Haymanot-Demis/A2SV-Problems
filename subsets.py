class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        def findSubsets(indx, subset):
            subsets.add(tuple(subset))
            if indx == len(nums):
                return 
            findSubsets(indx + 1, subset | set([nums[indx]]))
            findSubsets(indx + 1, subset)
        findSubsets(0, set())
        return subsets