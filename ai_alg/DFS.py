class DepthFirstSearch:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.found_path = False
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)

    def depth_first_search(self, start_node, end_node, current_path=[]):
        if self.found_path:
            return []
        current_path.append(start_node)
        if start_node == end_node:
            self.found_path = True
            return [current_path]

        if start_node not in self.graph_dict:
            return []

        sorted_neighbors = sorted(self.graph_dict[start_node])
        paths = []

        for neighbor in sorted_neighbors:
            if neighbor not in current_path:
                new_paths = self.depth_first_search(neighbor, end_node, current_path.copy())
                paths.extend(new_paths)

        return paths

    def show_path_dfs(self, start_node, end_node):
        paths = self.depth_first_search(start_node, end_node)
        if paths:
            print("Path derived by Depth First Search Algorithm:")
            for path in paths:
                print(" -> ".join(path))
        else:
            print("No valid path found.")

edges = [('S', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')]
dfs = DepthFirstSearch(edges)
dfs.show_path_dfs('S', 'G')
