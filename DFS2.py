# dfs.py - Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=" ")
    visited.add(start)
    
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    "A": [("B", 4), ("C", 5)],
    "B": [("A", 4), ("C", 11), ("D", 9), ("E", 7)],
    "C": [("A", 5), ("B", 11), ("E", 3)],
    "D": [("B", 9), ("E", 13), ("F", 2)],
    "E": [("B", 7), ("C", 3), ("D", 13), ("F", 6)],
    "F": [("D", 2), ("E", 6)]
}

dfs(graph, "A")