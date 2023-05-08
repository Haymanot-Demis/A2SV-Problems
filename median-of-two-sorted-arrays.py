class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        mid_pos = (len(nums1) + len(nums2)) // 2

        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2) and len(merged) < mid_pos + 1:
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        
        while p1 < len(nums1) and len(merged) < mid_pos + 1:
            merged.append(nums1[p1])
            p1 += 1
        
        while p2 < len(nums2) and len(merged) < mid_pos + 1:
            merged.append(nums2[p2])
            p2 += 1
        
        if (len(nums1) + len(nums2)) % 2:
            return merged[-1]
        else:
            return (merged[-1] + merged[-2]) / 2