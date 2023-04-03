#yime 70min
class Solution:
    def compress(self, chars: List[str]) -> int:
        right = 0
        left = right
        length  = len(chars)
        if length == 1:
            return 1
        while right < length - 1:
            count = 1
            while right < length - 1 and chars[right] == chars[right+1]:
                right += 1
                count += 1
            digits = []
            if count > 1:
                digits = list(str(count))
                chars[left + 1:] = chars[right + 1:]
                chars[left+1:left+1]= digits # this is to insert multiple elements at a position 
                digitLen = len(digits)
                right = left+digitLen
                left +=  digitLen
            left += 1
            length = len(chars)
            right += 1
        return len(chars)