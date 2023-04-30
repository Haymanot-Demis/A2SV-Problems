class ThroneInheritance:

    def __init__(self, kingName: str):
        self.King = kingName
        self.Family_Tree = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.Family_Tree[parentName].append(childName)        

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        currOrder = []
        visited = set()
        def successor(x):
            if x not in self.dead:
                currOrder.append(x)
            visited.add(x)
            for child in self.Family_Tree[x]:
                if child not in visited:
                    successor(child)
                    
        successor(self.King)
        return currOrder        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()