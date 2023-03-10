# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def gotoNextLevel(node, level, values):
            if not node:
                return values
            if len(values) <= level:
                values.append(deque([node.val]))
            else:
                if level % 2:
                    values[level].appendleft(node.val)
                else:
                    values[level].append(node.val)
            
            gotoNextLevel(node.left, level + 1, values) 
            gotoNextLevel(node.right, level + 1, values) 
            return values
        
        return gotoNextLevel(root, 0, [])