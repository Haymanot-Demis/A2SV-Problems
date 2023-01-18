class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        length = len(nums)
        stackLenCount = 0
        for i in range(length):
            if stackLenCount > 0:
                while length - i > k - stackLenCount and stack and stack[-1] > nums[i]:
                    stack.pop()
                    stackLenCount -= 1
                if stackLenCount < k:
                    stack.append(nums[i])
                    stackLenCount += 1
            elif stackLenCount == 0:
                stack.append(nums[i])
                stackLenCount += 1
        return stack