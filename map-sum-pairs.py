class TrieNode:
    def __init__(self):
        self.kids = {}
        self.value = 0
        self.EOW_Value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root

        for ch in key:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            
            node = node.kids[ch] 
            node.value += val
        
        if node.EOW_Value:
            self.overrite(key, node.EOW_Value)

        node.EOW_Value = val
    
    def overrite(self, key, val):
        node = self.root

        for ch in key:
            node = node.kids[ch] 
            node.value -= val
        

    def sum(self, prefix: str) -> int:
        node = self.root

        for ch in prefix:
            if ch not in node.kids:
                return 0
            node = node.kids[ch]
        
        return node.value        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)