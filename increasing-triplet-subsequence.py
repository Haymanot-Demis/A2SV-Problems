class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        use two variables to keep track of two increaing numbers then look for the third number. if we find a number that is greater that both of them it is guaranted that we got two increasing numbers some where, so we got Increasing Triplet Subsequence. 
        """
        first_smallest = float("inf")
        second_smallest = float("inf")
        for num in nums:
            if num <= first_smallest:
                first_smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        return False