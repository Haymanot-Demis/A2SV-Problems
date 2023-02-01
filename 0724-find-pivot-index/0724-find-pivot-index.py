class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        """
        the bruth force solution of this problem is take an index as piot index then add the numbers to the left and compare it with the sum of the numbers to the right until the end of the list if we get left sum and right sum we return that index as pivot index 
        but the efficient algorithm is use pivot index as a pointer and first compute left sum and right sum and consecutively add the value at the pivot index to the left_sum and subtract form right sum until we get left_sum and right_sum eqaul then we return pivot index if we get else return -1
        """
        pivot_index = 0
        left_sum = 0
        right_sum = sum(nums[pivot_index + 1:])
        
        if left_sum == right_sum:
            return pivot_index
        pivot_index += 1

        while pivot_index < len(nums):
            left_sum += nums[pivot_index - 1]
            right_sum -= nums[pivot_index]
            if left_sum == right_sum:
                return pivot_index
            pivot_index += 1
        return -1
            

