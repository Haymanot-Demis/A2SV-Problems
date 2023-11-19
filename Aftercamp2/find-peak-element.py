class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        has two approach 
        1. Brute force: just iterating over the elements and check is the current number is peak
        2. using binary search to find the peak element based on the truth nums[i] != nums[i + 1]
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1
        
        left = 1
        right = len(nums) - 2

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        