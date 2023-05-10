class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = defaultdict(list)
        incoming = defaultdict(int)

        for course, pre in prerequisites:
            dependency[pre].append(course)
            incoming[course] += 1
        queue = deque()
        order  = []

        for course in range(numCourses):
            if course not in incoming:
                queue.append(course)
        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for course in dependency[curr]:
                incoming[course] -= 1
                if incoming[course] == 0:
                    queue.append(course)
                
        if len(order) < numCourses:
            return False
        
        return True