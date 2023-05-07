class LockingTree:
    def __init__(self, parent: List[int]):
        self.child = defaultdict(list)
        self.parent = defaultdict(lambda : None)
        for child, parent in enumerate(parent[1:]):
            self.child[parent].append(child + 1)
            self.parent[child + 1] = parent
        self.Locker = defaultdict(int)                

    def lock(self, num: int, user: int) -> bool:
        if not self.Locker[num]:
            self.Locker[num] = user
            return True
        return False        

    def unlock(self, num: int, user: int) -> bool:
        if self.Locker[num] == user:
            self.Locker[num] = 0
            return True
        return False        

    def upgrade(self, num: int, user: int) -> bool:
        ancestor = not self.LockedAncestor(num)
        descendant = self.LockedDescendant(num)

        if ancestor and descendant:
            self.LockDown(num)
            self.Locker[num] = user
            return True
        return False
    
    def LockedAncestor(self, node):
        while node and not self.Locker[node]:
            node = self.parent[node]
        
        if not node and not self.Locker[node]:
            return False
        return True

    def LockedDescendant(self,node):
        if self.Locker[node]:
            return True
        
        for child in self.child[node]:
            if self.LockedDescendant(child):
                return True
        return False

    def LockDown(self, node):
        self.Locker[node] = 0
        for child in self.child[node]:
            self.LockDown(child)       


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)