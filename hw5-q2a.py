class Network:
    def __init__(self, node_count):
        self.n_count = node_count
        self.network = list()
        self.nodes = list()

    def add_vertex(self, ver_val):
        self.nodes.append(ver_val)

    def add_connection(self, source, dest, weight):
        self.network.append([source, dest, weight])

    def disp_short_weights(self, source, network_map):
        print("Shortest-path tree using Bellman-Ford algorithm")
        for (node, weight) in network_map.items():
            print(source, "->", node.ljust(3), ":", weight)

    def bellManFord(self, source):
        net_source = source
        dist = {node: float("inf") for node in self.nodes}
        dist[source] = 0

        for _ in range(self.n_count - 1):
            for source, dest, weight in self.network:
                if (dist[source] != float("Inf")) and (dist[source] + weight < dist[dest]):
                    dist[dest] = dist[source] + weight

        for (source, dest, weight) in self.network:
            if (dist[source] != float("Inf")) and (dist[source] + weight < dist[dest]):
                print("Network contains Negative Cycle")
                return None

        self.disp_short_weights(net_source, dist)


if __name__ == "__main__":
    net = Network(6)
    net.add_vertex("S")
    net.add_vertex("A")
    net.add_vertex("B")
    net.add_vertex("C")
    net.add_vertex("D")
    net.add_vertex("t")

    net.add_connection("S", "A", 4)
    net.add_connection("S", "B", 6)
    net.add_connection("A", "D", 1)
    net.add_connection("A", "C", 2)
    net.add_connection("B", "A", 2)
    net.add_connection("B", "D", 2)
    net.add_connection("C", "D", 1)
    net.add_connection("C", "t", 3)
    net.add_connection("D", "t", 7)

    net.bellManFord("S")


'''
Distance of node from Source 
S -> S   : 0
S -> A   : 4
S -> B   : 6
S -> C   : 6
S -> D   : 5
S -> t   : 9
'''
