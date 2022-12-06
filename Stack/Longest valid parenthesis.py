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
        return self.ValidParenthesis(s)

    
    def OuterFunction(self, s):
        return self.checkNestedParenthesis(s, True)[0]

    
    def checkNestedParenthesis(self, s, flag = False):
        stack = list()
        i = 0;
        validParenthesis = ''
        prevParenthesis = ''
        interupted = False

        while i < len(s):
            char = s[i]
            if interupted:
                if len(validParenthesis) > len(prevParenthesis):  
                    prevParenthesis = validParenthesis
                validParenthesis = ''
                interupted = False
            if char == '(' and len(stack) == 0: # check to ensure no infinite loop
                if len(s)-1 > i:
                    validParenthesis += char
                    stack.append("(")
            elif char == '(':
                print(s[i:],i)
                result = self.checkNestedParenthesis(s[i:]) # s[i+1]???
                print(stack)
                stack.clear()
                print(stack)
                print(result, i)
               

                # i think the else part is unnecessary and the comment inside it is talking about the issue of the if part
                if result[1] >= 0:
                    print(i)
                    i += result[1] # don't forgot to add one for the next iteration (done)
                    # if i + result[1] == len(s) => we reach end of line and we don't get a match for the current char so check which is the longest valid parenthesis and return it else it returned since it got the match so continue    
                    print(i)
                    if i == len(s): # reached end of line so return largest valid parenthesis
                        print("Returned parenth",i, result)

                        if len(validParenthesis) < len(result[0]):
                            # print("v < r")
                            if len(result[0]) > len(prevParenthesis):
                                return [result[0], i]
                            else:
                                return [prevParenthesis, i]
                        elif len(validParenthesis) >= len(prevParenthesis):
                            return [validParenthesis[:-1], i]
                        else:
                            return [prevParenthesis, i]
                    else: # got match so continue
                        validParenthesis += result[0] + ')'
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
                    stack.pop()
            elif char == ')' and len(stack) == 0 and flag == True:
                interupted = True
                pass
            else:
                print("got error with empty stack asked for match", i)
                break # got error with empty stack asked for match
            print("90", i)
            i += 1   # increment the index 
                                         
        
        if len(validParenthesis) >= len(prevParenthesis):
            return [validParenthesis, i]
        return [prevParenthesis, i]



            
mySolution = Solution()
print(len(mySolution.OuterFunction('(()))(()()))))')))
"""                                                       (((((()()()()()(()())))))))
give it a flag to tell it that it is from nested or not
if len(validParenthesis) >= len(prevParenthesis):
                                return [validParenthesis[:-1], i]
                            else:
                                return [prevParenthesis[:-1], i] check this concept
"""

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

