import heapq
from CSC370_8PuzzleBoard import PuzzleBoard


class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h


def a_star(initial, heuristic):
    start_node = Node(initial, None, 0, heuristic(initial))

    # Initialize the frontier
    frontier = []
    counter = 0  # Counter will act as tie-breaker for the priority queue when f values match --> When its time to compare nodes in the pq.
    heapq.heappush(frontier, (start_node.f, counter, start_node))

    visited = set()
    nodes_generated = 1 

    while True:
        if not frontier:
            return None

        current_f, current_counter, current_node = heapq.heappop(frontier) 

        if current_node.state.tiles in visited:
            continue

        visited.add(current_node.state.tiles)

        if current_node.state.goal_reached():
            return current_node.g, nodes_generated

        successors = current_node.state.neighbors()

        for successor_state in successors:
            if successor_state.tiles in visited:
                continue

            counter += 1
            new_g = current_node.g + 1
            new_h = heuristic(successor_state)
            new_node = Node(successor_state, current_node, new_g, new_h)
            heapq.heappush(frontier, (new_node.f, counter, new_node))
            nodes_generated += 1