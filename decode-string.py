class Solution:
    """
    go from right most of the given string to left
    if it is alphabetical add to the answer 
    if it is closing bracket we have to compute inner expression so call the recursive funtion
    if is opening bracket the next is number so take the number and mutiply the string and continue parsing
    """
    def decodeString(self, s: str) -> str:
        s = list(s)
        decodeString = self.decodeStringHelper(s)
        return ''.join(decodeString[::-1])

    def decodeStringHelper(self, stack:List[str]):
        ans = ""
        number = ""
        while stack:
            if stack[-1].isalpha():
                ans += stack.pop()
            elif stack[-1] == "]":
                stack.pop()
                ans += self.decodeStringHelper(stack)
            else: # it is nopening bracke and next numeric
                if stack[-1] == "[": stack.pop()# remove the opening bracket
                while stack and stack[-1].isnumeric():
                    number = stack.pop() + number
                print(number)
                ans = ans * int(number)
                return ans
        return ans