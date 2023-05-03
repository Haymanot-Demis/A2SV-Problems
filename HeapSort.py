class Solution:
    #Heapify function to maintain heap property.
    def swap(self, arr, indx1, indx2):
        arr[indx1], arr[indx2] = arr[indx2], arr[indx1]
    def heapify(self,arr, n, i):
        # code here
        left = i * 2 + 1
        right = left + 1
        
        if left < n:
            largest = i 
            if arr[largest] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            
            if largest != i:
                self.swap(arr, largest, i)
                self.heapify(arr, n, largest)
    
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        last_parent = n // 2 - 1
        for parent in range(last_parent, -1, -1):
            self.heapify(arr, n, parent)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, len(arr))
        
        n = len(arr)
        while n:
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            n -= 1
            self.heapify(arr, n, 0)