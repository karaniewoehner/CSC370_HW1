from puzzleState import PuzzleState
import heapq


class Node: 
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h



def a_star(start_board, heuristic_function):
    start_state = PuzzleState(start_board)
    start_node = Node(start_state, None, 0, heuristic_function(start_state))

    #Initialize the frontier
    frontier = []
    counter = 0 #This will keep track of the nth node that has been visited --> Helps when f values are a tie and the priority queue needs to compare some other value other than the node
    heapq.heappush(frontier, (start_node.f, counter, start_node))

    explored = set()
    nodes_generated = 1 

    #Check if the frontier is empty, then return failure 
    while True: 
        if not frontier:
            return None 

        current_f, current_counter, current_node = heapq.heappop(frontier)

        if current_node.state.board in explored: 
            continue

        explored.add(current_node.state.board)
        
        if current_node.state.is_goal():
            return current_node, nodes_generated

        successors = current_node.state.check_neighbors()

        #Loop over successors and create the search node: 
        for successor_state in successors: 
            if successor_state.board in explored: #check if the successor we're about to add has already been explored. 
                continue


            counter += 1 #the tiebreaker we created for the priority queue
            new_g = current_node.g + 1 #sliding a tile once (one move) costs one step, hence we add 1.
            new_h = heuristic_function(successor_state)
            new_node = Node(successor_state, current_node, new_g, new_h) #current_node is the parent node
            heapq.heappush(frontier, (new_node.f, counter, new_node))
            nodes_generated += 1 #Keep track of how many nodes we've visited.




       
        

