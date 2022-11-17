#!/usr/bin/env python3
'''
OS : Windows 10
author : Kalagiri Narendhar
encoding : UTF-8
'''

from collections import defaultdict

# Defining Network


class Network:
    def __init__(self):
        self.nodes = list()
        self.weights = defaultdict(dict)

    # Add a node to the network
    def add_vertex(self, ver_val):
        self.nodes.append(ver_val)

    # Add directed edge/connection between nodes with given weight
    def add_connection(self, source, dest, weight):
        self.weights[source][dest] = weight

    # Display Result
    def disp_short_weights(self, source):
        print("Shortest-path tree using Dijkstra algorithm on Figure-1")
        for (node, weight) in self.visited.items():
            print(source, "->", node.ljust(3), ":", weight)

    # Implementation of Dijkstra Algorithm
    def dijkstra(self,  source):
        net_source = source
        dist = {node: None for node in self.nodes}

        self.visited = dict()

        dist[source] = 0

        while (True):
            for (dest, weight) in self.weights[source].items():
                if dest not in dist:
                    continue

                if (dist[dest] is None) or (dist[dest] > dist[source] + weight):
                    dist[dest] = dist[source] + weight

            self.visited[source] = dist[source]
            del dist[source]
            if not dist:
                break

            candidates = [node for node in dist.items() if node[1]]
            source, dist[source] = sorted(candidates, key=lambda x: x[1])[0]

        self.disp_short_weights(net_source)


if __name__ == "__main__":
    # initializing a Network
    net = Network()

    # Adding nodes to the network
    net.add_vertex("S")
    net.add_vertex("A")
    net.add_vertex("B")
    net.add_vertex("C")
    net.add_vertex("D")
    net.add_vertex("t")

    # Defining edges and weights in the network.
    net.add_connection("S", "A", 4)
    net.add_connection("S", "B", 6)
    net.add_connection("A", "D", 1)
    net.add_connection("A", "C", 2)
    net.add_connection("B", "A", 2)
    net.add_connection("B", "D", 2)
    net.add_connection("C", "D", 1)
    net.add_connection("C", "t", 3)
    net.add_connection("D", "t", 7)

    # Performing Dijkstra algorithm on the network
    net.dijkstra("S")
    input("\n\n\n\n Press Enter to exit the Program....")
