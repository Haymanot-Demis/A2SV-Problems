class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        indx = 0
        while indx < length:
            reverse = int(str(nums[indx])[::-1])
            nums.append(reverse)
            indx += 1

        return len(set(nums))