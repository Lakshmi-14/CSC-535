
# Defining the Network

class Network:
    def __init__(self, node_count):
        self.n_count = node_count
        self.network = list()
        self.nodes = list()

    # Adding node/vertex to the Network
    def add_vertex(self, ver_val):
        self.nodes.append(ver_val)

    # Adding connections/edges in the network with weights
    def add_connection(self, source, dest, weight):
        self.network.append([source, dest, weight])
        self.network.append([dest, source, weight])

    # Display result
    def disp_short_weights(self, source, network_map):
        print("Distance of node from Source using Bellman-Ford on Figure-3 ")
        for (node, weight) in network_map.items():
            print(source, "->", node.ljust(3), ":", weight)

    # Implementation of Bellman-Ford Algorithm
    def bellManFord(self, source):
        net_source = source
        dist = {node: float("inf") for node in self.nodes}
        dist[source] = 0

        for _ in range(self.n_count - 1):
            for source, dest, weight in self.network:
                if (dist[source] != float("Inf")) and (dist[source] + weight < dist[dest]):
                    dist[dest] = dist[source] + weight

        # Detection of Negative cycle
        for (source, dest, weight) in self.network:
            if (dist[source] != float("Inf")) and (dist[source] + weight < dist[dest]):
                print("Network contains Negative Cycle")
                return None

        self.disp_short_weights(net_source, dist)


if __name__ == "__main__":

    # Initializing a Network
    net = Network(10)

    # Adding edges to the Network
    for let in "ABCDEFGHJK":
        net.add_vertex(let)

    # Adding Connectins/edges to the Network with Weights
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

    # Performing Bellman-Ford Algorithm
    net.bellManFord("A")
