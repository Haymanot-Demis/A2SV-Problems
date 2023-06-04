# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_list = defaultdict(list)
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                adj_list[curr.val].append(curr.left.val)
                adj_list[curr.left.val].append(curr.val)
            if curr.right:
                queue.append(curr.right)
                adj_list[curr.val].append(curr.right.val)
                adj_list[curr.right.val].append(curr.val)
            
        queue = deque([start])
        infected = set([start])

        time = 0
        while queue:
            length = len(queue)
            time += 1
            for _ in range(length):
                curr = queue.popleft()

                for adj in adj_list[curr]:
                    if adj not in infected:
                        queue.append(adj)
                        infected.add(adj)
        return time - 1