= = = = = = = = = = = = = = = = = = = = = = = = = 
01. The Story Telling
= = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, graph, visited, result):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.append(node)


graph = {}

while True:
    line = input()
    if line == "End":
        break
    node, children_str = [x.strip() for x in line.split('->')]
    children = children_str.split()
    graph[node] = children

visited = set()
result = list()

for node in graph:
    dfs(node, graph, visited, result)

print(' '.join(result[::-1]))

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Time
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

s1 = input().split()
s2 = input().split()

rows = len(s1) + 1
cols = len(s2) + 1

dp = list()
for _ in range(rows):
    dp.append([0] * cols)

for row in range(1, rows):
    for col in range(1, cols):
        if s1[row-1] == s2[col-1]:
            dp[row][col] = dp[row-1][col-1] + 1
        else:
            dp[row][col] = max(dp[row-1][col], dp[row][col-1])

row = rows - 1
col = cols - 1
result = deque()

while row > 0 and col > 0:
    if s1[row-1] == s2[col-1]:
        result.appendleft(s1[row-1])
        row -= 1
        col -= 1
    elif dp[row-1][col] > dp [row][col-1]:
        row -= 1
    else:
        col -= 1

print(*result, sep=" ")
print(dp[rows-1][cols-1])

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Chain Lighting
= = = = = = = = = = = = = = = = = = = = = = = = =
from queue import PriorityQueue

class Edge:
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance

    def __gt__(self, other):
        return self.distance > other.distance

def calc_damage(jumps, damage):
    for _ in range(jumps):
        damage = damage // 2

    return damage

def prim(node, damage, damage_by_node, graph):
    damage_by_node[node] += damage

    tree = {node}
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = -1, -1

        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        if min_edge.first not in tree and min_edge.second in tree:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node == -1:
            continue

        tree.add(non_tree_node)
        for edge in graph[non_tree_node]:
            pq.put(edge)

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += calc_damage(jumps[non_tree_node], damage)


nodes = int(input())
edges = int(input())
lightnings = int(input())

graph = list()
[graph.append([]) for _ in range(nodes)]


for _ in range(edges):
    first, second, distance = [int(x) for x in input().split()]
    edge = Edge(first, second, distance)
    graph[first].append(edge)
    graph[second].append(edge)

damage_by_node = [0] * nodes

for _ in range(lightnings):
    node, damage = [int(x) for x in input().split()]
    prim(node, damage, damage_by_node, graph)

print(max(damage_by_node))

= = = = = = = = = = = = = = = = = = = = = = = = =