class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last_seen_bit = [0] * 30
        n = len(nums)
        smallest_subarrays = [0] * n
        for index in range(n - 1, -1, -1):
            for bit_index in range(30):
                if nums[index] & (1 << bit_index):
                    last_seen_bit[bit_index] = index
            smallest_subarrays[index] = max(1, max(last_seen_bit) - index + 1)
        return smallest_subarrays