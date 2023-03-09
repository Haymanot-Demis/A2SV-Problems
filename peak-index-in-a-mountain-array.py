class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        low = 0 
        high = length - 1
        while low <= high:
            mid = low + (high - low) // 2
            if mid == 0:
                low = mid + 1
                continue
            elif mid == length - 1:
                high = mid - 1
                continue
            if  arr[mid - 1] < arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                high = mid - 1
            else:
                return mid
        return low