# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_even_grandparent = [0]
        def sumNodes(parent, evenParent, evenGP, prev_sum):
            if parent:
                if evenGP:
                    prev_sum[0] += parent.val
                sumNodes(parent.left, parent.val % 2 == 0, evenParent, prev_sum)
                sumNodes(parent.right, parent.val % 2 == 0, evenParent, prev_sum)
                
        sumNodes(root, False, False, sum_even_grandparent)
        return sum_even_grandparent[0]