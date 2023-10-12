# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        freq = defaultdict(int)
        ans = []
        def dfs(node):
            if not node:
                return ""

            subtree = str(node.val) + "/" + dfs(node.left) + "/" + dfs(node.right)
            freq[subtree] += 1
            if freq[subtree] == 2:
                ans.append(node)

            return subtree

        dfs(root)
        return ans