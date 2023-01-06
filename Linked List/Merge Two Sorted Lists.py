# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            result = ListNode()
            itr = result

            while list1 and list2:
                if list1.val >= list2.val:
                    itr.next = list2
                    list2 = list2.next
                else:
                    itr.next = list1
                    list1 = list1.next
                itr = itr.next
            
            if not list1:
                itr.next = list2
            else:
                itr.next = list1

            return result.next

