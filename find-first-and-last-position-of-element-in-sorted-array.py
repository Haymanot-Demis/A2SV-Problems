class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right = len(nums) - 1
        left = 0
        start = -1
        end = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                start = self.bisect_left(nums, mid, left, target)
                end = self.bisect_right(nums, mid, right, target)
                return [start, end]
        return [-1, -1]
        
    def bisect_left(self,nums, mid, left, target):
        right = mid
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target and (mid == left or nums[mid - 1] < target):
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return mid

    def bisect_right(self,nums, mid, right, target):
        left = mid
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target and (mid == right or nums[mid + 1] > target):
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return mid