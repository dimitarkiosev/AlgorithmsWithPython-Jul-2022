= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Areas in Matrix
= = = = = = = = = = = = = = = = = = = = = = = = =
rows = int(input())
cols = int(input())

matrix = []
visited = []
areas = dict()

for _ in len(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)
    
def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col] == True:
        return
    if matrix[row][col] == parent:
        return
    
    visited[row][col] = True
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)
    
for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1
        
= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Cycles in a Graph
= = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)
    cycles.remove(node)


graph = dict()

while True:
    line = input()
    if line == 'End':
        break
    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

try:
    visited = set()
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Salaries
= = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1

    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    salaries[node] = salary
    return salary

nodes = int(input())
graph = list()

for _ in range(nodes):
    line = input()
    children = []
    for idx, ch in enumerate(line):
        if ch == 'Y':
            children.append(idx)
    graph.append(children)

salaries = [None] * nodes

result = 0
for node in range(nodes):
    salary = dfs(node, graph, salaries)
    result += salary

print(result)

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Break Cycles
= = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node, destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()
    dfs(source, destination, graph, visited)
    return destination in visited


nodes = int(input())
graph = dict()
edges = list()

for _ in range(nodes):
    line = input()
    node, children_str = line.split(' -> ')
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

removed_edges = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for first, second in removed_edges:
    print(f'{first} - {second}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Road Reconstruction
= = = = = = = = = = = = = = = = = = = = = = = = =
def dfs(node,  graph, visited):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)

nodes_count = int(input())
edges_count = int(input())
graph = list()
edges = list()

[graph.append([]) for _ in range(nodes_count)]

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

important_streets = list()
for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

print('Important streets:')
for first, second in important_streets:
    print(f'{first} {second}')

= = = = = = = = = = = = = = = = = = = = = = = = = 