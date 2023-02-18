# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        """
        the idea of this solution is if we get node value that exists in nums then this is one component and then next  all  consecutive elements which are in the list are part of the previous component, if we get a node element that is part of nums then we won't increament the count until we got a node value that is part of nums 

        i.e we increament the count if node value exists in nums and the previous node is not in nums and we won't increamnet count if we get a node value that is not in nums or the  current node value and the  previous node value both exist in nums since they are counted as one component

        we  can solve using falg to indicate 
            1. if false it means I haven't get value that is in the list based on this if the current           node value is in the list it is time increment the count of the components
            2. if True I got a value in the nums sub previously so I won't increament count since either        the current node value is in the previous component or it is not in the nums sub list
                """
        get = False
        components = 0
        nums = set(nums) # for fast checking of an element's existence
        itr = head
        while nums and itr:
            if not get and itr.val in nums:
                nums.remove(itr.val)
                components += 1
                get = True
            elif get and itr.val not in nums:
                get = False
            elif get and itr.val in nums:
                nums.remove(itr.val)
         
            itr = itr.next
        return components