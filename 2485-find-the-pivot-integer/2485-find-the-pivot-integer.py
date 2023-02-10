class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = n + 1
        rightSum = 0
        leftSum = 0
        while left < right:
            if leftSum < rightSum:
                left += 1
                leftSum += left
            else:
                right -= 1
                rightSum += right
        if leftSum == rightSum:
            return left
        else:
            return -1
