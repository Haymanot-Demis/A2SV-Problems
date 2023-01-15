from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hasmap = defaultdict(list)
        for path in paths:
            fileDirectory = path.split()
            for i in range(1, len(fileDirectory)):
                fileContentIndex = fileDirectory[i].index("(")
                hasmap[fileDirectory[i][fileContentIndex:]].append(fileDirectory[0]  + "/" + fileDirectory[i][:fileContentIndex])
        return[paths for paths in hasmap.values() if len(paths) > 1]