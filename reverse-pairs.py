class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left, right, l1, l2):
            p1, p2, prev, count, total = 0, 0, 0, 0, 0
            while p1 < l1 and p2 < l2:
                if left[p1] > 2 * right[p2]:
                    count += 1
                    p2 += 1
                else:
                    total += prev + count
                    prev += count
                    count = 0
                    p1 += 1
            total += (l1 - p1) * (prev + count)

            p1, p2 = 0, 0
            merged = []
            while p1 < l1 and p2 < l2:
                if left[p1] > right[p2]:
                    merged.append(right[p2]) 
                    p2 += 1
                else:
                    merged.append(left[p1]) 
                    p1 += 1
            merged.extend(left[p1:])
            merged.extend(right[p2:])
            return merged, total      

        def mergeSort(arr, l, r):
            if r - l == 1:
                return arr[l:r], 0
            mid = l + (r - l) // 2
            left, pair_count1 = mergeSort(arr, l, mid)
            right, pair_count2 = mergeSort(arr, mid, r)
            merged, pair_count3 = merge(left, right, len(left), len(right))
            return merged, pair_count1 + pair_count2 + pair_count3

        sorted_arr, count = mergeSort(nums, 0, len(nums))
        return count