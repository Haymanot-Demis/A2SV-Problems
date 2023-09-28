class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = [("", 0, 0)]
        digits = set(["2", "3", "4", "5", "6", "7", "8", "9"])
        i = 0
        while i < len(s):
            word = ""
            while i < len(s) and s[i] not in digits:
                word += s[i]
                i += 1
            if i < len(s):
                d = int(s[i])
            else:
                d = 1

            prev_len = stack[-1][2] * stack[-1][1]
            stack.append([word, d, (prev_len + len(word))])
            i += 1

            while i < len(s) and s[i] in digits:
                stack[-1][1] *= int(s[i])
                i += 1


        def decode(right, k):
            left = 0

            while left <= right:
                mid = left + (right - left) // 2
                length = stack[mid][2] * stack[mid][1]

                if k > length:
                    left = mid + 1
                elif k < length:
                    right = mid - 1
                else:
                    kth = stack[mid][0][-1] # kth letter is here
                    return kth
            
            word, d, length = stack[left]

            q = k // length

            if q == 0:
                indx = k - stack[left - 1][2] * stack[left - 1][1] - 1
                return word[indx]
            stack[left][1] = d - q
            k -= q * length # or k = k % length

            if k == 0:
                # if k is exact multiple of length i.e the kth letter is the last letter of the string until left
                return word[-1]

            return decode(left, k)

        return decode(len(stack) - 1, k)