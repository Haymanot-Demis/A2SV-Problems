# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymetricHelper(subtree1, subtree2):
            if not subtree1 and not subtree2:
                return True
            if not subtree1 or not subtree2:
                return False
            if subtree1.val != subtree2.val:
                return False
            return isSymetricHelper(subtree1.left, subtree2.right) and isSymetricHelper(subtree1.right, subtree2.left)
        return isSymetricHelper(root.left, root.right)