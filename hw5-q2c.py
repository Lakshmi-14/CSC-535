#!/usr/bin/env python3
'''
author : Ashok Ajmeera
encoding UTF-8
OS : windows 10 
'''


def bellManFord(src):
    lengths = {ele: float("inf") for ele in vertices}
    lengths[src] = 0

    for i in range(len(vertices) - 1):
        for src, dest, weight in network:
            if (lengths[src] != float("Inf")) and (lengths[src] + weight < lengths[dest]):
                lengths[dest] = lengths[src] + weight

    for (src, dest, weight) in network:
        if (lengths[src] != float("Inf")) and (lengths[src] + weight < lengths[dest]):
            print("Network contains Negative Cycle")
            return None

    return lengths


if __name__ == "__main__":

    vertices = ['A', 'B', 'E', 'C', 'G', 'F', 'J', 'K', 'D', 'H']

    sources = ['A', 'A', 'B', 'C', 'C', 'C', 'F', 'J', 'D', 'D', 'D', 'E', 'G']
    destinations = ['B', 'E', 'C', 'G', 'F',
                    'J', 'K', 'D', 'K', 'E', 'H', 'G', 'H']
    weights = [1, 1, 1, 1, 3, 4, 1, 2, 1, 5, 1, 1, 1]

    network = []

    for i in range(len(sources)):
        network.append([sources[i], destinations[i], weights[i]])
        network.append([destinations[i], sources[i], weights[i]])

    init_source = 'A'
    sol_array = bellManFord(init_source)

    print("\n\nsource ----> destination : shortest Distance")
    print("----"*10)
    for (ele, length) in sol_array.items():
        print(" "*4, init_source, "---->", ele.ljust(5), ":", length)
    input("\n\n\n Press Enter to exit")
