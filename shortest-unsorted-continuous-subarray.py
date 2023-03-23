class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        stack = []
 
        left = length
        right = -1

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] <= num:
                stack.pop()
            if stack:
                right = i
            stack.append(i)
      
        if left == length and right == -1:
            return 0
        return right - left  + 1