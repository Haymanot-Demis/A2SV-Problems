class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for lexeme in tokens:
            if lexeme in "+-*/":
                y = int(stack.pop())
                x = int(stack.pop())
                print(x, lexeme, y)
                stack.append(self.calc(x, y, lexeme))
            else:
                stack.append(lexeme)
        return stack[0]
    
    def calc(self, num1, num2, operator) -> int:
        print(type(num1), type(num2))
        if operator == '+':
            return num1 + num2
        elif operator == '-': 
            return num1 - num2
        elif operator == '*': 
            return num1 * num2
        elif operator == '/': 
            return num1 / num2
        