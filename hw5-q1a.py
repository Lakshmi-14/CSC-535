def dijkstra(src):
    lengths = {ele: None for ele in 'SABCDt'}
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

        values = [vertex for vertex in lengths.items() if vertex[1]]
        src, lengths[src] = sorted(values, key=lambda x: x[1])[0]


if __name__ == "__main__":

    weights = {'S': {'A': 4, 'B': 6},
               'A': {'D': 1, 'C': 2},
               'B': {'A': 2, 'D': 2},
               'C': {'D': 1, 't': 3},
               'D': {'t': 7}}

    init_source = "S"
    sol_array = dijkstra(init_source)

    print("\n\nsource ----> destination : shortest Distance")
    print("----"*10)
    for (node, length) in sol_array.items():
        print(" "*4, init_source, "---->", node.ljust(5), ":", length)

    print("\nPROGRAM EXECUTED SUCCESSFULLY !!!")
    input("\nPress Enter to close")
