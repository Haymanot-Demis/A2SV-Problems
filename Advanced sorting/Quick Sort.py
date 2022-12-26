class Solution:
    def QuickSort(self, array:list):
        print("sort ", array)
        if len(array) > 1:
            left = 0
            right = len(array) - 1
            pivot = left
            while (left < right):
            
                if (pivot == left):
                    if array[left] > array[right]:
                        array[left],array[right] = array[right], array[left]
                        pivot = right
                        left += 1
                    else:
                        right -= 1
                else:
                    if array[left] > array[right]:
                        array[left],array[right] = array[right], array[left]
                        pivot = left
                        right -= 1
                    else:
                        left += 1
            print(array)
            array[:pivot] = self.QuickSort(array[:pivot])
            array[pivot + 1:] = self.QuickSort(array[pivot + 1:])
            return array
        else:
            return array

mySolution = Solution()
nums = [5, 8, 2, 4, 1, 3, 9, 7, 6, 0]
mySolution.QuickSort(nums)
print(nums)