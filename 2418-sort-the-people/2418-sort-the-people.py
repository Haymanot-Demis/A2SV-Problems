class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            #selection sort
            for i in range(len(names)-1):
                maxIndex = i
                for j in range(i + 1, len(names)):
                    if heights[maxIndex] < heights[j]:
                        maxIndex = j
                if heights[maxIndex] > heights[i]:
                    heights[i], heights[maxIndex] = heights[maxIndex], heights[i]
                    names[i], names[maxIndex] = names[maxIndex], names[i]
            return names