# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """"
        get the node before the node to be deleted is the main trick so we have to check it before we reach the node either by using two consecutive pointers or using dummy node and comparing next node's value with the given val
        """
        dummy_node = ListNode(0, head)
        temp =  dummy_node
        while temp and temp.next:
            if temp.next.val == val:
                ttemp = temp
                while ttemp and ttemp.next and ttemp.next.val == val:
                    ttemp = ttemp.next
                temp.next = ttemp.next
            else:
                temp = temp.next

        return dummy_node.next
            