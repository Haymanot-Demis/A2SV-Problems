# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head and not head.next:
            return True
        elif not head.next.next:
            return bool(head.val == head.next.val)

        fast = head
        slow = head
        while fast and fast.next: # at the end slow will equal to middle node
            slow = slow.next
            fast = fast.next.next
        reversedSecondHalf = self.reverse(slow)

        temp = head
        while temp is not slow:
            if temp.val != reversedSecondHalf.val:
                return False
            temp = temp.next
            reversedSecondHalf = reversedSecondHalf.next
        return True
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev