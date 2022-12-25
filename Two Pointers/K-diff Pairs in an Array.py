class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        left = 0
        right = 1
        nums.sort()
        numsLength = len(nums)
        pairList = []
        while left < (numsLength - 1) and right < numsLength:
            if right == left:
                right += 1
            if abs(nums[right] - nums[left]) > k:
                left += 1
            elif abs(nums[right] - nums[left]) < k:
                right += 1
            elif (abs(nums[right] - nums[left]) == k):
                if (nums[right], nums[left]) not in pairList and (nums[left], nums[right]) not in pairList:
                    pairList.append((nums[right], nums[left]))
                right += 1
                left += 1
                
        return len(pairList)