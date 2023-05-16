from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        # chars = set()
        incomings = defaultdict(int)
        for i in range(N - 1):
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            
            p1, p2 = 0, 0
            while p1 < len(word1) and p2 < len(word2) and word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
            
            if p1 < len(word1) and p2 < len(word2):
                graph[word1[p1]].append(word2[p2])
                incomings[word2[p2]] += 1
                # chars.add(word1[p1])
                # chars.add(word2[p2])
                
        visited = set()
        queue = deque()
        answer = []
        for i in range(K):
            if incomings[chr(97 + i)] == 0:
                queue.append(chr(97 + i))
            
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            for adj in graph[curr]:
                incomings[adj] -= 1
                if incomings[adj] == 0:
                    queue.append(adj)
                    
        return "".join(answer)