class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_set = []
        for word in words:
            word_bit = 0
            for char in word:
                word_bit |= 1 << (ord(char) - 97)
            words_set.append(word_bit)
        max_len_prod = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if not (words_set[i] & words_set[j]):
                    # no intersection
                    max_len_prod = max(max_len_prod, len(words[i]) * len(words[j]))
        return max_len_prod