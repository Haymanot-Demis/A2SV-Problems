class MyQueue:
    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.isEmpty():
            for i in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


    def peek(self) -> int:
        if self.stack2.isEmpty():
            for i in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()


    def empty(self) -> bool:
        return self.stack1.isEmpty() and self.stack2.isEmpty()
    
class Stack:
    def __init__(self):
        self.stack = list()
    
    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        return None
            
    def peek(self):
        if len(self.stack):
            return self.stack[-1]
        return None
    
    def push(self, x):
        self.stack.insert(-1, x)
        # self.stack.append(x):
    
    def size(self) -> int:
        return len(self.stack)
    
    def isEmpty(self) -> bool:
        return bool(len(self.stack) == 0)




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()