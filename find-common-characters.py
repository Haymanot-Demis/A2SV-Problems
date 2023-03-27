from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonChars = Counter(words[0])
        for word in words[1:]:
            charsOfCurrWord = Counter(word)
            for char, count in commonChars.items():
                if char in charsOfCurrWord:
                    commonChars[char] = min(commonChars[char], charsOfCurrWord[char])
                else:
                    commonChars[char] = 0
        result = []
        for char, count in commonChars.items():
            for _ in range(count):
                result.append(char)
        return result