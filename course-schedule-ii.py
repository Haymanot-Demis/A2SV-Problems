class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        dependency = defaultdict(list)
        color = [0] * numCourses

        for course, pre in prerequisites:
            dependency[pre].append(course)
        answer = []
        for course in range(numCourses):
            if not self.dfs(dependency, course, color, answer):
                return []
                
        return answer[::-1]

    def dfs(self, dependency, course, color, answer):
        if color[course] == 1:
            return False
        
        if color[course] == 2:
            return True

        color[course] = 1
        
        for next_course in dependency[course]:
            if not self.dfs(dependency, next_course, color, answer):
                return False
        
        color[course] = 2
        answer.append(course)
        return True