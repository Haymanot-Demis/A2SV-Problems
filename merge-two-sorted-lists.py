# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            merged = ListNode()
            itr = merged
            if list1.val >= list2.val:
                itr.next = list2
                list2 = list2.next
            else:
                itr.next = list1
                list1 = list1.next
            itr = itr.next
            itr.next = self.mergeTwoLists(list1, list2)
            return merged.next