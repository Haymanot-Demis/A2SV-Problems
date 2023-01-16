class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        singleLineComment = -1
        mulLineComment = -1
        length = len(source)
        index = 0 
        while index < length:
            singleLineComment  = source[index].find("//")
            mulLineComment  = source[index].find("/*")
            if (mulLineComment != -1 and singleLineComment == -1) or (mulLineComment != -1 and singleLineComment > mulLineComment):
                codeBeforeComment = source[index][:mulLineComment]
                commnetEndingSymbol = -1
                first = True
                while index < length and commnetEndingSymbol == -1:
                    if first:
                        commnetEndingSymbol = source[index].find("*/",mulLineComment + 2)
                        first = False
                    else:
                        commnetEndingSymbol = source[index].find("*/")
                    index += 1
                index -= 1
                codeAfterComment = source[index][commnetEndingSymbol + 2:]
                source[index] = codeBeforeComment + codeAfterComment
                index -= 1            
            elif (singleLineComment != -1 and mulLineComment == -1) or (singleLineComment != -1 and mulLineComment > singleLineComment):
                code = source[index][:singleLineComment]
                if code != "":
                    answer.append(code)
            else:
                if source[index] != "":
                    answer.append(source[index])
            index += 1

        return answer
        