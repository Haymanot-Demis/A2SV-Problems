# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.dfs(root, 0, defaultdict(int, {0:1}), targetSum)
    def dfs(self, node, prefix_sum, hash_table, target):
        if not node:
            return 0

        prefix_sum += node.val
        count = 0
        count += hash_table[prefix_sum - target]
        
        hash_table_c = hash_table.copy()
        hash_table_c[prefix_sum] += 1

        left = self.dfs(node.left, prefix_sum, hash_table_c, target)
        right = self.dfs(node.right, prefix_sum, hash_table_c, target)

        return left + right + count