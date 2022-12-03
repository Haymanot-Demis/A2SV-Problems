class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        nums.sort(reverse = True)
        return str(nums[k - 1])
        

mySolution = Solution()
mySolution.kthLargestNumber(["3", "1", "10", "2"], 2)