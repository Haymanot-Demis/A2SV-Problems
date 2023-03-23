# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None 
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        indx = 1
        length = len(preorder)
        while indx < length and preorder[0] > preorder[indx]:
            indx += 1
            
        return TreeNode(preorder[0],self.bstFromPreorder(preorder[1:indx]), self.bstFromPreorder(preorder[indx:]))