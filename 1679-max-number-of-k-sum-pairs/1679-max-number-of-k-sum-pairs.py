from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            if hashmap[k - nums[i]] > 0:
                count += 1
                hashmap[k - nums[i]] -= 1
            else:
                hashmap[nums[i]] += 1
            
        return count


                
        