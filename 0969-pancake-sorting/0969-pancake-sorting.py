class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
        the idea behind this solution is 
        take the largest number each time then reverse the numbers up to that num then reverse the largets number of numbers from the begining  
        """
        length = len(arr)
        flips = []
        for num in range(length, 0, -1):
            k = arr.index(num) + 1
            arr[:k] = arr[:k][::-1]
            flips.append(k)
            arr[:num] = arr[:num][::-1]
            flips.append(num)
        return flips
        