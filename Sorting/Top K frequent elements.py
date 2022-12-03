# 10
class Solution(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freqDict = {}
        nums.sort()
        for i  in range(len(nums)):
            if nums[i] not in freqDict.keys():
                freqDict[nums[i]] = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] == nums[i]:
                        freqDict[nums[i]] += 1
                    else:
                        break
        
        frequencies = list(freqDict.values())
        frequencies.sort(reverse=True)
        prevFrequentNumber = None
        kFreqNums = set()
        for i in range(k):
            for key, num in freqDict.items():
                if frequencies[i] == num and key != prevFrequentNumber:
                    kFreqNums.add(key)
                    prevFrequentNumber = key
        print(frequencies)
        print(kFreqNums)
        return kFreqNums