# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        store the odds in one linked list and the evens to another linked list the append the head of the evens linked list to the end of the odds linked list
        """
        oddsHead = ListNode()
        odds = oddsHead
        EvensHead = ListNode()
        Evens = EvensHead

        iterator = head
        turn = "odd"
        while iterator:
            if turn == "odd":
                odds.next = ListNode(iterator.val)
                odds = odds.next
                turn = "even"
            else:
                Evens.next = ListNode(iterator.val)
                Evens = Evens.next
                turn = "odd"
            iterator = iterator.next
        odds.next = EvensHead.next
        return oddsHead.next