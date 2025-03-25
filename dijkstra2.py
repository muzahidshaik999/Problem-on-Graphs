import heapq

def dijkstra(graph, start, target):
    pq = []  # Min-heap priority queue
    heapq.heappush(pq, (0, start))  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {start: None}

    while pq:
        cost, node = heapq.heappop(pq)

        if node == target:
            break  # Reached the target

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    # Reconstruct path
    path = []
    node = target
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    return distances[target], path

# Graph representation
Graph = {
    "A": [("B", 4), ("C", 5)],
    "B": [("A", 4), ("C", 11), ("D", 9), ("E", 7)],
    "C": [("A", 5), ("B", 11), ("E", 3)],
    "D": [("B", 9), ("E", 13), ("F", 2)],
    "E": [("B", 7), ("C", 3), ("D", 13), ("F", 6)],
    "F": [("D", 2), ("E", 6)]
}

shortest_distance, path = dijkstra(Graph, "A", "F")
print(f"Shortest Path from A to F: {path} with distance {shortest_distance}")
