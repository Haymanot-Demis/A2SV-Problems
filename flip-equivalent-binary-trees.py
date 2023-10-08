# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2 or node1 and not node2 or node1.val != node2.val:
                return False
            
            ll = dfs(node1.left, node2.left)
            lr = dfs(node1.left, node2.right)

            rl = dfs(node2.left, node1.right)
            rr = dfs(node2.right, node1.right)

            return (ll and rr and lr and rl) or (ll and rr) or (lr and rl)
        

        return dfs(root1, root2)