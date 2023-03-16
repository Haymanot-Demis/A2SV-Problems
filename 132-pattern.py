class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        stack = []
        smaller = []
        stack.append(0)
        smaller.append(nums[0])
        for i in range(1, length):
            smaller.append(min(smaller[-1], nums[i]))
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                if smaller[stack[-1]] < nums[i]:
                    return True
            stack.append(i)

        return False