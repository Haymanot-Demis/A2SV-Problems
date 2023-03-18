class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterElems = list()
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            hasNext = False
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums2[j]:
                    nextGreaterElems.append(nums2[k])
                    hasNext = True
                    break
            if hasNext == False:
                nextGreaterElems.append(-1) 
        return nextGreaterElems