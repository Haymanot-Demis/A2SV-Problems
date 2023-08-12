class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))
        prefix = [0] + prefix

        count = 0 if nums[0] >= k else 1

        for i in range(2, len(nums) + 1):
            left = 1
            right = i
            while left <= right:
                mid = left + (right - left) // 2
                if (prefix[i] - prefix[mid - 1]) * (i - mid + 1) >= k:
                    left = mid + 1
                else:
                    right = mid - 1
            count += max(i - left + 1, 0)
        return count