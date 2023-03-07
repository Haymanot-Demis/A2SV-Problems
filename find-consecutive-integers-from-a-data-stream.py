class DataStream:

    def __init__(self, value: int, k: int):
        self.value , self.k = value, k
        self.data_stream = deque()
        self.last_k_nums = defaultdict(int) 
        self.length = 0

    def consec(self, num: int) -> bool:
        self.data_stream.append(num)
        self.last_k_nums[num] += 1
        self.length += 1
        
        if self.length < self.k:
            return False
        if self.length > self.k:
            popped_value = self.data_stream.popleft()
            self.last_k_nums[popped_value] -= 1
            if self.last_k_nums[popped_value] == 0:
                del self.last_k_nums[popped_value]
        if len(self.last_k_nums) == 1 and self.value in self.last_k_nums:
            return True
        return False
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)