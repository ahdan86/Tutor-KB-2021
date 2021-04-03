import queue


class Node:
    def __init__(self, name):
        self.name = name
        self.Heuristic = 0
        self.GValue = 0
        self.neighbors = {}

    def assignHeuristic(self, value):
        self.Heuristic = value

    def assignG(self, value):
        self.GValue = value

    def addNeighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

    def listNeighbors(self):
        for neigbor in self.neighbors:
            print(neigbor.name)


class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def listNode(self):
        for i in self.nodes:
            print(i.name)


# Asistensi KB
# Define your graph!

a = Node('NodeA')
b = Node('NodeB')
c = Node('NodeC')
d = Node('NodeD')

"""
10  5
A - B \
  \ C - D
    3   0
"""

a.addNeighbor(b, 7)
a.addNeighbor(c, 10)

b.addNeighbor(a, 7)
b.addNeighbor(d, 1)

c.addNeighbor(a, 10)
c.addNeighbor(d, 10)

d.addNeighbor(b, 1)
d.addNeighbor(c, 10)

graph = Graph("graph")
graph.addNode(a)
graph.addNode(b)
graph.addNode(c)
graph.addNode(d)

# Set heuristic value
a.assignHeuristic(10)
b.assignHeuristic(5)
c.assignHeuristic(3)
d.assignHeuristic(0)

visited = {
    a: False,
    b: False,
    c: False,
    d: False
}

GlobalGValue = {
    a: 99999,
    b: 99999,
    c: 99999,
    d: 99999
}

priorityQueue = queue.PriorityQueue()

goal = d

GlobalGValue[a] = 0
a.assignG(0)
priorityQueue.put((a.Heuristic + a.GValue, a))

while not priorityQueue.empty():
    item = priorityQueue.get()
    print("F : " + str(item[0]))
    node = item[1]
    print("Node : " + node.name)
    visited[node] = True
    if node == goal:
        print("Found goal")
        break
    for neighbor in node.neighbors:
        GValue = node.neighbors[neighbor] + node.GValue
        if GValue < GlobalGValue[neighbor]:
            neighbor.assignG(GValue)
        if not visited[neighbor]:
            priorityQueue.put((neighbor.Heuristic + neighbor.GValue, neighbor))
