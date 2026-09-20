

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

        #m is a certain move and the if statements look at one move at a time. 
        
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
        
        ## Make a copy of current board and blank spot and neighbor spot 
        # swap places, put back into PuzzleBoard class

        for m in moves:

            copy = list(self.tiles)
            move_tile = copy[m]
            copy[m] = 0
            copy[blank_spot] = move_tile

            boards.append(PuzzleBoard(copy))
            
        return boards
        

    ## Heuristic 2: the amount of rows and columns that each tile is 
    ## away from its goal state 
    def heuristic_2(self):
        count = 0
        for i in range(9):
            tile = self.tiles[i]
            if tile == 0:
                continue
            row, col = i // 3, i % 3
            goal_index = GOAL.index(tile)
            goal_row, goal_col = goal_index // 3, goal_index % 3
            count += abs(row - goal_row) + abs(col - goal_col)
        return count

    ## Heuristic 3: any tile anywhere may swap positions with the blank
    def heuristic_3(self):
        tiles = list(self.tiles)
        count = 0

        while tiles != list(GOAL):
            blank = tiles.index(0)
            ## Blank tile in goal state, but not whole board
            if tiles[blank] == GOAL[blank]:
                for i in range(9):
                    if tiles[i] != GOAL[i]:
                        break
                tiles[blank], tiles[i] = tiles[i], tiles[blank]
            ## Put correct tile where blank is
            else:
                swap_spot = GOAL[blank]
                i = tiles.index(swap_spot)
                tiles[blank], tiles[i] = tiles[i], tiles[blank]

            count += 1
        return count

## Start with goal puzzle then jumble taking random.choice on 
# the function neighbors on the array board
def random_start(num_moves = 100):
    board = PuzzleBoard(GOAL)
    for i in range(num_moves):
        board = random.choice(board.neighbors())
    return board



