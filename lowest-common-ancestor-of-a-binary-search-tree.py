# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findSmallestAncestor(node):
            if not node:
                return False
 
            left_res = False
            right_res = False

            if node.val == p.val:
                if node.val > q.val:
                    left_res = findSmallestAncestor(node.left)
                else:
                    right_res = findSmallestAncestor(node.right)
            elif node.val == q.val:
                if node.val > p.val:
                    left_res = findSmallestAncestor(node.left)
                else:
                    right_res = findSmallestAncestor(node.right)
            else:
                left_res = findSmallestAncestor(node.left)
                right_res = findSmallestAncestor(node.right)
            
            if node.val == p.val or node.val == q.val:
                if left_res == True or right_res == True:
                   return node
                return True
            
            if left_res == right_res == False:
                return False
            if (left_res == True) ^ (right_res == True): #bitwise operator if one of the condition is true
                return True
            if left_res == right_res == True:
                return node

            if left_res:
                return left_res
            return right_res

        return findSmallestAncestor(root)