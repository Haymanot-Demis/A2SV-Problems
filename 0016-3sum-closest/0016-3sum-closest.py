class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        first sort the numbers given then take three pointers left, middle and right
        for each number at left we find any middle and right value that can give us a closest sum to the target 
        each time if current triplet sum is more closer to the target than previuos closest sum change it and the other point is increaing middle if sum less than target or decrease right if sum greater than target
        """
        length = len(nums)
        middle = 1
        right = length - 1
        closestSum = 300000
        nums.sort()
        for left in range(length):
            middle = left + 1
            right = length - 1
            while middle < right:
                tripletSum = nums[left] + nums[middle] + nums[right]
                if abs(closestSum - target) > abs(tripletSum - target):
                    closestSum = tripletSum
                if tripletSum > target:
                    right -= 1
                elif tripletSum < target:
                    middle += 1
                else:
                    closestSum = tripletSum
                    return closestSum
        return closestSum

