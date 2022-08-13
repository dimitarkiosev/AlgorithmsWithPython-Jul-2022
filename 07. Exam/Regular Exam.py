= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Conditional Expression Resolver - 100/100
= = = = = = = = = = = = = = = = = = = = = = = = =
expression = input().split()

while True:
    result = ''
    for x in range(len(expression)-1, -1, -1):
        if expression[x] == '?':
            statement = expression[x-1]
            if statement == 't':
                result = expression[x + 1]
            else:
                result = expression[x + 3]
            expression[x-1] = result
            expression.pop(x)
            expression.pop(x)
            expression.pop(x)
            expression.pop(x)
            break
    if len(expression) == 1:
        break

print(expression[0])

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Guards - 100/100
= = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = 1

    for child in graph[node]:
        dfs(child, graph, visited)

nodes = int(input())
edges = int(input())
graph = list()
[graph.append([]) for _ in range(nodes+1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

current = int(input())

visited = dict()
for x in range(1, nodes+1):
    visited[x] = 0

dfs(current, graph, visited)

for key, value in visited.items():
    if value == 0:
        print(key, end=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Arbitrage - изкарва правилни стойности в distance, но не е оправен Output-а и не е събмината
= = = = = = = = = = = = = = = = = = = = = = = = =
from queue import PriorityQueue
from collections import deque

class Edge:
    def __init__(self, from_cur, to_cur, price):
        self.from_cur = from_cur
        self.to_cur = to_cur
        self.price = price

edges = int(input())
graph = dict()

for _ in range(edges):
    line = input().split()
    from_cur = line[0]
    to_cur = line[1]
    price = float(line[2])
    if from_cur not in graph:
        graph[from_cur] = []
    if to_cur not in graph:
        graph[to_cur] = []
    graph[from_cur].append(Edge(from_cur, to_cur, price))

target = input()
cur_count = len(graph.keys())
distance = dict()

for key in graph.keys():
    distance[key] = -1

pq = PriorityQueue()
pq.put((-1, target))

node = ''
frist = 0

while not pq.empty():
    max_distance, node = pq.get()
    if node == target and frist == 1:
        break
    for edge in graph[node]:
        child = edge.to_cur
        new_distance = -(abs(max_distance * edge.price))
        if new_distance < distance[child]:
            distance[child] = new_distance
            pq.put((new_distance, child))
    frist = 1

print(distance)



= = = = = = = = = = = = = = = = = = = = = = = = = 