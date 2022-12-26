class Solution:
    def MergeSort(self, array, left, right):
        if right - left > 1:
            mid = (left + right)//2
            count1 = self.MergeSort(array, left, mid)
            count2 = self.MergeSort(array, mid + 1, right)
            count = self.Merge(array, left, mid, right)
            return count + count1 + count2
        else:
            return 0

    def Merge(self, array, left, mid, right, ):
        count = 0
        while mid <= right:
            val = array[mid]
            j = mid - 1
            while j >= left and val < array[j]:
                array[j + 1] = array[j]
                j -= 1
                count += 1
            array[j + 1] = val
            mid += 1
        return count
        
mySolution = Solution()
nums = [2,1,3,1,2]
print(mySolution.MergeSort(nums, 0, len(nums) - 1))
print(nums)