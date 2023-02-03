from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return len(counter) if counter.get(0, 0) == 0 else len(counter) - 1
    
