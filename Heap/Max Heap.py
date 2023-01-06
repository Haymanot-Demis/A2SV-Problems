class MaxHeap:
    def __init__(self, array=[]) -> None:
        self.heap = array
        self.buildHeap()
        print(self.heap)

    def buildHeap(self):
        parentIndx = len(self.heap)//2 - 1
        for i in range(parentIndx, -1, -1):
            self.heapify(i, len(self.heap))
    
    def heapify(self, indx, endIndx):
        left = indx*2 + 1
        right = indx*2 + 2
        largeIndx = indx
        length = endIndx
        if left < length and self.heap[left] > self.heap[largeIndx]:
            largeIndx = left
        if right < length and self.heap[right] > self.heap[largeIndx]:
            largeIndx = right
        if largeIndx != indx:
            self.heap[largeIndx], self.heap[indx] = self.heap[indx], self.heap[largeIndx]
            self.heapify(largeIndx, length)        

    def shiftUp(self, indx):
        parentIndex =(indx - 1)//2
        if parentIndex >= 0 and self.heap[parentIndex] < self.heap[indx]:
            self.heap[parentIndex], self.heap[indx] = self.heap[indx], self.heap[parentIndex]
            self.shiftUp(parentIndex)

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap) - 1)

    def heappop(self):
        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        value = self.heap.pop()
        self.heapify(0, len(self.heap))
        return value
    def remove(self, value):
        i = 0
        length = len(self.heap)
        while i < length and self.heap[i] != value:
            i+=1
        if i == length:
            print(value, "doesn't exist in the heap")
            return
        
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        value = self.heap.pop()
        for j in range(i, -1, -1):
            self.heapify(j, len(self.heap))
        return value
    
    def printHeap(self):
        print(self.heap)

    def modify(self, valueTobeModified, newvalue):
        i = 0
        length = len(self.heap)
        while i < length and self.heap[i] != valueTobeModified:
            i+=1
        if i >= length:
            print(valueTobeModified, "doesn't exist in the heap")
        
        self.heap[i] = newvalue
        for j in range(i, -1, -1):
            self.heapify(j, len(self.heap))

    def heapSort(self):
        sortedHeap = []
        while self.heap:
            sortedHeap.insert(0,self.heappop())
        print(sortedHeap)
    def heapSortInplace(self):
        for i in reversed(range(len(self.heap))):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify(0, i)
        print(self.heap)

heap = MaxHeap([6, 3, 5, 7, 2, 4, 10, 9])
heap.heapSortInplace()

# heap.insert(10)
# heap.printHeap()
# heap.modify(6,12)
# heap.heapSortInplace()
# print(heap.remove(9))
# heap.heapSort()
# heap.printHeap()
# print(heap.heappop())
# heap.printHeap()
# heap.printHeap()


