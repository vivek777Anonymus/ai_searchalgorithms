class PathOracle:
    def __init__(self, edges):
        self.graph_dict = {}
        for start, end, cost in edges:
            self.graph_dict.setdefault(start, []).append((end, cost))

    def find_all_paths(self, start, end, current_path=[], cost=0):
        current_path = current_path + [start]
        if start == end:
            return [(cost, current_path)]

        if start not in self.graph_dict:
            return []

        paths = []
        for neighbor, edge_cost in self.graph_dict[start]:
            if neighbor not in current_path:
                new_paths = self.find_all_paths(neighbor, end, current_path.copy(), cost + edge_cost)
                paths.extend(new_paths)

        return paths

    def show_ranked_paths(self, start, end, show_oracle_value=False):
        paths = self.find_all_paths(start, end)

        if not paths:
            print("No valid path found.")
            return

        paths.sort(key=lambda x: x[0])

        print("Paths ranked from best to worst based on cost:")
        oracle = paths[0]
        print("Oracle:", oracle[0] if show_oracle_value else "Hidden")  # Show oracle value on request

# Define the edges with updated values
edges_with_cost = [('S', 'B', 4), ('S', 'A', 3), ('A', 'B', 2), ('B', 'A', 3),
                   ('A', 'D', 5), ('D', 'F', 4), ('B', 'C', 2), ('C', 'E', 4), ('F', 'G', 2)]

path_oracle = PathOracle(edges_with_cost)
path_oracle.show_ranked_paths('S', 'G', show_oracle_value=True)  
