# Effective branching factor
## Calculate a full tree of depth d
def tree_size(b, d):
    total = 0
    for power in range(d + 1):
        total += b ** power
    return total

## Compare tree size against our target value of N + 1 until we reach it,
## then return our effective branching factor
def effective_b_factor(N, d):
    # base case
    if d == 0:
        return 0.0
    target = N + 1
    b = 1.0
    step = 0.01
    while tree_size(b, d) < target:
        b += step
        return b