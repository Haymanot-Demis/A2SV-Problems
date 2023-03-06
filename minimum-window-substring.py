class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hashed_target = Counter(t)
        hash_s = {}
        left = 0
        right = 0
        min_window_size = len(s) + 1
        min_window_substr = ""
        while right < len(s):
            if s[right] in hashed_target:
                hash_s[s[right]] = hash_s.get(s[right], 0) + 1
            if self.compare_dict(hash_s, hashed_target):
                while self.compare_dict(hash_s, hashed_target):
                    if s[left] in hash_s:
                        hash_s[s[left]] -= 1
                    left += 1
                if right - left + 2 <= min_window_size:
                    min_window_size = right - left + 2
                    min_window_substr = s[left - 1:right + 1]
            right += 1
        return min_window_substr
    
    def compare_dict(self, dict1, dict2):
        if len(dict1) != len(dict2):
            return False
        for char,freq in dict1.items():
            if dict2[char] > freq:
                return False
        return True