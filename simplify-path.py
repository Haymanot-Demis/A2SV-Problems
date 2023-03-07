class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        length = len(path)
        path = path.split("/")
        unnecessary = set([".", "", ".."])
        
        for string in path:
            if string == ".." and stack:
                stack.pop()
            elif string not in unnecessary:
                stack.append(string)
        
        return "/" + "/".join(stack)