class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_board1 = 0 #for +ves
        nums_board2 = 0 #for -ves
        for num in nums:
            if num >= 0:
                nums_board1 ^= (1 << num)
            else:
                nums_board2 ^= (1 << -num)
        if nums_board1:
            return int(log2(nums_board1))
        return -int(log2(nums_board2))