# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def gotoNextLevel(node, level, values):
            if not node:
                return values
            if len(values) <= level:
                values.append([node.val])
            else:
                values[level].append(node.val)
            gotoNextLevel(node.left, level + 1, values)
            gotoNextLevel(node.right, level + 1, values)
            return values
        values = gotoNextLevel(root, 0, [])
        return [value[-1] for value in values]