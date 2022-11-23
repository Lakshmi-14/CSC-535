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

    vertices = ['A', 'B', 'C', 'D', 'E']

    sources = ['A', 'A', 'B', 'B', 'E', 'E', 'E', 'D', 'D', 'C']
    destinations = ['B', 'E', 'E', 'C', 'B', 'C', 'D', 'A', 'C', 'D']
    weights = [10, 5, 3, 1, 3, 9, 2, 7, 6, 4]

    network = []

    for i in range(len(sources)):
        network.append([sources[i], destinations[i], weights[i]])

    init_source = 'A'
    sol_array = bellManFord(init_source)

    print("\n\nsource ----> destination : shortest Distance")
    print("----"*10)
    for (ele, length) in sol_array.items():
        print(" "*4, init_source, "---->", ele.ljust(5), ":", length)
    input("\n\n\n Press Enter to exit")
