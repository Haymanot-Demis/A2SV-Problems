from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sorted_window = SortedList(nums[:indexDiff])

        for i in range(len(nums) - 1):
            if i + indexDiff < len(nums):
                sorted_window.add(nums[i + indexDiff])
            sorted_window.remove(nums[i])
            low = 0
            high = len(sorted_window) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if abs(sorted_window[mid] - nums[i]) > valueDiff and sorted_window[mid] < nums[i]:
                    low = mid + 1
                elif abs(sorted_window[mid] - nums[i]) > valueDiff:
                    high = mid - 1
                else:
                    return True

        return False