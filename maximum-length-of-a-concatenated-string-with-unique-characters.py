class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(indx, chars):
            if indx == len(arr):
                return len(chars)
            current_chars = set()

            isValid = True
            for char in arr[indx]:
                if char in current_chars or char in chars:
                    isValid = False
                    break
                current_chars.add(char)

            case1 = 0
            if isValid:
                case1 = backtrack(indx + 1, chars | current_chars)

            case2 = backtrack(indx + 1, chars)
            return max(case1, case2)
        return backtrack(0, set())