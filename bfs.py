from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G':[]
}
print()
def bfs(graph,start):
    visited = set ()
    queue = deque()
    
    visited.add(start)
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        
        print(node,end='')
        
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i) 
        print('q',queue)
        print('s',visited)
        print("="*50)
            
bfs(graph,'A')
        