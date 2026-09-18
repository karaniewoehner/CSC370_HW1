"""
from hw1_puzzle_state.py import PuzzleState, GOAL_STATE
from a_star import a_star


#Create a random puzzle generator, which returns a board we'll search and solve: 
import random

def generate_puzzle(num_moves = 120):
    state = PuzzleState(GOAL_STATE)
    for i in range(num_moves):
        neighbors = state.check_neighbors()
        state = random.choice(neighbors)

    scrambled_board = state.board

    return scrambled_board




#Experiment:
target_depths = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

results = {}

for d in target_depths:
    results[d] = []

#Loop through the boards n times 

"""


import random
from hw1_puzzle_state import PuzzleState, GOAL_STATE
from a_star import a_star
from branching_factor import effective_branching_factor



def generate_problem(num_moves = 100):
    state = PuzzleState(GOAL_STATE)
    for _ in range(num_moves):
        neighbors = state.check_neighbors()
        state = random.choice(neighbors)

    scrambled_board = state.board

    goal_node, nodes = a_star(scrambled_board, PuzzleState.h2)
    true_depth = goal_node.g

    return scrambled_board, true_depth


# set up empty buckets, one per depth we care about
target_depths = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

results = {}
for d in target_depths:
    results[d] = []

# generate problems and run all 4 heuristics on each
num_trials = 1200

for trial in range(num_trials):
    board, depth = generate_problem(100)

    if depth not in target_depths:
        continue


    node1, nodes1 = a_star(board, PuzzleState.h1)
    node2, nodes2 = a_star(board, PuzzleState.h2)
    node3, nodes3 = a_star(board, PuzzleState.h3)

    one_result = [nodes1, nodes2, nodes3]
    results[depth].append(one_result)


# average each depth bucket and print
print("depth   count        h1       h2       h3")

for d in target_depths:
    bucket = results[d]
    count = len(bucket)

    if count == 0:
        print(d, "     0     (no data)")
        continue

    total_h1 = 0
    total_h2 = 0
    total_h3 = 0

    for result in bucket:
        total_h1 += result[0]
        total_h2 += result[1]
        total_h3 += result[2]

    avg_h1 = total_h1 / count
    avg_h2 = total_h2 / count
    avg_h3 = total_h3 / count

    print(d, "   ", count, "  ", avg_h1, avg_h2, avg_h3)