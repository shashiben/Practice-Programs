from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def TopologicalUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if(not visited[i]):
                self.TopologicalUtil(i, visited, stack)
        stack.insert(0, v)

    def Topological(self):
        visited = [False]*self.vertices
        stack = []
        for i in range(self.vertices):
            if(not visited[i]):
                self.TopologicalUtil(i, visited, stack)
        print(stack)


n = int(input("Enter no of vertices:"))
g = Graph(n)
for i in range(n):
    x = list(map(int, input("Enter u and v values:").split()))
    g.addEdge(x[0], x[1])
g.Topological()
