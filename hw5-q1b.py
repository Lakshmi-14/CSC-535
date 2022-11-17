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
        print("Shortest-path tree using Dijkstra algorithm on Figure-2")
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

    # Adding vertices to the Network
    net.add_vertex("A")
    net.add_vertex("B")
    net.add_vertex("C")
    net.add_vertex("D")
    net.add_vertex("E")

    #Defining Connections in the network with weights
    net.add_connection("A", "B", 10)
    net.add_connection("A", "E", 5)
    net.add_connection("B", "E", 3)
    net.add_connection("B", "C", 1)
    net.add_connection("E", "B", 3)
    net.add_connection("E", "C", 9)
    net.add_connection("E", "D", 2)
    net.add_connection("D", "A", 7)
    net.add_connection("D", "C", 6)
    net.add_connection("C", "D", 4)

    # Performing the Algorithm 
    net.dijkstra("A")
    
    input("\n\n\n Press Enter to exit...")
