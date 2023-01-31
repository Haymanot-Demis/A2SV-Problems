# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        the principle of this solution is 
        1. save the length of the sublist that has to be reversed 
        2. the node before the left node        
        3. the left node i.e the first node of the sublist that has to be reversed        
        3. the right node i.e the last node of the sublist that has to be reversed i.e final value of variable prev      
        3. the node next to the right node i.e final value of variable curr
        4. then reverse the sublist between left and right inclusive
        5. set next of node before left to prev i.e the right node
        6. set next node of left node to the node next to right i.e curr

        '''
        dummy_node = ListNode()
        dummy_node.next = head
        beforeStart = dummy_node
        right = right - left + 1
        while left > 1:
            beforeStart = beforeStart.next
            left -= 1
        start = beforeStart.next
        print(beforeStart.val)
        print(start.val)
        curr = start
        prev = None
    
        while right > 0:
            print(right, curr.val)
            Next = curr.next
            curr.next = prev
            prev= curr
            curr = Next
            right -= 1
        start.next = curr
        beforeStart.next = prev
        return dummy_node.next


