class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length <= 10:
            return []
        window_end = 9
        char_to_digit = {"A":1,"C":2,"G":3,"T":4}
        digit_to_char = {1:"A",2:"C",3:"G",4:"T"}
        DNA_sequence = 1

        for i in range(9):
            DNA_sequence = DNA_sequence * 10 +  char_to_digit[s[i]]
        set_of_DNA_sequences = set()
        answer = set()

        while window_end < length:
            DNA_sequence = (DNA_sequence % 10**9) * 10 + char_to_digit[s[window_end]]
            if DNA_sequence in set_of_DNA_sequences:
                answer.add(self.DNA(DNA_sequence, digit_to_char))
            else:
                set_of_DNA_sequences.add(DNA_sequence)
            window_end += 1

        return answer

    def DNA(self, sequence, hash_table):
        res = ""
        for x in str(sequence):
            res += hash_table[int(x)]
        return res