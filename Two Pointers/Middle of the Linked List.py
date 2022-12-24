# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head
        count = 1
        while p2 != None and p2.next != None:
           p2 = p2.next.next
           p1 = p1.next
           count += 1
        return p1

head = ListNode(1);
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
sixth = ListNode(6)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

mysolution = Solution()
print(mysolution.middleNode(head).val)