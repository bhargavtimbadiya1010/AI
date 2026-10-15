graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

    print(visited)

print("DFS Traversal:")
dfs('A')