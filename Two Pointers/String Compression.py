#yime 70min
class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ''
        right = 0
        left = right
        length  = len(chars)
        while right < length - 1:
            left = right
            s += chars[left]
            while right < length - 1 and chars[right] == chars[right+1]:
                right += 1
            count = right - left + 1
            digits = []
            if count > 1:
                while count > 0: # here we need a method that converts anumber into array of its digits
                    digits.insert(0, str(count%10))
                    count = int(count/10)
              
                chars[left+1:left+1]= digits # this is to insert multiple elements at a position 
                digitLen = len(digits)
                del chars[left+digitLen+1:right+digitLen+1]
                right = left+digitLen
            length = len(chars)
            right += 1
        return len(chars)