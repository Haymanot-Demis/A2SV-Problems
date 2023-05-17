class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """"
        
        """
        permutations = []
        def backtrack(container, permutation, permutations):
            if not container:
                permutations.append(permutation)
                return
            
            for i,num in enumerate(container):
                backtrack(container[0:i] + container[i+1:], permutation + [num], permutations)

        backtrack(nums, [], permutations)
        return permutations