#time = 30min
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freqDict = {}
        arr.sort()
        for i  in range(len(arr)):
            if arr[i] not in freqDict.keys():
                freqDict[arr[i]] = 1
                for j in range(i + 1, len(arr)):
                    if arr[j] == arr[i]:
                        freqDict[arr[i]] += 1
                    else:
                        break
        frequencies = freqDict.values()
        frequencies.sort(reverse=True)
        print(frequencies)
        minSetSize = 0
        sum = 0
        while sum < len(arr)/2:
            sum += frequencies[minSetSize]
            minSetSize += 1
        return minSetSize


mySolution = Solution()
mySolution.minSetSize([3,3,3,3,5,5,5,2,2,7])



