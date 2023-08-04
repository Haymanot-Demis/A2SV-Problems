class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        counter = Counter(wordDict)
        memo = {}
        def recursive(indx, word_dict):
            print(indx)
            if indx in memo:
                return memo[indx]
            if indx >= len(s):
                return True
            word = ""

            for i in range(indx, len(s)):
                word += s[i]
                if word in word_dict:
                    res = recursive(i + 1, word_dict)
                    if res:
                        return True
            memo[indx] = False
            return False
        
        return recursive(0, counter)