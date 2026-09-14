import heapq
from CSC370_8PuzzleBoard import PuzzleBoard

def a_star(initial, heuristic):
    nodes_generated = 1
    counter = 0
    ## initialize frontier using initial state of problem of starting board
    ## and hueristic function as a priority queue
    frontier = [(heuristic(initial), counter, 0, initial)]
    ## Track boards that are fully explored
    visited = set()

    while frontier:
        ## pop node from frontier
        f, _, g, board = heapq.heappop(frontier)

        ## if node contains goal state, return solution
        if board.goal_reached():
            return g, nodes_generated
        ## if we already visited board, add to list
        if board in visited:
            continue
        visited.add(board)

        ## else, for each successor one move away from node, add to frontier
        for neighbor in board.neighbors():
            nodes_generated += 1

            if neighbor not in visited:
                counter += 1
                new_g = g + 1
                ## f = g + h
                new_f = new_g + heuristic(neighbor)
                ## add to frontier
                heapq.heappush(frontier, (new_f, counter, new_g, neighbor))
        
    return None, nodes_generated



