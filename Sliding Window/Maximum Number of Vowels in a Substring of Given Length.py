#time 40
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        count = 0 
        maxVowels = 0
        length = len(s)
        for right in range(length):
            if s[right] in 'aeiou':
                count += 1
            if right - left + 1 == k:
                maxVowels = max(count, maxVowels)
                if s[left] in 'aeiou':
                    count -= 1
                left += 1
        return maxVowels

