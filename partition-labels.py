class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        length = len(s)
        left = 0
        right = 0
        i = 0
        sizes = []
        while i < length:
            if right == 0:
                if s[i] in s[right+1:] :
                    right += s[right+1:].rfind(s[i]) + 2
                else:
                    right += 1
            elif s[i] in s[left:right]:
                if s[i] in s[right+1:]:
                    tempRight = right + s[right+1:].rfind(s[i]) + 2
                    if tempRight > right:
                        right = tempRight
                elif (i + 1) > right:
                    right = i + 1
            elif s[i] in s[right+1:]:
                if i == right:
                    sizes.append(right - left)
                    left = right
                    right += s[right+1:].rfind(s[i]) + 2
            else:
                sizes.append(right - left)
                left = right
                right += 1
        
            i += 1
        sizes.append(right - left)
        return sizes