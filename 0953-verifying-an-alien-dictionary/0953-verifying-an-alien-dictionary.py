class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = {}
        for indx, char in enumerate(order):
            alphabets[char] = indx
        
        for indx in range(len(words) - 1):
            print(words[indx], words[indx + 1], self.comp(words[indx], len(words[indx]),words[indx + 1], len(words[indx + 1]), alphabets))
            if self.comp(words[indx], len(words[indx]),words[indx + 1], len(words[indx + 1]), alphabets) == 1:
                return False
        return True
        
    def comp(self, elm1, length1, elm2, length2, alphabets):
            p1 = 0
            p2 = 0
            while p1 < length1 and p2 < length2:
                if alphabets[elm1[p1]] < alphabets[elm2[p2]]:
                    return -1
                elif alphabets[elm1[p1]] > alphabets[elm2[p2]]:
                    return 1
                p1 += 1
                p2 += 1
            if p1 < length1: 
                return 1
            else:
                return -1
            
                      
