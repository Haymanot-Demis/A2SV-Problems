class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def nextLeft(slot):
            if int(slot) > 0:
                return str(int(slot) - 1)
            return str(9)

        def nextRight(slot):
            if int(slot) < 9:
                return str(int(slot) + 1)
            return str(0)
        
        deadends = set(deadends)
        pin = "0000"
        if pin in deadends:
            return -1
        if pin == target:
            return 0

        queue = deque([pin])
        visited = set([pin])
        turns = 0

        while queue and target != pin:
            turns += 1
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                if curr == target:
                    pin = curr
                    break
                
                for i in range(4):
                    left_adj_pin = curr[0:i] + nextLeft(curr[i]) + curr[i+1:]

                    if left_adj_pin not in visited and left_adj_pin not in deadends:
                        queue.append(left_adj_pin)
                        visited.add(left_adj_pin)

                    right_adj_pin = curr[0:i] + nextRight(curr[i]) + curr[i+1:]

                    if right_adj_pin not in visited and right_adj_pin not in deadends:
                        queue.append(right_adj_pin)
                        visited.add(right_adj_pin)

        return turns - 1 if target == pin else -1