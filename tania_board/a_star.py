class Node: 
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h



import heapq

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
        if current_node.state.is_goal():
            return current_node, nodes_generated
    
