class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikes_list = defaultdict(list)
        for u,v in dislikes:
            dislikes_list[u].append(v)

        visited = set()
        nodes = list(dislikes_list.keys())
        for u in nodes: 
            if (u, 1) in visited or (u, 0) in visited:
                continue
            stack = [(u, 1)]
            visited = set((u, 1))
            

            while stack:
                node, color = stack.pop()
                for adj in dislikes_list[node]:
                    if (adj, color) in visited:
                        return False
                    new_color = 0 if color else 1
                    if (adj, new_color) not in visited:
                        visited.add((adj, new_color))
                        stack.append((adj, new_color))

        return True