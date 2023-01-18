# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        array = []
        while temp:
            array.append(temp.val)
            temp = temp.next
        array.sort()
        temp = head
        for num in array:
            temp.val = num
            temp = temp.next
        return head