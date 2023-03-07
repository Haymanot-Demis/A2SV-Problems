# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        itr = result

        def merge(list1, list2, itr):
            if not list1:
                itr.next = list2
                return itr
            elif not list2:
                itr.next = list1
                return itr
            else:
                if list1.val >= list2.val:
                    itr.next = list2
                    list2 = list2.next
                else:
                    itr.next = list1
                    list1 = list1.next
                itr = itr.next
                return merge(list1, list2, itr)
        merge(list1,list2, itr)
        return result.next