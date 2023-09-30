import heapq

class AStar:
    def __init__(self, edges, heuristic_values):
        self.edges = edges
        self.graph = {}
        self.heuristics = heuristic_values
        self.path_found = False

        for start, end, cost in edges:
            if start not in self.graph:
                self.graph[start] = []
            self.graph[start].append((end, cost))

    def find_shortest_path(self, start_node, end_node):
        open_list = [(0, start_node, [])]  # (Total cost, Current node, Path)
        closed_set = set()

        while open_list:
            total_cost, current_node, path = heapq.heappop(open_list)

            if current_node == end_node:
                path.append(current_node)
                return path

            if current_node in closed_set:
                continue

            closed_set.add(current_node)

            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor not in closed_set:
                    heuristic_cost = self.heuristics[neighbor]
                    new_total_cost = total_cost + cost + heuristic_cost
                    new_path = path + [current_node]
                    heapq.heappush(open_list, (new_total_cost, neighbor, new_path))

        return []

    def show_path(self, start_node, end_node):
        path = self.find_shortest_path(start_node, end_node)
        if path:
            print("Shortest Path derived by A* Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

if __name__ == "__main__":
    # Define the edges and heuristic values
    edges = [('S', 'A', 4), ('S', 'B', 2), ('A', 'B', 2), ('B', 'A', 1),
             ('A', 'D', 1), ('D', 'F', 2), ('B', 'C', 3), ('C', 'E', 1), ('F', 'G', 2)]
    heuristic_values = {'S': 7, 'A': 2, 'B': 4, 'C': 6, 'D': 5, 'E': 1, 'F': 2, 'G': 0}

    # Create an AStar object and find the path
    a_star = AStar(edges, heuristic_values)
    a_star.show_path('S', 'G')
