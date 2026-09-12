import random

from CSC370_8PuzzleBoard import PuzzleBoard, random_start
from CSC370_A_star import a_star
from CSC370_BranchingFactor import effective_b_factor

def h1(board):
    return board.misplaced_tiles()

def h2(board):
    return board.manhattan_distance()

DEPTHS = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
INSTANCES_PER_DEPTH = 100

