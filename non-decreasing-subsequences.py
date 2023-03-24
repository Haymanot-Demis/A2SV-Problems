class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(indx, subsequence, flag, subsequences):
            if flag and len(subsequence) >= 2:
                subsequences.add(tuple(subsequence))
            if indx == len(nums):
                return subsequences

            if not subsequence or nums[indx] >= subsequence[-1]:
                backtrack(indx + 1, subsequence + [nums[indx]], True, subsequences)
                while indx < len(nums) - 1 and nums[indx] == nums[indx + 1]:
                    indx += 1
                backtrack(indx + 1, subsequence, False, subsequences)
            else:
                backtrack(indx + 1, subsequence, False, subsequences)

            return subsequences

        return backtrack(0, [], False, set())