#by using adjacency matrix
# Below are the basic operations on the graph:
# Insertion of Nodes/Edges in the graph – Insert a node into the graph.
# Deletion of Nodes/Edges in the graph – Delete a node from the graph.
# Searching on Graphs – Search an entity in the graph.
# Traversal of Graphs – Traversing all the nodes in the graph. 
class GraphWithAdjMatrix:
    def __init__(self, size = 10) -> None:
        self.adjMatrix = [ [ None for i in range(size) ] for j in range(size) ]
        self.vertices = {}
        self.verticesList = [None] * size

    def addVertex(self, indx, value):
        self.vertices[value] = indx
        self.verticesList[indx] = value
    
    def addEdge(self, src:int, dest:int, weight = 1): #by vertices id
        length = len(self.verticesList)
        if src < length and dest < length:
            self.adjMatrix[src][dest] = weight
            self.adjMatrix[dest][src] = weight
        else:
            print("Vertices are not found")
    def getEdges(self):
        length = len(self.verticesList)
        for i in range(length):
            for j in range(length):
                print("(", i, j, "{}".format(self.adjMatrix[i][j]), ")", end=" ")
            print()
    
    def getVertices(self):
        return self.vertices

    def getMAtrix(self):
        return self.adjMatrix

US_cities = GraphWithAdjMatrix()
US_cities.addVertex(0, 'Austin')
US_cities.addVertex(1, 'Atlanta')
US_cities.addVertex(2, 'Chicago')
US_cities.addVertex(3, 'Dallas')
US_cities.addVertex(4, 'Denver')
US_cities.addVertex(5, 'Houston')
US_cities.addVertex(6, 'Washington')

US_cities.addEdge(0,5)
US_cities.addEdge(0,6)
US_cities.addEdge(1,5)
US_cities.addEdge(1,3)
US_cities.addEdge(2,4)
US_cities.addEdge(3,1)
US_cities.addEdge(3,4)
US_cities.addEdge(3,2)
US_cities.addEdge(4,2)
US_cities.addEdge(4,2)
US_cities.addEdge(5,0)
US_cities.addEdge(6,0)
US_cities.addEdge(6,3)
# print(US_cities.getVertices())

# US_cities.getEdges()


#by using adjacency list 
# adjacency list usiong python dixtionary
class GraphWithAdjList():
    def __init__(self) -> None:
        self.adjList = {}
    
    def addVertex(self, data):
        self.adjList[data] = []
    
    def addEdge(self, src, dest, weight = 1):
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

    def getAdjList(self):
        return self.adjList

    def DepthFirstSearch(self, start, visited=None):
        # stack = list()
        # stack.append(start)
        # found = False
        if visited == None:
            visited = list()
        if start not in visited:
            visited.append(start)
        print(start)
        for adj in self.adjList[start]:
            if adj not in visited:
                self.DepthFirstSearch(adj, visited)

        print("visited", visited)
        

    def BreadthFirstSearch(self):
        pass
    

graph = GraphWithAdjList()

graph.addVertex("austin")
graph.addVertex("denver")
graph.addVertex("dallas")
graph.addVertex("chicago")
graph.addVertex("atlanta")
graph.addVertex("houston")
graph.addVertex("washington")

print(graph.getAdjList())

graph.addEdge("austin", "dallas")
graph.addEdge("austin", "houston")
graph.addEdge("denver", "chicago")
graph.addEdge("denver", "atlanta")
graph.addEdge("denver", "dallas")
graph.addEdge("houston", "atlanta")
graph.addEdge("dallas", "washington")
graph.addEdge("atlanta", "washington")

print(graph.getAdjList())
graph.DepthFirstSearch('austin')

