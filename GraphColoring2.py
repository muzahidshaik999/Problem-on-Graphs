# graph_coloring.py - Graph Coloring using a Greedy Algorithm
def graph_coloring(graph):
    color_map = {}
    available_colors = ["Red", "Green", "Blue"]
    
    for node in graph:
        used_colors = {color_map[neighbor] for neighbor, _ in graph[node] if neighbor in color_map}
        for color in available_colors:
            if color not in used_colors:
                color_map[node] = color
                break
    
    return color_map

graph = {
    "A": [("B", 4), ("C", 5)],
    "B": [("A", 4), ("C", 11), ("D", 9), ("E", 7)],
    "C": [("A", 5), ("B", 11), ("E", 3)],
    "D": [("B", 9), ("E", 13), ("F", 2)],
    "E": [("B", 7), ("C", 3), ("D", 13), ("F", 6)],
    "F": [("D", 2), ("E", 6)]
}

print(graph_coloring(graph))