class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        counter = 0
        counter += hashmap[nums[0] - goal]
        hashmap[nums[0]] += 1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            counter += hashmap[nums[i] - goal]
            hashmap[nums[i]] += 1
        return counter