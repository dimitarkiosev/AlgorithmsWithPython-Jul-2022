1. Shortest Path
 A. in Unweighted Graph
  def bfs(G, start, end)
    visited[start] = true    
    queue.enqueue(start)
    while (!queue.isEmpty())
        v = queue.dequeue()
        if v is end:
            return v
        for all edges from v to w in G.adjacentEdges(v):
            if w is not labeled as discovered then
                label w as discovered
                w.parent = v
                queue.enqueue(w)

 B. Dijkstra Algorithm (weighted graph) - use 'priority queue' (sorting elements using some filter)
  Initially calculate all direct distances d[] from S
  Enqueue that start node S
  While (queue not empty)
    Dequeue the nearest vertex B
    Enqueue all unvisited child nodes of B
    For each edge {B → A}, improve d[A] through B:
        d[S → A] = min(d[S → A], d[S → B] + weight[B → A])

 C. Bellman-Ford (Shorts Path in Graph with Negative Edges)


2. MST
 A. Kruskal's Algorithm
  
 B. Prim's Algorithm
  



= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Shortest Path in Unweighted Graph
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque


nodes = int(input())
edges = int(input())
graph = list()

[graph.append([]) for _ in range(nodes+1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start_node] = True

queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == destination_node:
        break

    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()
node = destination_node

while node is not None:
    path.appendleft(node)
    node = parent[node]

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Dijkstra's Algorithm
= = = = = = = = = = = = = = = = = = = = = = = = =
from queue import PriorityQueue
from collections import deque

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
graph = dict()

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start = int(input())
target = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == target:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])

    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Bellman-Ford
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True
    if not updated:
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
    print(distance[target])

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Kruskal's Algorithm
= = = = = = = = = = = = = = = = = = = = = = = = =
class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node

edges = int(input())
graph = list()

max_node = float('-inf')
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

parent = [num for num in range(max_node+1)]

forest = list()

for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Prim's Algorithm
= = = = = = = = = = = = = = = = = = = = = = = = =

= = = = = = = = = = = = = = = = = = = = = = = = = 