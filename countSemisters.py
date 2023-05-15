from collections import defaultdict
from collections import deque

def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    courses = set()
    incomings = defaultdict(int)
    for pre, course in prerequisites:
        graph[pre].append(course)
        courses.add(course)        
        courses.add(pre)
        incomings[course] += 1
    queue = deque()
    for course in range(1, n + 1):
        if incomings[course] == 0:
            queue.append(course)
    courses_taken, semisters = bfs(graph, queue, n, incomings)
    if len(courses_taken) == n:
        return semisters
    return -1

def bfs(graph, queue, n, incomings):
    level = 0
    courses = []
    while queue:
        length = len(queue)
        for _ in range(len(queue)):
            curr = queue.popleft()
            courses.append(curr)
            for adj in graph[curr]:
                incomings[adj] -= 1
                if incomings[adj] == 0:
                    queue.append(adj)
        level += 1
    
    return courses, level