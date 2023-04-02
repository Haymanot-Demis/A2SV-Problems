class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(indx, subset, subsets):
            if indx == len(nums):
                elems = []
                i = 0 
                while subset:
                    if subset & 1:
                        elems.append(nums[i])
                    subset >>= 1
                    i += 1
                subsets.append(elems)
                return 
            backtrack(indx + 1, subset | (1 << indx), subsets)
            backtrack(indx + 1, subset, subsets)
        subsets = []
        backtrack(0, 0, subsets)
        return subsets