class MyCircularDeque:

    def __init__(self, k: int):
        self.__deque = list()
        self.__size = k

    def insertFront(self, value: int) -> bool:
        if len(self.__deque) <= self.__size:
            self.__deque.append(value)
            print(self.__deque, len(self.__deque) <= self.__size)
            return True
        else:  
            return False        

    def insertLast(self, value: int) -> bool:
        if len(self.__deque) <= self.__size:
            self.__deque.insert(0, value)
            print(self.__deque, len(self.__deque) <= self.__size)
            return True
        else:
            return False        

    def deleteFront(self) -> bool:
        if len(self.__deque) != 0:
            self.__deque.pop()
            print(self.__deque)
            return True
        else:
            return False        

    def deleteLast(self) -> bool:
        if len(self.__deque) != 0:
            self.__deque.pop(0)
            print(self.__deque)
            return True
        else:
            return False    
        

    def getFront(self) -> int:
        self.__deque[-1]

    def getRear(self) -> int:
        self.__deque[0]

    def isEmpty(self) -> bool:
        return bool(len(self.__deque) == 0)
        

    def isFull(self) -> bool:
        return bool(len(self.__deque) == self.__size)


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
param_1 = obj.insertLast(1)
param_2 = obj.insertLast(2)
param_3 = obj.insertFront(3)
param_4 = obj.insertFront(4)
param_5 = obj.getRear()
param_6 = obj.isFull()
param_7 = obj.deleteLast()
param_9 = obj.insertFront(4)
param_10 = obj.getFront()

print([param_1, param_2, param_3, param_4, param_5, param_6, param_7,param_9,param_10])
