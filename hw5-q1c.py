from collections import defaultdict

# Define the graph Network


class Network:
    def __init__(self):
        self.nodes = list()
        self.weights = defaultdict(dict)

    # Add a node to the graph
    def add_vertex(self, ver_val):
        self.nodes.append(ver_val)

    # Create Bi-Directional connection/edge between two nodes in graph with given weight
    def add_connection(self, source, dest, weight):
        self.weights[source][dest] = weight
        self.weights[dest][source] = weight

    # Display the resultant shortest paths rooted at "source"
    def disp_short_weights(self, source):
        print("Distance of node from Source ")
        for (node, weight) in self.visited.items():
            print(source, "->", node.ljust(3), ":", weight)

    # Implementation of Dijkstra algorithm
    def dijkstra(self,  source):

        # Store the source/root
        # So that it can be used later while displaying the result to screen
        net_source = source
        dist = {node: None for node in self.nodes}
        self.visited = dict()
        dist[source] = 0

        # Infinite loop
        # Breaks when dist dictionary becomes empty
        while (True):
            for (dest, weight) in self.weights[source].items():
                if dest not in dist:
                    continue

                if (dist[dest] is None) or (dist[dest] > dist[source] + weight):
                    dist[dest] = dist[source] + weight

            self.visited[source] = dist[source]

            # delete the dist[source] element as we found its shortest path
            del dist[source]
            if not dist:
                break

            candidates = [node for node in dist.items() if node[1]]
            source, dist[source] = sorted(candidates, key=lambda x: x[1])[0]

        self.disp_short_weights(net_source)


if __name__ == "__main__":
    net = Network()

    # Adding vertices to the Graph
    for let in "ABCDEFGHJK":
        net.add_vertex(let)

    # Defining the edges and weights in the graph
    net.add_connection("A", "B", 1)
    net.add_connection("A", "E", 1)
    net.add_connection("B", "C", 1)
    net.add_connection("C", "G", 1)
    net.add_connection("C", "F", 3)
    net.add_connection("C", "J", 4)
    net.add_connection("F", "K", 1)
    net.add_connection("J", "D", 2)
    net.add_connection("D", "K", 1)
    net.add_connection("D", "E", 5)
    net.add_connection("D", "H", 1)
    net.add_connection("E", "G", 1)
    net.add_connection("G", "H", 1)

    # Performing Dijkstra Algorithm to find shortest-path tree
    net.dijkstra("A")
