# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        answer = [0]
        temp = head
        stack = []
        i = 1
        while temp:
            while stack and stack[-1]["val"] < temp.val:
                answer[stack.pop()["idx"]] = temp.val
            stack.append({"val":temp.val,"idx":i})
            i += 1
            answer.append(0)
            temp = temp.next
        return answer[1:]