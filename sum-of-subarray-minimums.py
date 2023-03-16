class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left_monotonic = []
        right_monotonic = []
        hashtable = defaultdict(lambda:[0,0])

        for i,num in enumerate(arr):
            while left_monotonic and arr[left_monotonic[-1]] >= num:
                hashtable[i][0] += hashtable[left_monotonic.pop()][0] + 1
            left_monotonic.append(i)

        for i in range(len(arr) - 1, -1, -1):
            while right_monotonic and arr[right_monotonic[-1]] > arr[i]:
               hashtable[i][1] += hashtable[right_monotonic.pop()][1] + 1
            right_monotonic.append(i)
        min_sum = 0

        for i in range(len(arr)):
            min_sum += arr[i] * (hashtable[i][0] + 1) * (hashtable[i][1] + 1)
        return min_sum % (10 ** 9 + 7)