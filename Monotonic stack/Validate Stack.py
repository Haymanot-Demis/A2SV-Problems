class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        nums = [-1]
        pushedpointer = 0
        poppedpointer = 0
        length = len(pushed)
        while pushedpointer < length and poppedpointer < length:
            while pushedpointer < length and nums[-1] != popped[poppedpointer]:
                nums.append(pushed[pushedpointer])
                pushedpointer += 1
            
            while poppedpointer < length and nums[-1] == popped[poppedpointer]:
                nums.pop()
                poppedpointer += 1

        if poppedpointer == length:
            return True
        else:
            False