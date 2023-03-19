# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def equalToAverage(node):
            if not node:
                return [0, 0, 0]
            left_nodes, l_sum, l_count = equalToAverage(node.left)
            right_nodes, r_sum, r_count = equalToAverage(node.right)

            if node.val == (l_sum + r_sum + node.val) // (left_nodes + right_nodes + 1):
                return [left_nodes + right_nodes + 1, l_sum + r_sum + node.val, l_count + r_count + 1]
            return [left_nodes + right_nodes + 1, l_sum + r_sum + node.val, l_count + r_count]
        
        result = equalToAverage(root)
        return result[2]