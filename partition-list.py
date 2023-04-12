# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greaters = ListNode()
        greatersHead = greaters
        lesses = ListNode()
        lessesHead = lesses
        iterator = head
        while iterator:
            if iterator.val >= x:
                greaters.next = ListNode(iterator.val)
                greaters = greaters.next
            else:
                lesses.next = ListNode(iterator.val)
                lesses = lesses.next
            iterator = iterator.next
        lesses.next = greatersHead.next # the first greater value is at the second node in the greaters list
        return lessesHead.next # the first less value is at the second node in the lesses list