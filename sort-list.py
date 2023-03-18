# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val <= head.next.val:
                return head
            head.next.next = ListNode(head.val)
            return head.next
        
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        list1 = self.sortList(fast)
        list2 = self.sortList(head)
        
        merged = ListNode()
        itr = merged
        while list1 and list2:
            if list1.val <= list2.val:
                itr.next = list1
                list1 = list1.next
            else:
                itr.next = list2
                list2 = list2.next
            itr = itr.next
        if list1:
            itr.next = list1
        else:
            itr.next = list2
        return merged.next