class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def backtrack(curr_num, combination):
            if len(combination) == k:
                combinations.append(combination)
                return 
            if curr_num > n:
                return 
    
            backtrack(curr_num + 1, combination + [curr_num])
            backtrack(curr_num + 1, combination)
        backtrack(1, [])
        return combinations