class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        decodeString = ''
        self.decodeStringHelper(s, 0, stack)
        decodeString = ''.join(char for char in stack)
        return decodeString

    def decodeStringHelper(self, s:str, indx:int, stack:List[str]):
        if indx >=len(s):
            return
        if (ord(s[indx]) <= 122 and ord(s[indx]) >= 97) or s[indx] == '[':
            stack.append(s[indx])
        elif s[indx].isnumeric():
            if stack and stack[-1].isnumeric():
                stack.append(stack.pop() + s[indx])
            else:
                stack.append(s[indx])
        elif s[indx] == ']':
            substring = ''
            decodesSubString = ''
            # call a recursive function to get the substring 
            substring = self.getSubstring(stack, substring)
            stack.pop()
            repeat = int(stack.pop())
            # call a recursive function to decode the substring basef in the repeater
            decodesSubString = self.decoder(decodesSubString, substring, repeat)
            print("35", decodesSubString)
            stack += list(decodesSubString)
        self.decodeStringHelper(s, indx + 1, stack)

    def getSubstring(self, stack, substring:str) -> str:
        if stack[-1] == '[':
            return substring
        substring = stack.pop() + substring
        return self.getSubstring(stack, substring)

    def decoder(self, decoded, substring, repeat):
        if repeat < 1:
            return decoded
        decoded += substring
        return self.decoder(decoded, substring, repeat - 1)
        


        

        