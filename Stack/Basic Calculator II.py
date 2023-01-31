class Solution:
    def calculate(self, s: str) -> int:
        # given string as prefix we have to change to post fix using stack
        s = s.replace(" ", "")
        infix = []
        left = 0
        right = 1
        array = []
        array.append("12")
        while right < len(s):
            if s[right] == "/" or s[right] == "*" or s[right] == "+" or s[right] == "-":
                infix.append(s[left:right])
                infix.append(s[right])
                left = right + 1
            right += 1
        infix.append(s[left:])
        postfix = self.infixToPostfix(infix)
        stack = []
        for char in postfix:
            if char.isdigit() or char[1:].isdigit():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(str(self.calculator(operand2, operand1, char)))
        return int(stack[-1])

    def calculator(self, x, y, op):
        if op == "*":
            return int(x) * int(y)
        elif op == "/":
            if int(x) / int(y) < 0:
                return -(abs(int(x)) // abs(int(y)))
            return int(x) // int(y)
        elif op == "+":
            return int(x) + int(y)
        else:
            return int(x) - int(y)

    def infixToPostfix(self, infix: list):
        stack = []
        postfix = []
        unaryope = False
        for char in infix:
            if char.isdigit() or char[1:].isdigit():
                if unaryope:
                    char = -((int(char)))
                    unaryope = False
                postfix.append(str(char))
            else:
                if char == "-":
                    char = "+"
                    unaryope = True
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[-1] != "(":
                        postfix
                    stack.pop()
                elif stack and self.opPrecedence(stack[-1], char):
                    postfix.append(stack.pop())
                    stack.append(char)
                else:
                    stack.append(char)
        for op in stack[::-1]:
            postfix.append(op)
        return postfix

    def opPrecedence(self, *operators):
        operators = list(operators)
        for indx in range(len(operators)):
            if operators[indx] == "*" or operators[indx] == "/":
                operators[indx] = 1
            elif operators[indx] == "+" or operators[indx] == "-":
                operators[indx] = 0
        return operators[0] >= operators[1]
