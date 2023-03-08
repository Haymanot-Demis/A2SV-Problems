# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compareSubtree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or (root1.val != root2.val):
                return False
            
            return compareSubtree(root1.left, root2.left) and compareSubtree(root1.right, root2.right)

        def findSubtree(node, val):
            if not node:
                return False
            if node.val == val:
                res = compareSubtree(node, subRoot)
                if res:
                    return True
            return findSubtree(node.left, val) or findSubtree(node.right, val)

        return findSubtree(root, subRoot.val)