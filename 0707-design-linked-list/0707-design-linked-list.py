class Node:
    def __init__(self, val=0):
        self.value = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self, node=None):
        self.head = node
        self.end = node
        self.length = 0
        # print("init",self.head)

    def get(self, index: int) -> int:
        temp = self.head
        if index >= 0 and index < self.length:
            while index > 0:
                temp = temp.next
                index -= 1
            self.getList()
            return temp.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        # print("addAtHead")
        if not self.head:
            self.head = node
            self.end = self.head
        else:
            temp = self.head
            node.next = temp
            temp.prev = node
            self.head = node 
            if self.end is self.head:
                self.end = self.head.next
        self.length += 1
        # self.getList()

    def addAtTail(self, val: int) -> None:
        # print(self.end.value)
        node = Node(val)
        if self.end == None:
            self.head = node
            self.end = self.head
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node
        self.length += 1
        # self.getList()

    def addAtIndex(self, index: int, val: int) -> None:
        dummynode = Node()
        dummynode.next = self.head
        if index >= 0 and index <= self.length:
            temp = dummynode
            while index > 0:
                temp = temp.next
                index -= 1
            node = Node(val)
            if temp is self.end:
                self.end = node
            node.prev = temp
            node.next = temp.next
            temp.next = node
            self.length += 1
        self.head = dummynode.next
        # if index == 0:
        #     self.addAtHead(val)
        # elif index > 0 and index <= self.length:
        #     temp = self.head
        #     while index > 1:
        #         temp = temp.next
        #         index -= 1
        #     # print("val", temp.value)
        #     node = Node(val)
        #     if temp is self.end:
        #         self.end = node
        #     node.prev = temp
        #     node.next = temp.next
        #     temp.next = node
        #     self.length += 1
        # self.getList()             

    def deleteAtIndex(self, index: int) -> None:
        dummynode = Node()
        dummynode.next = self.head
        if index >= 0 and index < self.length:
            temp = dummynode
            while index > 0:
                temp = temp.next
                index -= 1
            print(temp.next.value)
            if temp.next is self.end:
                self.end = temp
            nodeToBeDeleted = temp.next
            temp.next = temp.next.next
            if temp.next:
                temp.next.prev = temp
            del nodeToBeDeleted
            self.length -= 1
        self.head = dummynode.next
        self.getList()
        # if index == 0:
        #     self.head = self.head.next
        #     self.length -= 1
        # elif index > 0 and index < self.length:
        #     temp = self.head
        #     while index > 1:
        #         temp = temp.next
        #         index -= 1
        #     if temp.next is self.end:
        #         self.end = temp
        #     nodeToBeDeleted = temp.next
        #     temp.next = temp.next.next
        #     if temp.next:
        #         temp.next.prev = temp
        #     del nodeToBeDeleted
        #     self.length -= 1
        # self.getList()

    def getList(self):
        temp = self.head
        while temp:
            print(temp.value, end=", ")
            temp = temp.next
        print(" length", self.length)              
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)