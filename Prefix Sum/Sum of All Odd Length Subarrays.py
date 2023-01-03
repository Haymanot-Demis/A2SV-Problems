class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        # the core idea behind this problem is counting the number of times an element can exist in the odd length subarrays
        length = len(arr)
        arr[0] = (((0+1)*(length - 0) + 1) // 2)*arr[0] # the number of times the first element exists in the odd length subarrays based on the formula ((index+1)*(length - index) + 1) // 2
        for i in range(1, length):
            freq = ((i+1)*(length - i) + 1) // 2
            arr[i] = arr[i]*freq + arr[i-1]
        return arr[-1] 