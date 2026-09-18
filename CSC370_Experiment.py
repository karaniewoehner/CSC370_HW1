import random
from collections import deque

from CSC370_8PuzzleBoard import PuzzleBoard, random_start, GOAL
from CSC370_A_star import a_star
from CSC370_BranchingFactor import effective_b_factor

## Constants that can be changed
DEPTHS = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
INSTANCES_PER_DEPTH = 100


def h1(board):
    return board.heuristic_1()

def h2(board):
    return board.heuristic_2()

def h3(board):
    return board.heuristic_3()

## Sort boards based on solution depth so that each DEPTHS has INSTANCES_PER_DEPTH
## amount of solution lengths
def sort_boards():
    ## one bin per depth
    buckets = {}
    for d in DEPTHS:
        buckets[d] = []
    
    count = 0
    while count < 50000:
        count += 1
        ## Run A* on a random solveable board
        board = random_start(100)
        depth = a_star(board, h2)[0]
        ## Add solved board to its solution depth if the solution depth is what we are
        ## looking for and the depth's bucket is not yet full
        if depth in buckets and len(buckets[depth]) < INSTANCES_PER_DEPTH:
            buckets[depth].append(board)
            print("filled depth", depth, "->", len(buckets[depth]))
        ## Check if buckets are full after adding a board's solution depth
        full = True
        for d in DEPTHS:
            if len(buckets[d]) < INSTANCES_PER_DEPTH:
                full = False
        if full:
            break
    
    print("Collection done. Now computing the table...")
    return buckets

def results():

    buckets = sort_boards()

    print("d | A*(h1) Nodes | A*(h2) Nodes | A*(h3) Nodes | A*(h1) b* | A*(h2) b* | A*(h3) b*")
    ## For the boards in each depth group
    for d in DEPTHS:
        boards = buckets[d]

        if len(boards) == 0:
            continue

        h1_total = 0
        h2_total = 0
        h3_total = 0
        ## Find nodes of each board per heuristic
        for b in boards:
            h1_total = h1_total + a_star(b ,h1)[1]
            h2_total = h2_total + a_star(b ,h2)[1]
            h3_total = h3_total + a_star(b ,h3)[1]
        ## Find average number of nodes per heuristic 
        h1_nodes = h1_total / len(boards)
        h2_nodes = h2_total / len(boards)
        h3_nodes = h3_total / len(boards)
        ## Calculate effective branchign factor with average nodes per heuristic
        h1_b = effective_b_factor(round(h1_nodes), d)
        h2_b = effective_b_factor(round(h2_nodes), d)
        h3_b = effective_b_factor(round(h3_nodes), d)

        print(d, "|", round(h1_nodes), "|", round(h2_nodes), "|", round(h3_nodes),
              "|", round(h1_b, 2), "|", round(h2_b, 2), "|", round(h3_b, 2))
results()