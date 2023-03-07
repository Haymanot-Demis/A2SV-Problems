class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        """
        the main idea behind this problem is the distance between the currrent index that number and each indices of that number the is (if we know the number of numbers before and the distance from each number of the number before it) adding the distance between the current index and the index before it to all of the distances of numbers before it (i.e. adding this distance the number of numbers times)
        """
        length = len(arr)
        prefixsum = [0] * (length + 1)
        suffixsum = [0] * (length + 1)
        indices_of = defaultdict(list)

        for indx, num in enumerate(arr):
            indices_of[num].append(indx)

        for num, indices in indices_of.items():

            for i in range(1, len(indices)):
                prefixsum[indices[i] + 1] += prefixsum[indices[i - 1] + 1] + (indices[i] - indices[i - 1]) * i
            
            reverse = indices[::-1]
            for i in range(1, len(reverse)):
                suffixsum[reverse[i] + 1] += suffixsum[reverse[i - 1] + 1] + abs(reverse[i] - reverse[i - 1]) * i
               
        return [sum(pair) for pair in zip(prefixsum, suffixsum)][1:]