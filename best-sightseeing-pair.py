class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        leng = len(values)

        # array for values[i] + i
        arr1 = [values[0]]

        # array for values[j] - j
        arr2 = [values[-1] - (leng - 1)]

        for i in range(1, len(values)):
            arr1.append(max(values[i] + i, arr1[-1]))
            arr2.append(max(values[leng - i - 1] - (leng - i - 1), arr2[-1]))
        arr1.pop()
        arr2.pop()
        arr2 = arr2[::-1]

        max_score = 0
        for i in range(len(arr1)):
            max_score = max(max_score, arr1[i] + arr2[i])

        return max_score