# CSC370_HW1 — 8 Puzzle with A* Search

Coursework for CSC 370 (Machine Reasoning). This project solves the 8 puzzle
with A* search under three different heuristics and compares how efficiently
each heuristic guides the search, measured by the average number of nodes
generated and the resulting effective branching factor.

## Contributors

- Kara Niewoehner (`karaniewoehner`)
- Tania Umurerwa Kalisa (`taumurerwakalisa`)

## Files

**CSC370_8PuzzleBoard.py**
Defines the 8 puzzle. The `PuzzleBoard` class stores a board as a tuple of nine
tiles, where 0 is the blank. It checks whether the goal has been reached and
generates a board's neighbors by sliding the blank up, down, left, or right. It
also defines the three heuristics: `heuristic_1` counts the misplaced tiles,
`heuristic_2` computes Manhattan distance (how many rows and columns each tile
sits from its goal position), and `heuristic_3` applies a relaxed rule in which
any tile may swap with the blank. The `random_start` function builds a solvable
board by shuffling the goal with random moves.

**CSC370_A_star.py**
Implements the A* search. It takes a starting board and a heuristic function,
keeps the frontier in a priority queue ordered by f = g + h, and tests for the
goal when a node is popped. Boards already in the visited set are skipped. The
function returns the solution depth and the number of nodes generated.

**CSC370_BranchingFactor.py**
Computes the effective branching factor. `tree_size` adds up the nodes in a full
tree of a given branching factor and depth. `effective_b_factor` searches upward
for the branching factor whose tree size matches the node count that A* produced.

**CSC370_Experiment.py**
Runs the full experiment. It generates random solvable boards, groups them by
solution depth (100 boards for each depth from 2 to 24), runs A* on each board
under all three heuristics, averages the nodes generated, converts those
averages into effective branching factors, and prints the comparison table.

## How to run

```bash
python3 CSC370_Experiment.py
```

This prints a table with one row per solution depth, showing the average nodes
generated and the effective branching factor for each of the three heuristics.

## Notes

The experiment uses randomly generated boards, so exact node counts vary
slightly between runs while the overall trends stay consistent.
