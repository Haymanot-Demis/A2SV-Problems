class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        answer = [0] * (len(s) + 1)
        answer[0] = 31
        vowels_hash_table = {"a" : [1, 16], "e" : [1, 8], "i" : [1, 4], "o" : [1, 2], "u" : [1, 1]}
        for indx, char in enumerate(s):
            if char in vowels_hash_table:
                if vowels_hash_table[char][0] == 0:
                    vowels_hash_table[char][0] = 1
                    answer[indx + 1] += vowels_hash_table[char][1]
                else:
                    vowels_hash_table[char][0] = 0
                    answer[indx + 1] -= vowels_hash_table[char][1]
            answer[indx + 1] += answer[indx]
            
        hash_map = {31:0}

        max_size = 0
        for i in range(1, len(answer)):
            if answer[i] == 31:
                max_size = max(max_size, i)
            if answer[i] in hash_map:
                max_size = max(max_size, i - hash_map[answer[i]])
            else:
                hash_map[answer[i]] = i

        return max_size
        