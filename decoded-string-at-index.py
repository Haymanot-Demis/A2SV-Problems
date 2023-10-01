class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        if we go from end of the string, we could see where the position of k could be  
        """

        decodedLength = 0
        i = 0        

        while k > decodedLength:
            if s[i].isdigit():
                decodedLength *= int(s[i])
            else:
                decodedLength += 1
            
            i += 1
        
        for j in range(i - 1, -1, -1):
            if s[j].isdigit():
                decodedLength //= int(s[j])
                k %= decodedLength # give attension
            else:
                if k == 0 or k == decodedLength:
                    return s[j]

                decodedLength -= 1