class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                if i - hash_table[nums[i]] <= k:
                    return True    
            hash_table[nums[i]] = i
        
        return False