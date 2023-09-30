from collections import defaultdict

class BreadthFirstSearch:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        for start, end in edges:
            self.graph[start].append(end)

    def find_shortest_path(self, start_node, end_node):
        visited = set()
        queue = [[start_node]]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end_node:
                return path

            if node not in visited:
                for neighbor in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                visited.add(node)

        return []

    def show_path(self, start_node, end_node):
        path = self.find_shortest_path(start_node, end_node)
        if path:
            print("Shortest Path derived by Breadth-First Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

# Define the edges for BFS
edges_bfs = [('S', 'B'), ('S', 'A'), ('A', 'B'), ('B', 'A'), ('A', 'D'), ('D', 'F'), ('B', 'C'), ('C', 'E'), ('F', 'G')]

# Create a BreadthFirstSearch object and find the path
bfs = BreadthFirstSearch(edges_bfs)
bfs.show_path('S', 'G')
