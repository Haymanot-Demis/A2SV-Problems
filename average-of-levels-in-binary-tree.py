# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        levels_average = []
        while queue:
            curr_level_len = len(queue)
            this_level = []
            for i in range(curr_level_len):
                curr = queue.popleft()
                this_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levels_average.append(sum(this_level) / curr_level_len)
        return levels_average