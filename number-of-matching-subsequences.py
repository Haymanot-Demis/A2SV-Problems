class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        position = defaultdict(list)

        for i, ch in enumerate(s):
            position[ch].append(i)
        print(position)
        def check(word):
            pos = -1
            for ch in word:
                new_pos = bisect_left(position[ch], pos)

                while new_pos < len(position[ch]) and position[ch][new_pos] <= pos:
                    new_pos += 1
                
                if new_pos == len(position[ch]):
                    return False

                pos = position[ch][new_pos]
                
            return True

        count = 0
        for word in words:
            if check(word):
                count += 1

        return count