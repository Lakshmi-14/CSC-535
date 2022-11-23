#!/usr/bin/env python3
'''
author : Ashok Ajmeera
encoding UTF-8
OS : windows 10 
'''


def dijkstra(src):
    lengths = {ele: None for ele in 'ABCDEFGHJK'}
    lengths[src] = 0

    traversed = dict()

    while (1):
        for (dest, weight) in weights.get(src, {}).items():
            if dest not in lengths:
                continue

            if (lengths[dest] is None) or (lengths[dest] > lengths[src] + weight):
                lengths[dest] = lengths[src] + weight

        traversed[src] = lengths[src]
        del lengths[src]
        if len(lengths) == 0:
            return traversed

        values = [node for node in lengths.items() if node[1]]
        src, lengths[src] = sorted(values, key=lambda x: x[1])[0]


if __name__ == "__main__":

    weights = {'A': {'B': 1, 'E': 1},
               'B': {'A': 1, 'C': 1},
               'E': {'A': 1, 'D': 5, 'G': 1},
               'C': {'B': 1, 'G': 1, 'F': 3, 'J': 4},
               'G': {'C': 1, 'E': 1, 'H': 1},
               'F': {'C': 3, 'K': 1},
               'J': {'C': 4, 'D': 2},
               'K': {'F': 1, 'D': 1},
               'D': {'J': 2, 'K': 1, 'E': 5, 'H': 1},
               'H': {'D': 1, 'G': 1}}

    init_source = "A"
    sol_array = dijkstra(init_source)
    print("\n\nsource ----> destination : shortest Distance")
    print("----"*10)
    for (node, length) in sol_array.items():
        print(" "*4, init_source, "---->", node.ljust(5), ":", length)

    print("\nPROGRAM EXECUTED SUCCESSFULLY !!!")
    input("\nPress Enter to close")
