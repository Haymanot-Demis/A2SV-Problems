class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(nums, left, right, k):
            if left >= right:
                return
            l = left
            r = right
            pivot = left
            while left < right:
                if pivot == right:
                    while left < pivot and nums[pivot] <= nums[left]:
                        left += 1
                    nums[pivot], nums[left] = nums[left], nums[pivot]
                    pivot = left                    
                else:
                    while right > pivot and nums[pivot] >= nums[right]:
                        right -= 1
                    nums[pivot], nums[right] = nums[right], nums[pivot]
                    pivot = right   
            if left == right == k - 1:
                return nums[k - 1]  
            left_subarr = quicksort(nums, l, pivot - 1, k)
            right_subarr = quicksort(nums, pivot + 1, r, k)
            return nums[k - 1]
        if len(nums) == 1:
            return nums[0]
        return quicksort(nums, 0, len(nums) - 1, k)