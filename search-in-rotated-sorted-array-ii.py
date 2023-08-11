class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1

            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = left + (right - left) // 2

            if nums[left] == target or nums[mid] == target or nums[right] == target:
                return True
            # if nums[left] == nums[mid] == nums[right]:
            #     return self.search(nums[:mid], target) or self.search(nums[mid + 1:], target)
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    return self.binarySearch(nums, left, mid, target)
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    return self.binarySearch(nums, mid, right, target)
                else:
                    right = mid - 1
        return False

    def binarySearch(self, nums, left, right, target):
        print(left, right)
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return True
        
        return False