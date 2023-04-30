class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def distance(x1, y1, x2, y2):
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        adj_bombs_list = defaultdict(list)
        for bomb_i, data_i in enumerate(bombs):
            for bomb_j, data_j in enumerate(bombs[bomb_i + 1:]):
                if bomb_i != bomb_j + bomb_i + 1:

                    if distance(data_i[0], data_i[1], data_j[0], data_j[1]) <= data_i[2]:
                        # if distance b/n centers is less than or equal to radius
                        adj_bombs_list[bomb_i].append(bomb_j + bomb_i + 1)

                    if distance(data_i[0], data_i[1], data_j[0], data_j[1]) <= data_j[2]:
                        # for the reverse one
                        adj_bombs_list[bomb_j + bomb_i + 1].append(bomb_i)      
        
        max_detonation = 0
        for bomb_i, data_i in enumerate(bombs):
            detonated = set([bomb_i])
            queue = deque([bomb_i])
            detonated_bombs = 0
            
            while queue:
                length = len(queue)
                detonated_bombs += length

                for i in range(length):
                    curr = queue.popleft()
                    for bomb in adj_bombs_list[curr]:
                        if bomb  not in detonated:
                            queue.append(bomb)
                            detonated.add(bomb)
            max_detonation = max(max_detonation, detonated_bombs)

        return max_detonation