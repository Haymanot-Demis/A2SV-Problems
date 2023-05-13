class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for pre, course in prerequisites:
            graph[course].append(pre)
        
        prerequisite = defaultdict(set)

        visited = set()

        for course in range(numCourses):
            if course not in visited:

                self.dfs(graph, course, visited, prerequisite)
        
        answer = [False] * len(queries)
        for i in range(len(queries)):
            if queries[i][0] in prerequisite[queries[i][1]]:
                answer[i] = True

        return answer
    def dfs(self, prerequisite, course, visited, all_prerequisite):
        visited.add(course)
        pres = set()
        for pre in prerequisite[course]:
            if pre not in visited:
                pres |= self.dfs(prerequisite, pre, visited, all_prerequisite)
            else:
                pres |= all_prerequisite[pre] | set([pre])
            
        all_prerequisite[course] |= pres
        return pres | set([course])