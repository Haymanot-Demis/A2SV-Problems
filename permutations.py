class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """"
        
        """
        permutations = []
        def backtrack(container, permutation):
            if not container:
                permutations.append(permutation)
                return 
            for num in container:
                backtrack(container - set([num]), permutation + [num])

        backtrack(set(nums), [])

        return permutations