def total_nodes_for_b(b, depth):
    total = 0
    for i in range(depth + 1):
        total += b ** i
    return total


def effective_branching_factor(nodes, depth):
    N = nodes + 1

    low = 1.0
    high = 10.0

    for step in range(50):
        mid = (low + high) / 2
        guess_total = total_nodes_for_b(mid, depth)

        if guess_total < N:
            low = mid
        else:
            high = mid

    return (low + high) / 2