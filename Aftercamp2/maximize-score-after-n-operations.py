class Solution:
    def maxScore(self, nums: List[int]) -> int:
        result = 0
        def bt(s,arr):
            nonlocal result
            ind = -1
            for i,val in enumerate(nums):
                if i not in s:
                    ind = i
                    break
            if ind == -1:
                arr.sort()
                c = 0
                for i,_ in enumerate(arr):
                    c += arr[i] * (i + 1) 
                result = max(result,c)
                return
            s.add(ind)
            for i in range(len(nums)):
                if i not in s:
                    s.add(i)
                    temp = gcd(nums[i] ,nums[ind])
                    arr.append(temp)
                    bt(s.copy(),arr.copy())
                    arr.pop()
                    s.remove(i)
        bt(set(),[])
        return result