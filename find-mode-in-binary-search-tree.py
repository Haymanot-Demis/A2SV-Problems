# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def mostFrequent(node, counter):
            if not node:
                return counter
            counter[node.val] += 1
            mostFrequent(node.left, counter)
            mostFrequent(node.right, counter)
            return counter

        counter = mostFrequent(root, defaultdict(int))
        max_freq = max(counter.values())
        return [num for num, freq in counter.items() if freq == max_freq]