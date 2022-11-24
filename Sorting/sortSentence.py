class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = {}
        init = 0
        for i  in range(len(s)):
            if s[i] == ' ' or i == len(s)-1:
                if i == len(s)-1:
                    words[s[i]] = s[init : i]
                else:
                    words[s[i - 1]] = s[init : i - 1]
                init  = i + 1
        sentence = ''
        print(words)
        for i in range(1, len(words) + 1):
            sentence += words[str(i)] + " "
        print(sentence)
        return sentence[:len(sentence) - 1]
    
mySolution = Solution()
mySolution.sortSentence("is2 sentence4 This1 a3")