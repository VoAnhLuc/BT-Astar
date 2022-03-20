class Graph:
    def __init__(self, adjacents, h_list):
        self.adjacents = adjacents
        self.h = h_list

    def get_adjacents(self, u):  # tao luat
        return self.adjacents[u]

    def get_h(self, u):     # ham heuristic
        return self.h[u]

    def a_star(self, start, end):  # ham tim duong di
        open_set = set(start)
        closed_set = set()
        g = {}
        g[start] = 0

        while len(open_set) > 0:
            u = None
            for v in open_set:
                if u == None or g[u] > g[v] + self.get_h(v):
                    u = v

            if u == end:
                return g[u]

            adjacents = self.get_adjacents(u)
            for v, w in adjacents:
                if v not in open_set and v not in closed_set:
                    g[v] = g[u] + w
                    open_set.add(v)
                elif v in open_set:
                    g[v] = min(g[v], g[u] + w)
                elif v in closed_set and g[v] > g[u] + w:
                    g[v] = g[u] + w
                    closed_set.remove(v)
                    open_set.add(v)

            open_set.remove(u)
            closed_set.add(u)
        return None

def main():
    adjacents = {
        'A': [('B', 6), ('D', 4), ('G', 18)],
        'B': [('A', 6), ('H', 6), ('C', 5), ('E', 4)],
        'C': [('B', 5), ('D', 15), ('F', 8)],
        'D': [('A', 4), ('C', 15)],
        'E': [('B', 4), ('F', 7), ('G', 5)],
        'F': [('C', 8), ('G', 3), ('E', 7)],
        'G': [('A', 18), ('F', 3), ('E', 5), ('H', 6)],
        'H': [('B', 6), ('G', 6)]
        }
    h_list = {
        'A': 18,
        'B': 9,
        'C': 11,
        'D': 23,
        'E': 5,
        'F': 3,
        'G': 0,
        'H': 6 }
    graph = Graph(adjacents, h_list)

    print(graph.a_star('A', 'G'))
    
if __name__ == "__main__":
    main()