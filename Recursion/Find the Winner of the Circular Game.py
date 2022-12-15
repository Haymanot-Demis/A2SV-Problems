class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = CircularQueue(n)
        while(queue.size() != 1):
            self.removeNumber(queue, k)
            print(queue)
        return queue.top()
    
    def removeNumber(self, peoples, k):
        if k == 1:
            peoples.pop()
            return peoples
        peoples.next()
        self.removeNumber(peoples, k - 1)
    
class CircularQueue:
    def __init__(self, size):
        self.__queue = list()
        for i in range(1, size + 1):
            self.__queue.append(i)
        self.__top = 0
    
    def next(self):
        self.__top += 1
        if self.__top >= len(self.__queue):
            self.__top = 0

    def top(self):
        if self.__queue:
            return self.__queue[self.__top]

    def pop(self):
        if self.__queue:
            self.__queue.pop(self.__top)
            # self.__top += 1
            if self.__top >= len(self.__queue):
                self.__top = 0
        
    def size(self):
        return len(self.__queue)