from bisect import bisect_left
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        the greater challenge of this problem is to keep track of the sequence of the numbers in increasing order and decreasing order which is very important to check the absolute diffrence between the min and max value in the subarray. In addition it is also used to move next minimum value. Then by saving the indexes of the elements in a min and max queue we can trace the next element we have to go. When the absolute diff is greater than the limit we have to go to the next greater or smaller number to narrow the gap which is found at the root of one of the queue/stack
        """
        left = 0
        right = 0
        length = len(nums)
        increasing_stack = []
        decreasing_stack = []
        max_subarr_length = -1

        while right < length:

            while increasing_stack and nums[increasing_stack[-1]] >= nums[right]:
                increasing_stack.pop()
            increasing_stack.append(right)

            while decreasing_stack and nums[decreasing_stack[-1]] <= nums[right]:
                decreasing_stack.pop()
            decreasing_stack.append(right)
            
            if abs(nums[increasing_stack[0]] - nums[decreasing_stack[0]]) > limit:
                if increasing_stack[0] < decreasing_stack[0]:
                    left = increasing_stack[0] + 1
                else:
                    left = decreasing_stack[0] + 1

                index_to_insert = bisect_left(increasing_stack, left)
                increasing_stack = increasing_stack[index_to_insert:]
                index_to_insert = bisect_left(decreasing_stack, left)
                decreasing_stack = decreasing_stack[index_to_insert:]
            else:
                max_subarr_length = max(max_subarr_length, right - left + 1)
                right += 1
        return max_subarr_length


     

