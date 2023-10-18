class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = [i for i in range(len(strs))]
        size = [1] * len(strs)

        def find(x):
            if parent[x] != x:
                p = find(parent[x])
                parent[x] = p

            return parent[x]

        def union(x, y):
            p_x = find(x)      
            p_y = find(y)  

            if size[p_x] > size[p_y]:
                parent[p_y] = p_x
                size[p_x] += size[p_y]
            else:
                parent[p_x] = p_y
                size[p_y] += size[p_x]
            
        
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                diff_count = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        diff_count += 1
                    if diff_count > 2:
                        break

                if diff_count <= 2:
                    union(i, j)

        reps = set()
        for i in range(len(strs)):
            reps.add(find(i))

        return len(reps)