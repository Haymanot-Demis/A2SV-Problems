class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph =  defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
            
        tot_time = 0
        queue = deque([(headID, 0)])

        while queue:
            length  = len(queue)
            time = 0
            for i in range(length):
                curr, time = queue.popleft()
                tot_time = max(time, tot_time)
                for adj in graph[curr]:
                    queue.append((adj, time + informTime[curr])) 
                 
        return tot_time