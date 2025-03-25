# Problems-on-Graphs

## Graph Algorithms

### Overview

This project implements various graph algorithms on the given weighted undirected graph. The source node is 'A' and the target node is 'F'. The following problems are solved:

1. **Shortest Path (Dijkstra's Algorithm)** - Find the shortest path from 'A' to 'F'.
2. **Breadth-First Search (BFS)** - Implement BFS traversal.
3. **Depth-First Search (DFS)** - Implement DFS traversal.
4. **Cycle Detection** - Detect if the graph contains a cycle.
5. **Graph Coloring** - Color the graph using at most 3 colors ensuring no adjacent nodes have the same color.

---

## Problem 1: Shortest Path (Dijkstra’s Algorithm)

### **Algorithm:**

- Initialize all node distances to infinity except the source node ('A'), which is set to 0.
- Use a priority queue (min-heap) to process nodes with the smallest distance.
- Update adjacent nodes with the minimum distance.
- Continue until the shortest path to the target node ('F') is found.

**Time Complexity:** O((V+E) log V)

---

## Problem 2: Breadth-First Search (BFS)

### **Algorithm:**

- Start at node 'A' and add it to a queue.
- Process each node and enqueue its unvisited neighbors.
- Continue until all nodes are visited.

**Time Complexity:** O(V + E)

---

## Problem 3: Depth-First Search (DFS)

### **Algorithm:**

- Start at node 'A'.
- Use recursion (or a stack) to explore each node deeply before backtracking.
- Visit all nodes.

**Time Complexity:** O(V + E)

---

## Problem 4: Cycle Detection (DFS Approach)

### **Algorithm:**

- Perform DFS while keeping track of visited nodes and their parent.
- If a visited node is encountered that is not the parent, a cycle exists.
- Check all nodes to ensure the entire graph is processed.

**Time Complexity:** O(V + E)

---

## Problem 5: Graph Coloring (Greedy Algorithm)

### **Algorithm:**

- Assign colors to nodes ensuring that no two adjacent nodes have the same color.
- Use a greedy approach, picking the smallest available color.
- Use at most 3 colors.

**Time Complexity:** O(V + E)

---

## Running the Code

### **Prerequisites**

- Python 3
- Install dependencies (if any) using:
  ```sh
  pip install heapq collections
  ```

### **Steps to Run**

1. Clone the repository:

   ```sh
   git clone https://github.com/Problems-on-Graphs.git
   cd graph-algorithms
   ```

2. Run each algorithm:

   ```sh
   python dijkstra.py   # Shortest path
   python bfs.py        # BFS traversal
   python dfs.py        # DFS traversal
   python cycle_detect.py  # Cycle detection
   python graph_coloring.py # Graph coloring
   ```

