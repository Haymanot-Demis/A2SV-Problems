class Solution():
    """ 
    """
    def validParenthesis(self, string):
        stack = list()
        for operator in string:
            if operator == ')':
                if len(stack) == 0:
                    print("Stack empty but there is closing parethesis ')'")
                    return False
                elif stack.pop() != '(':
                    print("')' doesn't have a match")
                    return False
            elif operator == '}':
                if len(stack) == 0:
                    print("Stack empty but there is closing curly brace '}'")
                    return False
                elif stack.pop() != '{':
                    print("'}' doesn't have a match")
                    return False
            elif operator == ']':
                if len(stack) == 0:
                    print("Stack empty but there is closing angled bracket ']'")
                    return False
                elif stack.pop() != '[':
                    print("']' doesn't have a match")
                    return False
            else:
                stack.append(operator)
        
        if not (len(stack) == 0):
            print(stack)
        return bool(len(stack) == 0)


mySolution = Solution()
print(mySolution.validParenthesis('()(){}[]'))
            
