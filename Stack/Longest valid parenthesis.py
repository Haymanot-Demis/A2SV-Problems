class Solution():
    """ 
    """
    def ValidParenthesis(self, s, preValidParenthesis):
        if  len(s):
            Valid_Parenthesis = ''
            for op in s:
                if op ==  '(':
                    if len(Valid_Parenthesis) == 0 or Valid_Parenthesis[-1] == ')':
                        if len(s)-1 > s.index(op):
                            Valid_Parenthesis += op
                    else:
                        Valid_Parenthesis = Valid_Parenthesis[:-1]
                        break
                elif op == ')' and len(Valid_Parenthesis) != 0:
                    if Valid_Parenthesis[-1] == '(':
                        Valid_Parenthesis += op
                    else:
                        break

            if len(Valid_Parenthesis) > len(preValidParenthesis):
                Valid_Parenthesis = self.ValidParenthesis(s[s.index(op) + 1:], Valid_Parenthesis)
            else:
                Valid_Parenthesis = self.ValidParenthesis(s[s.index(op) + 1:], preValidParenthesis)

            return Valid_Parenthesis
        else:
            return preValidParenthesis

    
    def LongestValidParenthesis(self, s):
        return self.ValidParenthesis(s,"")

    
    def checkNestedParenthesis(self, s):
        stack = list()
        i = 0;
        validParenthesis = ''
        while i < len(s):
            char = s[i]
            if char == '(' and len(stack) == 0: # check to ensure no infinite loop
                if len(s)-1 > s.index(char):
                    validParenthesis += char
                    stack.append("(")
            elif char == '(':
                result = self.checkNestedParenthesis(s[i+1:])

                # i think the else part is unnecessary and the comment inside it is talking about the issue of the if part
                if result[1] >= 0:
                    validParenthesis += result[0]
                    i += len(result[0]) # don't forgot to add one for the next iteration (done)
                    # if i + result[1] == len(s) => we reach end of line and we don't get a match for the current char so check which is the longest valid parenthesis and return it else it returned since it got the match so continue                    
                else:
                    if len(validParenthesis) < len(result[0]):
                        validParenthesis = result[0]
                        # to be determined i don't predict why error is occurred
                        # i think the erro is occurred b/c it has reached end of line and don't get the match or get ')' with empty stack
                        # the function always returned with the next valid parethesis

                        #two options 
                        """
                        1) i will have an outer function that iterates over the string as a first iteration
                            so i can continue here because this means this error tells me that we reached at the match (I hope this is good way)
                        2) if no outer function idon't know
                        """
            elif char == ')' and len(stack) != 0:
                if stack[-1] == '(':
                    validParenthesis +=  char
            else:
                break # got error with empty stack asked for match

            i += 1   # increment the index                              

        
        return [validParenthesis, i]

            
mySolution = Solution()
print(mySolution.LongestValidParenthesis('()()())()()()())()()()()())()()()()())()()()'))
            

"""
it will return
1)  when it gets an error parenthesis
        like if it gets ')' even if stack is empty:
                means -> has match so return valid srting got and index to be continued
        if stack is not empty even if end of line is reached
                no matchso return valid srting got and index to be continued
2) at end of line


idea 2
let me use the validParenthesis method and call an other method when i get a possibility of nested parenthesis
"""

