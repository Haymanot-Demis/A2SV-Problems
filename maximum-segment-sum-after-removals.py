class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        self.init_union_find(len(nums), nums)
        answer = [0] * len(nums)
        max_sum = 0
        pos = -2
        alives = set()
        removeQueries = removeQueries[1:][::-1]
        for indx in removeQueries:
            if (indx + 1) in alives:
                self.union(indx, indx + 1)
            if (indx - 1) in alives:
                self.union(indx, indx - 1)
            max_sum = max(max_sum, self.sum[self.find(indx)])
            answer[pos] = max_sum
            alives.add(indx)
            pos -= 1
        return answer            

        
    def init_union_find(self, size, nums):
        self.rep = {i:i for i in range(size)}
        self.sum = {i:nums[i] for i in range(size)}
        self.size = defaultdict(lambda : 1)

    def find(self, u):
        if u == self.rep[u]:
            return u
        self.rep[u] = self.find(self.rep[u])
        return  self.rep[u]
    
    def union(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        
        if rep_u != rep_v:
            if self.size[rep_u] >= self.size[rep_v]:
                self.rep[rep_v] = rep_u
                self.size[rep_u] += self.size[rep_v]
                self.sum[rep_u] += self.sum[rep_v]
            else:
                self.rep[rep_u] = rep_v
                self.size[rep_v] += self.size[rep_u]
                self.sum[rep_v] += self.sum[rep_u]