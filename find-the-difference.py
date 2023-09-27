class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        print(count_s)
        print(count_t)
        for ch, co in count_t.items():
            if ch not in count_s or co > count_s[ch]:
                return ch