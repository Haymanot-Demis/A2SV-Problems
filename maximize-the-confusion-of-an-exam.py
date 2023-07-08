class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        prefixsum = [0] * len(answerKey)
        prefixsum[0] += answerKey[0] == 'T'

        for i in range(1, len(answerKey)):
            prefixsum[i] += prefixsum[i - 1] + (answerKey[i] == 'T')

        print(prefixsum)
        
        max_confusion = 0
        Thash = defaultdict(lambda : -1, {0:-1})
        Fhash = defaultdict(lambda : -1, {0:-1})

        for i in range(len(prefixsum)):
            trues = prefixsum[i]
            falses = i + 1 - prefixsum[i]
            F = i - Thash[trues - k] # if we we want to change them to T
            T = i - Fhash[falses - k] # if we want to change to F        
            if trues not in Thash:
                Thash[trues] = i

            if falses not in Fhash:
                Fhash[falses] = i
            max_confusion = max(max_confusion, T, F)
        
        return max_confusion