from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)


g = Graph()
while(True):
    if(input("Enter Y to continue else press other key:") != "Y"):
        break
    x = list(map(int, input("Enter u and v values:").split()))
    g.addEdge(x[0], x[1])
startingVertex = int(input("Enter starting vertex:"))
g.DFS(startingVertex)
