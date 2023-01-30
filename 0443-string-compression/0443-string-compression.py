#yime 70min
class Solution:
    def compress(self, chars: List[str]) -> int:
        right = 0
        left = right
        length  = len(chars)
        while right < length - 1:
            left = right
            while right < length - 1 and chars[right] == chars[right+1]:
                right += 1
            count = right - left + 1
            digits = []
            if count > 1:
                digits = list(str(count))
                chars[left+1:left+1]= digits # this is to insert multiple elements at a position 
                digitLen = len(digits)
                del chars[left+digitLen+1:right+digitLen+1]
                right = left+digitLen
            length = len(chars)
            right += 1
        return len(chars)