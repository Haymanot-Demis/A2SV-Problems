# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 1
        first_bad = n
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid) and (mid == n - 1 or isBadVersion(mid + 1)):
                return mid + 1
            if isBadVersion(mid) and (mid == 1 or not isBadVersion(mid - 1)):
                return mid
            elif not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1