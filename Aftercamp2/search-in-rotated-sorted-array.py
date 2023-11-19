class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    return self.binarySearch(nums, left, mid, target)
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    return self.binarySearch(nums, mid, right, target)
                else:
                    right = mid - 1
        return -1
    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1