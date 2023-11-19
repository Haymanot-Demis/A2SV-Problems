class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def missing(indx):
            return arr[indx] - indx -1 

        arr.append(arr[-1] + 1)
        left = 0
        right = len(arr) - 1


        while left < right:
            mid = left + (right - left) // 2

            missed = missing(mid)

            if missed >= k:
                right = mid
            else:
                left = mid + 1
        print(left)
        return arr[left - 1] + k - missing(left - 1)