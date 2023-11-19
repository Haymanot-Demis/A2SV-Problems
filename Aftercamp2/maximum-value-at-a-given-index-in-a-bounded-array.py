class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def totalSum(indx, num):
            left = max(num - indx, 1)
            right = max(num - (n - indx - 1), 1)

            total_sum = (left + num) * (num - left + 1) // 2 + (right + num) * (num - right + 1) // 2  
            if indx >= num:
                total_sum += indx - num + 1

            if n - indx - 1 >= num:
                total_sum += (n - indx - 1) - num + 1

            return total_sum - num
        
        left = 1
        right = maxSum

        while left <= right:
            mid = left + (right - left) // 2

            arr_sum = totalSum(index, mid)
            # print(left, right, mid, arr_sum)

            if arr_sum <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
            
        return right
                 