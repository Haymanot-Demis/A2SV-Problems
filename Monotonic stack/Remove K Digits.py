#time 
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        index = 0
        length = len(num)
        deleteCount = 0
        stack = [] #increasing monotonic Stack
        while index < length and deleteCount < k:
            while stack and deleteCount < k and stack[-1] > num[index]:
                stack.pop()
                deleteCount += 1
            if not stack and num[index] == 0:
                index += 1
                continue  
            stack.append(num[index])
            index += 1
        print(stack, index, deleteCount)
        while index < length:
            if not stack and num[index] == 0:
                index += 1
                continue
            stack.append(num[index])
            index += 1
        while deleteCount < k:
            stack.pop()
            deleteCount += 1
        smallestNum = ''.join(stack)
        return "0" if smallestNum == "" else str(int(smallestNum))

    
sol = Solution()
print(sol.removeKdigits('10', 2))

