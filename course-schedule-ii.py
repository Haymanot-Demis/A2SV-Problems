class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        dependency = defaultdict(list)

        for course, pre in prerequisites:
            dependency[pre].append(course)
            incoming[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if course not in incoming:
                queue.append(course)
        answer = []
            
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            for course in dependency[curr]:
                incoming[course] -= 1
                if incoming[course] == 0:
                    queue.append(course)
        
        if len(answer) == numCourses:
            return answer
            
        return []