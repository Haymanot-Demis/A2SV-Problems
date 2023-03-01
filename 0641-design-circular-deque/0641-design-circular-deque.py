class MyCircularDeque:

    def __init__(self, k: int):
        self.__deque = list()
        self.__size = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.length < self.__size:
            self.__deque.append(value)
            self.length += 1
            return True
            
        return False        

    def insertLast(self, value: int) -> bool:
        if self.length < self.__size:
            self.__deque.insert(0, value)
            self.length += 1
            return True
        return False        

    def deleteFront(self) -> bool:
        if self.length:
            self.__deque.pop()
            self.length -= 1
            return True
        return False        

    def deleteLast(self) -> bool:
        if self.length:
            self.__deque.pop(0)
            self.length -= 1
            return True
        return False    

    def getFront(self) -> int:
        if self.length:
            return self.__deque[-1]
        return -1

    def getRear(self) -> int:
        if self.length:
            return self.__deque[0]
        return -1

    def isEmpty(self) -> bool:
        return bool(self.length == 0)
        
    def isFull(self) -> bool:
        return bool(self.length == self.__size)
