class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = (n + 1)*n//2
        print(totalSum)
        prefixSum = [0]*(n + 1)
        for i in range(1, n + 1):
            prefixSum[i] += prefixSum[i - 1] + i
            if totalSum - prefixSum[i - 1] == prefixSum[i]:
                return i
        return -1
        
