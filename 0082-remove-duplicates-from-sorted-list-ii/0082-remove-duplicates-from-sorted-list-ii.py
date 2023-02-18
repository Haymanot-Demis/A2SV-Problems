# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """"
        use dummy node not loose the if it has aduplicate value then using two pinters equal speed if the until the front pointer has duplicate get it forward it will stop when its value is not equal to the next then the next node of the back pointer will be the next of the front pointer 
        """
        dummy_node = ListNode(0, head)
        p1 = dummy_node
        p2 = p1.next
        while p2 and p2.next:
            if (p2.val == p2.next.val):
                while p2 and p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                p1.next = p2.next
                p2 = p1.next
            else:
                p1 = p2
                p2 = p2.next
        return dummy_node.next