# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def addLeaf(node, parent):
            if not node:
                return 0
            
            if not node.left and not node.right and parent and node == parent.left:
                return node.val

            return addLeaf(node.left, node) + addLeaf(node.right, node) 
        
        return addLeaf(root, None)