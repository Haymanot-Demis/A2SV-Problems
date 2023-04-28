class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        turns = 0

        while queue:
            turns += 1
            length = len(queue)
            
            for i in range(length):
                position, speed = queue.popleft()
                
                # if accelerate
                new_pos = position + speed
                new_speed = speed * 2

                if new_pos == target:
                    queue = []
                    break

                if (new_pos, new_speed) not in visited:
                    queue.append((new_pos, new_speed))
                    visited.add((new_pos, new_speed))
                
                if position != 0: 
                    # we can declerate (reverse)
                    if speed > 0:
                        new_speed = -1
                    else:
                        new_speed = 1
                    if  (position, new_speed) not in visited:
                        queue.append((position, new_speed))
                        visited.add((position, new_speed))

        return turns