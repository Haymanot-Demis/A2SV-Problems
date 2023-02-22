class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length <= 10:
            return []
        window_start = 0
        window_end = 10
        set_of_DNA_sequences = set()
        answer = set()
        while window_end <= length:
            DNA_sequence = s[window_start:window_end]
            if DNA_sequence in set_of_DNA_sequences:
                answer.add(DNA_sequence)
            else:
                set_of_DNA_sequences.add(DNA_sequence)
            window_start += 1
            window_end += 1
        return answer
