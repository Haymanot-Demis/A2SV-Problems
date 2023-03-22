class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr):
            p1, p2 = 0, 0
            l1, l2 = len(left_arr), len(right_arr)
            merged = []
            while p1 < l1 and p2 < l2:
                if left_arr[p1] <= right_arr[p2]:
                    merged.append(left_arr[p1])
                    p1 += 1
                else:
                    merged.append(right_arr[p2])
                    p2 += 1
            if p1 < l1:
                merged.extend(left_arr[p1:])
            else:
                merged.extend(right_arr[p2:])
            return merged

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = mergeSort(arr[:mid])
            right_half = mergeSort(arr[mid:])
            return merge(left_half, right_half)
        return mergeSort(nums)