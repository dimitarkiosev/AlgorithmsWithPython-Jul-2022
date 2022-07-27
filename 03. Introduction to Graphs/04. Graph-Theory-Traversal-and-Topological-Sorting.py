https://judge.softuni.org/Contests/Compete/Index/3462#0
INTRODUCTION to GRAPHS
1. Graph Definitions and Terminology
  G(V, E) - set of nodes V with many-to-many relations between them (edges E)
  Node
    element of a graph
    have name/value
    keep list of child nodes
  Edge - connection between 2 nodes
    - directed/inderected
    - weighted / unweighted
    - have name/value
  Type Graphs:  
    - Directed graph - edges have direction
    - Undirected graph
    - Weighted graph
    
  Path - sequence of nodes (n1, n2, ..)
  Cycle - start and end at starting node
    simple path - without cycle
    acyclic graph


2. Representing Graphs
    adjacency list - each note holds a list of its neghbors
    adjacency matrix - matrix nodes x nodes and 1 show that both nodes have connection
    list of edges

3. Graph Traversal Algotirhms
    - Depth-First-Search (DFS) - implement with recursion
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
}
visited = set()
for node in graph:
    dfs(node, graph, visited)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(node, graph, visited)

    print(node, end=' ')

graph = [
    [3, 6],
    [3, 6, 4, 2, 5],
    [1, 4, 5],
    [5, 0, 1],
    [1, 2, 6],
    [2, 1, 3],
    [0, 1, 4]
]

visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(node, graph, visited)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    
    - Breadth-First-Search (BFS) - implement with queue
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

def bfs(node, graph, visited):
    if node in visited:
        return

    queue = deque([node])
    visited.add(node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    23: [21],
    6: [],
}
visited = set()

for node in graph:
    bfs(node, graph, visited)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

4. Connected Components

5. Topological Sorting
    Source Removal
    DFS Algotihms

#= = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Connected Components 
#= = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * nodes
for node in range(nodes):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    print(f"Connected component: {' '.join([str(x) for x in component])}")
    
#= = = = = = = = = = = = = = = = = = = = = = = = = 
#02. Topological Sorting 
#= = = = = = = = = = = = = = = = = = = = = = = = =
def find_dependences(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_null(dependences_by_node):
    for node, dependencies in dependences_by_node.items():
        if dependencies == 0:
            return node
    return None


nodes = int(input())
graph = dict()

for _ in range(nodes):
    line = input()
    line_parts = line.split('->')
    node = line_parts[0].strip()
    if line_parts[1]:
        children = line_parts[1].strip().split(', ')
    else:
        children = []
    graph[node] = children

dependences_by_node = find_dependences(graph)
has_cycles = False
sorted_nodes = list()

while dependences_by_node:
    node_to_remove = find_node_null(dependences_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    dependences_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependences_by_node[child] -= 1

if has_cycles:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")

#= = = = = = = = = = = = = = = = = = = = = = = = = 