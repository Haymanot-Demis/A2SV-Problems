class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        use a number by assuming it will will be repersented with 5 bits to indicate the 5 vowel so at each position we check wich vowels have even freq and which have odd freq use shift operation and xor to toggle the bit that corresponds to the current vowel
        """
        answer = [0] * (len(s))
        vowels = {"a" : 4, "e" : 3, "i" : 2, "o" : 1, "u" : 0}
        current_vowels_parity = 31 # number indicating the parity of each vowel at the current indx
        for indx, char in enumerate(s):
            if char in vowels:
                current_vowels_parity ^= (1 << vowels[char])
            answer[indx] = current_vowels_parity

        hash_map = defaultdict(int, {31:-1})

        max_size = 0
        for i in range(len(answer)):
            if answer[i] in hash_map:
                max_size = max(max_size, i - hash_map[answer[i]])
            else:
                hash_map[answer[i]] = i

        return max_size