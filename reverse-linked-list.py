# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head, None)
        return head
    
    def reverse(self, head, prev):
        if head:
            root = self.reverse(head.next, head)
            head.next = prev
            return root
        else:
            return prev