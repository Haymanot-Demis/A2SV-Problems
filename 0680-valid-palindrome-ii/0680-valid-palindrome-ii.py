class Solution:
    def validPalindrome(self, s: str) -> bool:
        """"
        find the point of the where the palindromity is failed if exist and check again if the string without the current right or left char becomes palindrome if it is yes we can else not, if it is already palidrome it also become palindrome if we dlete a letter from the center
        """
        left = 0
        right = len(s) - 1
        isPalindrome = True
        while left < right:
            if s[left] != s[right]:
                lleft = left + 1
                rright = right
                while lleft < rright: # check if the right most subarray of the fail point is palindrome
                    if s[lleft] != s[rright]:
                        isPalindrome = False
                        break
                    lleft += 1
                    rright -= 1
                if isPalindrome:
                    return True
                isPalindrome = True
                lleft = left
                rright = right - 1
                while lleft < rright: # check if the left most subarray of the fail point is palindrome
                    if s[lleft] != s[rright]:
                        isPalindrome = False
                        break
                    lleft += 1
                    rright -= 1
                return isPalindrome                
            left += 1
            right -= 1 
        return True