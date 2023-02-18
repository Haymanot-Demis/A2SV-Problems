class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        triplets = set()
        nums.sort()
        for left in range(length):
            middle = left  + 1
            right = length - 1
            while middle < right and (nums[left] <= 0) and nums[right]  >= 0:
                triplet_sum = nums[left] + nums[middle] + nums[right] 
                if triplet_sum == 0 and (nums[left], nums[middle], nums[right]) not in triplets:
                    triplets.add((nums[left], nums[middle], nums[right])) 
                elif triplet_sum < 0:
                    middle += 1
                else:
                    right -= 1
        return triplets