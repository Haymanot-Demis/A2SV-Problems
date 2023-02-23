class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq_char = s[0]
        chars = {s[0]:1}
        max_substr_length = 0
        length = len(s)
        left = 0
        for right in range(1, length):
            chars[s[right]] = chars.get(s[right], 0) + 1
            if chars[s[right]] > chars.get(max_freq_char, 0):
                max_freq_char = s[right]
            while right - left + 1 - chars[max_freq_char] > k:
                chars[s[left]] -= 1
                max_freq_char = max(chars, key=lambda char : chars[char])
                left += 1
            max_substr_length = max(max_substr_length, right - left + 1)
        return max_substr_length