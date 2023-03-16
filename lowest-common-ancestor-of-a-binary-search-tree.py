# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findSmallestAncestor(node):
            if q.val <= node.val and p.val >= node.val or q.val >= node.val and p.val <= node.val:
                return node
            if q.val < node.val and p.val < node.val:
                return findSmallestAncestor(node.left)
            if q.val > node.val and p.val > node.val:
                return findSmallestAncestor(node.right)

        return findSmallestAncestor(root)