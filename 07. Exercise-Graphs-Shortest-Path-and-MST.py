= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Distance Between Vertices - Shortest Path
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque


def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}

    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node

    return parent


def find_path_size(parent, destination):
    node = destination
    size = 0
    while node is not None:
        node = parent[node]
        size += 1
    return size - 1

nodes = int(input())
pairs = int(input())
graph = dict()

for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    if children_str:
        children = [int(x) for x in children_str.split()]
    else:
        children = list()
    graph[node] = children


for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parent = find_shortest_path(graph, source, destination)

    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    size = find_path_size(parent, destination)

    print(f'{{{source}, {destination}}} -> {size}')
    
= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Most Reliable Path - DIJKSTRA
= = = = = = = = = = = = = = = = = = = = = = = = =
from queue import PriorityQueue
from collections import deque

class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

nodes = int(input())
edges = int(input())
graph = list()
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

start_node = int(input())
end_node = int(input())

pq = PriorityQueue()
pq.put((-100, start_node))

distance = [float('-inf')] * nodes
distance[start_node] = 100

parent = [None] * nodes

while not pq.empty():
    max_distance, node = pq.get()
    if node == end_node:
        break
    for edge in graph[node]:
        child = edge.second if edge.first == node else edge.first

        new_distance = -max_distance * edge.weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))

print(f'Most reliable path reliability: {distance[end_node]:.2f}%')

path = deque()
node = end_node
while node is not None:
    path.appendleft(node)
    node = parent[node]
print(*path, sep=' -> ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Cheap Town Tour - KRUSKAL
= = = = = = = = = = = = = = = = = = = = = = = = =
def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node

nodes = int(input())
edges = int(input())
graph = list()

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append((first, second, weight))

parent = [num for num in range(nodes)]
total_cost = 0

for first, second, weight in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root == second_node_root:
        continue
    
    parent[first_node_root] = second_node_root
    total_cost += weight

print(f'Total cost: {total_cost}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Undefined - BELMAN
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    graph.append((first, second, weight))

source = int(input())
destination = int(input())

distance = [float('inf')] * (nodes + 1)
distance[source] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for first, second, weight in graph:
        if distance[first] == float('inf'):
            continue

        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            distance[second] = new_distance
            parent[second] = first
            updated = True

    if not updated:
        break

for first, second, weight in graph:
    new_distance = distance[first] + weight
    if new_distance < distance[second]:
        print('Undefined')
        break
else:
    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
    print(distance[destination])
    
= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Cable Network - PRIM's
= = = = = = = = = = = = = = = = = = = = = = = = =
from queue import PriorityQueue

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

budget = int(input())
nodes = int(input())
edges = int(input())

graph = list()
[graph.append([]) for _ in range(nodes)]

tree = set()
for _ in range(edges):
    edge_data = input().split()
    start, end, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    graph[start].append(Edge(start, end, weight))
    graph[end].append(Edge(start, end, weight))

    if len(edge_data) == 4:
        tree.add(start)
        tree.add(end)

pq = PriorityQueue()

for node in tree:
    for edge in graph[node]:
        pq.put(edge)

budget_used = 0

while not pq.empty():
    min_edge = pq.get()

    non_tree_node = None
    if min_edge.start in tree and min_edge.end not in tree:
        non_tree_node = min_edge.end
    if min_edge.start not in tree and min_edge.end in tree:
        non_tree_node = min_edge.start

    if non_tree_node is None:
        continue

    if budget_used + min_edge.weight > budget:
        break

    budget_used += min_edge.weight
    tree.add(non_tree_node)
    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f'Budget used: {budget_used}')

= = = = = = = = = = = = = = = = = = = = = = = = = 