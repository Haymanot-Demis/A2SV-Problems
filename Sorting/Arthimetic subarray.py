#time 25
class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answer = [True]*len(l)
        # print(answer)
        for i in range(len(l)):
            subarray = nums[l[i]:r[i] + 1]
            # print(subarray)
            subarray.sort()
            commonDistance = subarray[1] - subarray[0]
            if len(subarray) == 2:
                answer[i] = True
            else:
                for k in range(2, len(subarray)):
                    if subarray[k] - subarray[k - 1] != commonDistance:
                        answer[i] = False
                        break
            # print(subarray, answer[i])
        return answer

mySolution = Solution()
print(mySolution.checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))