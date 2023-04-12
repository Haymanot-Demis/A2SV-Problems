# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        rotating list k times means taking the last k nodes to the front
        """
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next

        if length <= 1:
            return head

        k = k % length
        if k == 0:
            return head

        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        
        last_node = temp.next
        while last_node and last_node.next:
            last_node = last_node.next

        last_node.next = head
        head = temp.next
        temp.next = None

        return head