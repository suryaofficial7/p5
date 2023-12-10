# Step 1: Import the 'deque' class from the 'collections' module
from collections import deque

# Step 2: Define the water_jug_bfs function
def water_jug_bfs(capacity_a, capacity_b, target):
    # Step 3: Initialize the visited set and the queue with the initial state (0, 0)
    visited = set()
    queue = deque([(0, 0)])

    # Step 4: Perform BFS using a while loop until the queue is empty
    while queue:
        # Step 5: Dequeue the current state (a, b)
        current_state = queue.popleft()
        a, b = current_state

        # Step 6: Check if the current state has been visited
        if current_state in visited:
            continue

        # Step 7: Mark the current state as visited
        visited.add(current_state)

        # Step 8: Check if the target amount has been reached in either jug
        if a == target or b == target:
            print("Target amount reached:", current_state)
            return

        # Step 9: Enqueue possible pouring operations
        queue.append((0, b))
        queue.append((a, 0))
        queue.append((capacity_a, b))
        queue.append((a, capacity_b))
        queue.append((a - min(a, capacity_b - b), b + min(a, capacity_b - b)))
        queue.append((a + min(b, capacity_a - a), b - min(b, capacity_a - a)))

    # Step 10: Print a message if the target amount is not reachable
    print("Target amount not reachable with the given jug capacities.")

# Example usage:
# Step 11: Set jug capacities and target amount
jug_capacity_a = 4
jug_capacity_b = 3
target_amount = 2

# Step 12: Print a message indicating the problem parameters
print(f"Solving Water Jug problem for capacities ({jug_capacity_a}, {jug_capacity_b}) to measure {target_amount} units of water.")

# Step 13: Call the water_jug_bfs function with the specified parameters
water_jug_bfs(jug_capacity_a, jug_capacity_b, target_amount)
