class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        windowStart = 0
        windowEnd = k - 1
        Sum = sum(arr[:k-1])
        while windowEnd < len(arr):
            Sum += arr[windowEnd]
            if Sum/k >= threshold:
                print(arr[windowStart:windowEnd+1])
                count += 1
            windowEnd += 1
            Sum -= arr[windowStart]
            windowStart += 1
        
        return count