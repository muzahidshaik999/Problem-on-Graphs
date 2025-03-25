# cycle_detect.py - Detect Cycle in Graph using DFS
def is_cyclic(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

graph = {
    "A": [("B", 4), ("C", 5)],
    "B": [("A", 4), ("C", 11), ("D", 9), ("E", 7)],
    "C": [("A", 5), ("B", 11), ("E", 3)],
    "D": [("B", 9), ("E", 13), ("F", 2)],
    "E": [("B", 7), ("C", 3), ("D", 13), ("F", 6)],
    "F": [("D", 2), ("E", 6)]
}

print("Cycle Detected:", is_cyclic(graph))