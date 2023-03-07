class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        shift_record = [0]*length
        new_arr = ""
        for start, end, direction in shifts:
            if direction == 1:
                shift_record[start] += 1
                if end + 1 < length:
                    shift_record[end + 1] -= 1
            else:
                shift_record[start] -= 1
                if end + 1 < length:
                    shift_record[end + 1] += 1
                
        new_arr += chr(97 + (ord(s[0]) + shift_record[0] - 97) % 26)
        for i in range(1, length):
            shift_record[i] += shift_record[i - 1]
            new_arr += chr(97 + (ord(s[i]) + shift_record[i] - 97) % 26)

        return new_arr