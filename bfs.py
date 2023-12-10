# Step 1: Import the 'deque' class from the 'collections' module
from collections import deque

# Step 2: Define the BFS function
def bfs(graph, start):
    # Step 3: Initialize the visited set and the queue with the start node
    visited = set()
    queue = deque([start])

    # Step 4: Perform BFS using a while loop until the queue is empty
    while queue:
        # Step 5: Dequeue a node from the front of the queue
        node = queue.popleft()

        # Step 6: Check if the node has not been visited
        if node not in visited:
            # Step 7: Print the node, mark it as visited, and enqueue its unvisited neighbors
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Example usage:
# Step 8: Define an adjacency list for a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Step 9: Choose a starting node (e.g., 'A')
start_node = 'A'

# Step 10: Print a message indicating the starting node for BFS
print("BFS starting from node", start_node)

# Step 11: Call the BFS function with the graph and starting node
bfs(graph, start_node)
