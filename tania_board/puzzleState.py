GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Store the boards as a tuple:
class PuzzleState: 
    def __init__(self, board): #Self is the object and board is the value we are passing to it
        self.board = tuple(board) #Create a tuple for the board and pass it into "self" but labeled as board.
        self.blank_index = self.board.index(0) #Store the index of the blank tile into an object called 'blank_index.'


    # Method to check if we have reached the goal state
    def is_goal(self):
        return self.board == GOAL_STATE

    # Method to check the neighbors of the blank node (and facilitate swapping)
    # We'll need to check the neighbors in terms of (row,col) positions in a 3x3 grid.
    def check_neighbors(self):
        successors = [] #stores all the new puzzle states we get after moving a blank tile. 
        blank_row = self.blank_index // 3
        blank_col = self.blank_index % 3

        #Check above the blank tile: 
        new_row = blank_row - 1
        new_col = blank_col 
        if (0 <= new_row < 3) and (0 <= new_col < 3): #check if its a legal move i.e. indices should be between 0 and 3
            board_copy = list(self.board)
            new_index = new_row*3 + new_col
            temp = board_copy[self.blank_index]
            board_copy[self.blank_index] = board_copy[new_index]
            board_copy[new_index] = temp
            successors.append(PuzzleState(board_copy)) #or just pass the board_copy only??
       

        #Check below the blank tile: 
        new_row = blank_row + 1
        new_col = blank_col
        if (0 <= new_row < 3) and (0 <= new_col < 3):
            board_copy = list(self.board)
            new_index = new_row*3 + new_col
            temp = board_copy[self.blank_index]
            board_copy[self.blank_index] = board_copy[new_index]
            board_copy[new_index] = temp
            successors.append(PuzzleState(board_copy)) #or just pass the board_copy only??
                   


        #Check to the left of the blank tile: 
        new_row = blank_row 
        new_col = blank_col - 1
        if (0 <= new_row < 3) and (0 <= new_col < 3):
                board_copy = list(self.board)
                new_index = new_row*3 + new_col
                temp = board_copy[self.blank_index]
                board_copy[self.blank_index] = board_copy[new_index]
                board_copy[new_index] = temp
                successors.append(PuzzleState(board_copy)) #or just pass the board_copy only??
                      
            

        #Check to the right of the blank tile: 
        new_row = blank_row
        new_col = blank_col + 1
        if (0 <= new_row < 3) and (0 <= new_col < 3):
                board_copy = list(self.board)
                new_index = new_row*3 + new_col
                temp = board_copy[self.blank_index]
                board_copy[self.blank_index] = board_copy[new_index]
                board_copy[new_index] = temp
                successors.append(PuzzleState(board_copy)) #or just pass the board_copy only??
                      

        return(successors)


    ## We need a part where we first check if we've already visited this board. 
    #def equal_tiles(self, other):
         #return self.tiles == other.tiles


    #Implement Heuristic 1:
    def h1(self):  # Basically, how many tiles are not in their goal position?
        count = 0
        for i in range(9):
            tile = self.board[i]
            if tile != 0 and tile != GOAL_STATE[i]:
                count += 1
        return count


    #Implement Heuristic 2 (Manhattan):
    def h2(self):
        total_sum = 0
        for i in range(9):
            tile = self.board[i]
            if tile != 0:
               row = i // 3
               col = i % 3
               GOAL_row = GOAL_STATE.index(tile) // 3
               GOAL_col = GOAL_STATE.index(tile) % 3
               row_diff = abs(row - GOAL_row )
               col_diff = abs(col - GOAL_col)
               total_sum += row_diff + col_diff
        return total_sum
              

    #Implement Heuristic 3 (Relaxed Adjacency): 
    def h3(self):
        count = 0
        tiles = list(self.board)
        
        while tiles != list(GOAL_STATE):
             blank = tiles.index(0)

             if tiles[blank] == GOAL_STATE[blank]:
                  for i in range(9):
                       if tiles[i] != GOAL_STATE[i]:
                            target = i
                            break
                  temp = tiles[blank]
                  tiles[blank] = tiles[target]
                  tiles[target] = temp

             else:
                  move_tile = GOAL_STATE[blank]
                  target = tiles.index(move_tile)

                  temp = tiles[blank]
                  tiles[blank] = tiles[target]
                  tiles[target] = temp
             
             count += 1
        return count