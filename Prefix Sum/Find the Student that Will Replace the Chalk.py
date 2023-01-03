#time 25
class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        length = len(chalk)
        i = 0
        Sum = sum(chalk)
       # numberOfTurnsOfEachStudent 
        turns = k//Sum
        k -= turns*Sum
        while i < length:
            if chalk[i] > k:
                return i
            k -= chalk[i]
            i += 1
            