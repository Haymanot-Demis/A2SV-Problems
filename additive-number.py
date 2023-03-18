class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        def isFibonacci(indx, prev_nums): 
            if indx == len(num):
                print(prev_nums)
                return len(prev_nums) >= 3
            for i in range(indx, len(num)):
                print(i)
                if len(prev_nums) < 2:
                    if len(str(int(num[indx:i+1]))) == len(num[indx:i+1]):
                        if isFibonacci(i + 1, prev_nums + [int(num[indx:i+1])]):
                            return True
                elif int(num[indx:i+1]) == prev_nums[-1] + prev_nums[-2] and len(str(int(num[indx:i+1]))) == len(num[indx:i+1]):
                    if isFibonacci(i + 1, prev_nums + [int(num[indx:i+1])]):
                        return True
            return False
        return isFibonacci(0, [])