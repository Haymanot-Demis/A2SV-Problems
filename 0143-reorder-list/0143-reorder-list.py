# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        reversedSecondHalf, halfLen = self.reverse(slow)
        temp = head

        while reversedSecondHalf:
            node = ListNode(reversedSecondHalf.val)
            temp.next, node.next = node, temp.next
            reversedSecondHalf = reversedSecondHalf.next
            temp = temp.next.next

    def reverse(self, node):
        prev= None
        curr = node.next
        i = 0
        node.next = None
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            i += 1
        return prev, i
        