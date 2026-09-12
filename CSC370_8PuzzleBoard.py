import random

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

class PuzzleBoard:
    ## Constructor that stores the tiles of a specific board as a tuple
    def __init__(self, tiles):
        self.tiles = tuple(tiles)
    
    ## Method that returns the board as a 3x3 grid text
    def __str__(self):
        return "\n".join(
            " ".join(str(t) for t in self.tiles[i:i+3])
            for i in range(0,9,3)
        )
    
    ## Method that tests if the goal sequence was met
    def goal_reached(self):
        return self.tiles == GOAL
    
    def neighbors(self):

        boards = []
        blank_spot = self.tiles.index(0)

        ## Find grid spot of blank
        row, col = blank_spot // 3, blank_spot % 3

        moves = []
        ## Blank spot can move up to take position that is 3 before
        if row > 0: 
            moves.append(blank_spot - 3)
        ## Blank spot can move down to take position that is 3 after
        if row < 2:
            moves.append(blank_spot + 3)
        ## Blank spot can move left to take position that is 1 before
        if col > 0: 
            moves.append(blank_spot - 1)
        ## Blank spot can move right to take position that is 1 after
        if col < 2: 
            moves.append(blank_spot + 1)
        
        ## Make a copy of current board, blank spot and neighbor spot 
        # swap places, put back into PuzzleBoard class

        for m in moves:

            copy = list(self.tiles)
            move_tile = copy[m]
            copy[m] = 0
            copy[blank_spot] = move_tile
    

            boards.append(PuzzleBoard(copy))
            
        return boards
    

    ## Hueristic 1: number of tiles besides the blank that are NOT
    ## in their goal state
    def heuristic_1(self):
        count = 0
        for i in range(9):
            tile = self.tiles[i]
            if tile != 0 and tile != GOAL[i]:
                count += 1
        return count
    
    ## Heuristic 2: the amount of rows and columns that each tile is 
    ## away from its goal state
    def heuristic_2(self):
        total = 0
        for i in range(9):
            tile = self.tiles[i]
            if tile == 0:
                continue
            row, col = i // 3, i % 3
            goal_index = GOAL.index(tile)
            goal_row, goal_col = goal_index // 3, goal_index % 3
            total += abs(row - goal_row) + abs(col - goal_col)
        return total

## Start with goal puzzle then jumble taking random.choice on 
# the function neighbors on the array board
def random_start(num_moves=100):
    board = PuzzleBoard(GOAL)
    for i in range(num_moves):
         board = random.choice(board.neighbors())
    return board
    

        
        