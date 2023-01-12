from collections import OrderedDict
class LRUCache: 
    """
    the ordered dict contains the key valu pairsas: at the end the most recently used ones and at the begining the least recently used pairs, after get operation on the pairs we will move them to the top of the dict and when we put pairs we will put them at the end of the dict
    """
    def __init__(self, capacity: int):
        self.cacheCapacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if self.cache.get(key, -1) != -1:
            self.cache.move_to_end(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.get(key)
        if len(self.cache) > self.cacheCapacity:
            self.cache.popitem(last=False)             

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)