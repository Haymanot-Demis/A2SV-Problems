class Solution:
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