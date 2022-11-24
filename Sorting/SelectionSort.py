class Solution: 
    def select(self, arr, i):
        # code here 
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
            
        return min
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n - 1):
            minIdx = self.select(arr, i)
            if minIdx != i:
                arr[minIdx], arr[i] = arr[i], arr[minIdx]
            

mySolution = Solution()
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mySolution.selectionSort(arr, len(arr))
print(arr)
