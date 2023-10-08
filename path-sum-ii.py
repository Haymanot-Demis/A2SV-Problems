# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, prefixsum):
            nonlocal targetSum
            if not node:
                return []
                
            prefixsum += node.val
            if not node.left and not node.right:
                if prefixsum == targetSum:
                    return [[node.val]]
                return []
            
            left = []
            right = []

            if node.left:
                left = dfs(node.left, prefixsum)
            if node.right:
                right = dfs(node.right, prefixsum)

            all = []

            for path in left:
                all.append(path + [node.val])
            
            for path in right:
                all.append(path + [node.val])
            
            return all
        
        paths = dfs(root, 0)

        answer = []   

        for path in paths:
            answer.append(path[::-1])

        return answer