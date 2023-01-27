class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [-1]*length
        stack = []
        for indx in range(length*2):
            while stack:
                if nums[indx % length] > nums[stack[-1] % length]:
                    answer[stack.pop()] = nums[indx % length]
                elif (indx % length) == stack[-1]:
                    stack.pop()
                else:
                    break
            stack.append(indx % length)
            
        return answer
