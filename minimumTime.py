from typing import List
from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        incomings = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            incomings[v] += 1
        queue = deque()

        for job in range(1, n + 1):
            if incomings[job] == 0:
                queue.append(job)

        level = 0
        time = [0] * n
        while queue:
            level += 1
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                time[curr - 1] = level
                for next in graph[curr]:
                    incomings[next] -= 1
                    if incomings[next] == 0:
                        queue.append(next)
                        
        return " ".join(map(str, time))