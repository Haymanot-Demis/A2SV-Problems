class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        container = set()
        for i in range(len(nums)):
            if nums[i] in container:
                return nums[i]
            container.add(nums[i])