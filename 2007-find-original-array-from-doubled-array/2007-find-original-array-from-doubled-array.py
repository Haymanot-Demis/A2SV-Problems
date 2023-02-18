from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """
        check if each element has a double pair in the list then if it has add it to the answer list, then finally if the length of the answer id equal to the half of the changed array it is doubled array
        """
        changed.sort()
        counter_dict = dict(Counter(changed))
        answer = []
        if counter_dict.get(0, 0) % 2 == 1: # if the number of zeroes is odd the it can't be a doubled array
            return []

        if 0 in counter_dict: # if zero is in the list then append half of them to the answer array
            answer.extend([0] * (counter_dict[0] // 2))
            del counter_dict[0]
      
        for num, freq in counter_dict.items():
            if freq > 0 and counter_dict.get(num * 2, 0) > 0:
                answer.extend([num] * min(counter_dict[num * 2], freq))
                counter_dict[num * 2] -= min(counter_dict[num * 2], freq)
                counter_dict[num] -= min(counter_dict[num * 2], freq)
                

        if 2*len(answer) == len(changed):
            return answer
        return []