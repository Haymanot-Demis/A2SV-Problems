class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        answer = []
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        for i in range(len(queries)):
            if queries[i][0] == 0:
                answer.append(arr[queries[i][1]])
            else:
                answer.append(arr[queries[i][0] - 1]^arr[queries[i][1]])  
        return answer