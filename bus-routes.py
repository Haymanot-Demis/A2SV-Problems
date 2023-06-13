class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        busses_through = defaultdict(set)
        queue = deque([])

        for bus, bus_stops in enumerate(routes):
            for bus_stop in bus_stops:
                busses_through[bus_stop].add(bus)

            
        visited = set(busses_through[source])

        first_detinations = set()
        for bus in busses_through[source]:
            first_detinations |= set(routes[bus])
        
        first_detinations = first_detinations - set([source])

        queue = deque(first_detinations)
        bus_count = 0

        while queue:
            length = len(queue)
            bus_count += 1

            for _ in range(length):
                bus_stop = queue.popleft()

                if bus_stop == target:
                    return bus_count
                
                for bus in busses_through[bus_stop]:
                    if bus not in visited:
                        visited.add(bus)
                        queue += routes[bus]

        return -1