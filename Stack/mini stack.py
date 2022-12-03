class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack):
            return self.stack.pop()
        return None      

    def getMin(self) -> int:
        if len(self.stack):
            minVal = self.top()
            for num in self.stack:
                if minVal > num:
                    minVal = num
            return minVal
        return None

            
    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]
        return None
        
