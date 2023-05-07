class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.min_heap, num)
        if len(self.min_heap) - 1 > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        while self.min_heap and self.max_heap and self.min_heap[0] < -self.max_heap[0]:
            num1 = heappop(self.min_heap)
            num2 = heappop(self.max_heap)
            heappush(self.min_heap, -num2)
            heappush(self.max_heap, -num1)

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()