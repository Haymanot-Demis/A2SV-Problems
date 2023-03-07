class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monoton_stack = [] # decreasing
        mins = [0]*len(nums)
        mins[0] = nums[0]
        for indx in range(1, len(nums)):
            mins[indx] = min(mins[indx - 1], nums[indx])

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == mins[i]:
                continue
            while monoton_stack and monoton_stack[-1] < nums[i]:
                if monoton_stack[-1] > mins[i]:
                    return True
                monoton_stack.pop()
            if not monoton_stack or monoton_stack[-1] > nums[i]:
                monoton_stack.append(nums[i])

        return False