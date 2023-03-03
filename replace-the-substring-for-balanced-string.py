class Solution:
    def balancedString(self, s: str) -> int:
        """
        In my way first find the count of each char 
        then select the chars which has more count than the qaurter of the length because these are the one that we want to replace
        the window must at least contain each chars in 'chars_needed' dictionary (at least the count mustbe equal)
        move the right pointer until it comes true and move the left pointer until false to get the minimum length
        """
        # first find the chars the window must contain
        def isSatisfied(chars_needed, current_chars):
            for char, count in chars_needed.items():
                if current_chars[char] < count:
                    return False
            return True

        counter = Counter(s)
        quarter = len(s) // 4
        chars_needed = defaultdict(int)
        for char, count in counter.items(): # the window must contain the chars that have more than quarter
            if count > quarter:
                chars_needed[char] += count - quarter

        if len(chars_needed) == 0:
            return 0


        best_possible_min_length = sum(chars_needed.values())

        min_length = quarter * 4 + 1
        current_chars = defaultdict(int)
        left = 0

        for right in range(quarter*4):
            if s[right] in chars_needed:
                current_chars[s[right]] += 1
            while isSatisfied(chars_needed, current_chars):
                min_length = min(min_length, right - left + 1)
                if s[left] in chars_needed:
                    current_chars[s[left]] -= 1
                left += 1
                
        return min_length