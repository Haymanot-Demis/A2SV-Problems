#time 
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0;
        indx = 0
        smallestNumber = list(num)
        while smallestNumber and i < k and indx < len(num) - 1:
            if num[indx] > num[indx + 1]:
                smallestNumber.pop(indx - i)
                i += 1
                i = self.compare(smallestNumber, indx - i, i, k)
            indx += 1
        indx = len(num) - 1
        if i < k:
            while i < k and smallestNumber:
                smallestNumber.pop()
                i += 1
        smallestNumber = ''.join([str(elem) for elem in smallestNumber])
        smallestNumber = "0" if smallestNumber == ""  else smallestNumber
        smallestNumber = int(smallestNumber)
        print(len(str(smallestNumber)))    
        print(i)        
        return str(smallestNumber)
    
    def compare(self, smallArr:List[int], indx, counter, maxNumOFRemoved) -> int:
        if counter >= maxNumOFRemoved or indx < 0:
            return counter
        else:
            if smallArr and smallArr[indx] > smallArr[indx + 1]:
                smallArr.pop(indx)
                counter += 1
                return self.compare(smallArr, indx - 1, counter, maxNumOFRemoved)
            else:
                return counter




