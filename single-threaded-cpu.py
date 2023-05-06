class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = ([*tasks[i], i])

        tasks.sort(reverse=True, key=lambda task : task[0])
        waiting_queue = []

        execution_seq = []
        time = tasks[-1][0]

        while tasks:
            incoming = False
            while tasks and tasks[-1][0] <= time:
                incoming = True
                task = tasks.pop()
                self.heappush(waiting_queue, task)

            if waiting_queue:
                time  += waiting_queue[0][1]
                execution_seq.append(self.heappop(waiting_queue)[2])
            elif not incoming and tasks:
                time = tasks[-1][0]

        while waiting_queue:
            execution_seq.append(self.heappop(waiting_queue)[2])

        return execution_seq

    def buildheap(self, arr):
        parent = len(arr) // 2 - 1
        while parent > -1:
            self.heapify(arr, parent)
            parent -= 1
        
    def compare(self, task1, task2):             
        if task1[1] < task2[1]:
            return True

        if task1[1] == task2[1] and task1[2] < task2[2]:
            return True

        return False
    def heapify(self, arr, parent):
        left = 2 * parent + 1
        right = left  + 1
        if left < len(arr):
            first = parent
            if self.compare(arr[left], arr[first]):
                first = left

            if right < len(arr) and self.compare(arr[right], arr[first]):
                first = right
                
            
            if first != parent:
                arr[first], arr[parent] = arr[parent], arr[first]
                self.heapify(arr, first)
    def heappop(self, arr):
        arr[0], arr[-1] = arr[-1], arr[0]
        value = arr.pop()
        self.heapify(arr, 0)
        return value

    def heappush(self, arr, val):
        arr.append(val)
        parent = len(arr)//2 - 1
        child = len(arr) - 1
         
        while parent > -1 and self.compare(arr[child], arr[parent]):
            arr[child], arr[parent] = arr[parent], arr[child]
            child = parent
            parent = (child - 1) // 2