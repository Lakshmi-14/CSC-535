#!/usr/bin/env python3
'''
author : Ashok Ajmeera
encoding UTF-8
OS : windows 10 
'''


def dijkstra(src):
    lengths = {ele: None for ele in 'ABCDE'}
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

    weights = {'A': {'B': 10, 'E': 5},
               'B': {'E': 3, 'C': 1},
               'E': {'B': 3, 'C': 9, 'D': 2},
               'D': {'A': 7, 'C': 6},
               'C': {'D': 4}}

    init_source = "A"
    sol_array = dijkstra(init_source)

    print("\n\nsource ----> destination : shortest Distance")
    print("----"*10)
    for (node, length) in sol_array.items():
        print(" "*4, init_source, "---->", node.ljust(5), ":", length)

    print("\nPROGRAM EXECUTED SUCCESSFULLY !!!")
    input("\nPress Enter to close")
