class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        the solution is XORing all the numbers to get the XOR of the two numbers and then categorize to two groups, one which have set bit at one the set bit of the XOR result. This bit is selected aribitrarily then we categorize the numbers which have set bit and don't have set bit at that bit.
        """
        XOR = 0 # if we xor all of the numbers we will get XOR of the two numbers
        for num in nums:
            XOR ^= num
        # I am going to use the first set bit
        set_bit = XOR & -XOR
        first = 0
        second = 0 
        for i in nums:
            if set_bit & i:
                first ^= i
            else:
                second ^= i
        
        return [first, second]