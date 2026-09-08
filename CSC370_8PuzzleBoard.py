

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
        
        ## Make a copy of current board and blank spot and neighbor spot 
        # swap places, put back into PuzzleBoard class

        for m in moves:
            copy = list(self.tiles)
            move_tile = copy[m]
            copy[m] = 0
            copy[blank_spot] = move_tile

            boards.append(PuzzleBoard(copy))
            
        return boards
        
