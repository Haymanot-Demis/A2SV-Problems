class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])

        while queue:
            curr = queue.popleft()
            for key in rooms[curr]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
            
        return len(visited) == len(rooms)