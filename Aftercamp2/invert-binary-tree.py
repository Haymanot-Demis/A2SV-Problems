# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(parent):
            if not parent:
                return
            
            left = invert(parent.left)
            right = invert(parent.right)

            parent.left, parent.right = right, left

            return parent
        
        return invert(root)