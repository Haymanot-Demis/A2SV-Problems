class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        indx = 0
        while indx < length:
            num = nums[indx]
            reverse = 0
            while num >= 10:
                unit = num % 10
                num = num // 10
                reverse = reverse * 10 + unit
            reverse = reverse * 10 + num
            nums.append(reverse)
            indx += 1
            
        return len(set(nums))