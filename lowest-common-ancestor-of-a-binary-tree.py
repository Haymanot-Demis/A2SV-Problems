# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return False
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if root.val == p.val or root.val == q.val:
            if left == True or right == True:
                return root
            return True
            
        if left == right == False:
            return False
        if left == right == True:
            return root
        if (left == True) ^ (right == True):
            return True
        if left:
            return left
        return right