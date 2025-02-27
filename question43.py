from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0  # Discovery time counter

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, discovery_time, low, parent, bridges):
        visited[u] = True
        discovery_time[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:  # If `v` is not visited, do DFS
                parent[v] = u
                self.bridge_util(v, visited, discovery_time, low, parent, bridges)

                # Update the low value of `u`
                low[u] = min(low[u], low[v])

                # Condition for a bridge
                if low[v] > discovery_time[u]:
                    bridges.append((u, v))
            
            elif v != parent[u]:  # If `v` is visited and not parent of `u`, it's a back edge
                low[u] = min(low[u], discovery_time[v])

    def find_bridges(self):
        visited = [False] * self.V
        discovery_time = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        bridges = []

        for i in range(self.V):
            if not visited[i]:  
                self.bridge_util(i, visited, discovery_time, low, parent, bridges)

        return bridges

# Example Usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Bridges in the graph:", g.find_bridges())
