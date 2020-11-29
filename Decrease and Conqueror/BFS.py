from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False]*len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if(not visited[i]):
                    queue.append(i)
                    visited[i] = True


g = Graph()
while(True):
    if(input("Enter Y to continue else press other key: ") != "Y"):
        break
    x = list(map(int, input("Enter u and v values:").split()))
    g.addEdge(x[0], x[1])
startingVertex = int(input("Enter starting vertex: "))
g.BFS(startingVertex)
