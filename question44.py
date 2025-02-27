from collections import deque

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n  # -1 means uncolored

    for start in range(n):  # Check all components
        if color[start] == -1:  
            queue = deque([start])
            color[start] = 0  # Assign first color

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If uncolored, assign opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # Conflict detected
                        return False

    return True

# Example Usage
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}  # This graph is Bipartite

print("Graph is Bipartite" if is_bipartite(graph) else "Graph is NOT Bipartite")
