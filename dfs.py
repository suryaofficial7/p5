# Step 1: Define the DFS function
def dfs(graph, start, visited=None):
    # Step 2: Initialize the visited set if it's not provided
    if visited is None:
        visited = set()

    # Step 3: Mark the current node as visited and print it
    visited.add(start)
    print(start, end=' ')

    # Step 4: Recursively visit all unvisited neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
# Step 5: Define an adjacency list for a graph
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

# Step 6: Choose a starting node (e.g., 'A')
start_node = 'A'

# Step 7: Print a message indicating the starting node for DFS
print("DFS starting from node", start_node)

# Step 8: Call the DFS function with the graph and starting node
dfs(graph, start_node)
