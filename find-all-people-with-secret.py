class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        parent = {i:i for i in range(n)}
        parent[0] = firstPerson
        ans = set([0,firstPerson])
        graph = defaultdict(list)

        def find(num):
            if parent[num] != num:
                x = find(parent[num])
                parent[num] = x
            return parent[num]
        
        def union(num1,num2):
            p = find(num1)
            q = find(num2)

            if p == firstPerson or q == firstPerson:
                parent[p] = firstPerson
                parent[q] = firstPerson
                ans.add(num1)
                ans.add(num2)
            else:
                if p < q:
                    parent[q] = p
                else:
                    parent[p] = q

        def separate(x, y):
            p = find(x)
            q = find(y)

            if p == firstPerson or q == firstPerson:
                ans.add(x)
                ans.add(y)
            else:
                parent[x] = x
                parent[y] = y


        meetings = sorted(meetings, key=lambda x:x[-1])
        left = 0
        for idx in range(len(meetings)):
            if meetings[left][2] != meetings[idx][2]:
                for i in range(left, idx):
                    separate(meetings[i][0], meetings[i][1])
                left = idx

            union(meetings[idx][0],meetings[idx][1])
            
        
        for i in range(left, len(meetings)):
            separate(meetings[i][0], meetings[i][1])

        return ans