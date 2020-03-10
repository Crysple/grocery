from __future__ import division
from __future__ import print_function

import sys
import math
import time
import queue
import resource


## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0, blank_index=-1):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = tuple(config)
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = blank_index if blank_index!=-1 else self.config.index(0)

    def __lt__(self, o):
        return True

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3*i : 3*(i+1)])

    def config_after_move(self, moved_index):
        """ Move `moved_index` to blank and return a new config"""
        nconfig = list(self.config)
        nconfig[self.blank_index], nconfig[moved_index] = nconfig[moved_index], nconfig[self.blank_index]

        return nconfig

    def move_up(self):
        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index >= self.n:
            moved_index = self.blank_index - self.n
            nconfig = self.config_after_move(moved_index)
            return PuzzleState(nconfig, self.n, self, 'Up', self.cost+1, moved_index)

        return None
        
      
    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index < self.n*(self.n-1):
            moved_index = self.blank_index + self.n
            nconfig = self.config_after_move(moved_index)
            return PuzzleState(nconfig, self.n, self, 'Down', self.cost+1, moved_index)

        return None
      
    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index % self.n != 0:
            moved_index = self.blank_index - 1
            nconfig = self.config_after_move(moved_index)
            return PuzzleState(nconfig, self.n, self, 'Left', self.cost+1, moved_index)

        return None
        

    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        if (self.blank_index+1) % self.n != 0:
            moved_index = self.blank_index + 1
            nconfig = self.config_after_move(moved_index)
            return PuzzleState(nconfig, self.n, self, 'Right', self.cost+1, moved_index)

        return None
      
    def expand(self):
        """ Generate the child nodes of this node """
        
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children

# Function that Writes to output.txt

def writeOutput(path, cost, n_nodes, depth, max_depth, used_time, used_ram):
    content = "path to goal: {}\n".format(path)
    content += "cost of path: {}\n".format(cost)
    content += "nodes expanded: {}\n".format(n_nodes)
    content += "search depth: {}\n".format(depth)
    content += "max search depth: {}\n".format(max_depth)
    content += "running time: {:.3f}\n".format(used_time)
    content += "max ram usage: {} MB\n".format(used_ram)
    with open('output.txt', 'w') as f:
        f.write(content)

def log(solver):
    """solver returns:
    - final state
    - number of nodes expanded
    - max depth ever explored
    """
    def get_path(state):
        path = []
        while state:
            path += state.action,
            state = state.parent
        return path[::-1][1:]

    def wrapped_solver(*args, **kwargs):
        start_time = time.time()
        state, n_nodes, max_depth = solver(*args, **kwargs)
        used_time = time.time() - start_time
        path = get_path(state)
        used_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024/1024
        writeOutput(get_path(state), state.cost, n_nodes,
                        depth=len(path), max_depth=max_depth, used_time=used_time,
                        used_ram=used_ram)
        return state

    return wrapped_solver

@log
def bfs_search(initial_state):
    """BFS search"""
    visited = set()
    frontier = {initial_state.config}
    q = queue.Queue()
    q.put(initial_state)
    max_depth = 0
    while not q.empty():
        state = q.get()
        max_depth = max(max_depth, state.cost+1)
        if test_goal(state):
            return state, len(visited), max_depth
        visited.add(state.config)
        for neighbor in state.expand():
            if not (neighbor.config in visited or neighbor.config in frontier):
                q.put(neighbor)
                frontier.add(neighbor.config)
        frontier.remove(state.config)
    return None, None, None

@log
def dfs_search(initial_state):
    """DFS search"""
    stack = [initial_state]
    max_depth = 0
    visited = set()
    frontier = {initial_state.config}
    while stack:
        state = stack.pop()
        max_depth = max(max_depth, state.cost)
        if test_goal(state):
            return state, len(visited), max_depth
        visited.add(state.config)
        neighbors = [s for s in state.expand() if not (s.config in visited or s.config in frontier)]
        if neighbors:
            stack.extend(neighbors[::-1])
            frontier |= {n.config for n in neighbors}
        frontier.remove(state.config)
    return None, None, None

@log
def A_star_search(initial_state):
    """A * search"""
    prio_q = queue.PriorityQueue()
    prio_q.put((calculate_total_cost(initial_state), initial_state))
    visited = {initial_state.config}
    frontier = {initial_state.config}
    max_depth = 0
    while not prio_q.empty():
        state = prio_q.get()[1]
        max_depth = max(max_depth, state.cost)
        if test_goal(state):
            return state, len(visited), max_depth
        visited.add(state.config)
        for neighbor in state.expand():
            if not (neighbor.config in visited or neighbor.config in frontier):
                prio_q.put((calculate_total_cost(neighbor), neighbor))
                frontier.add(neighbor.config)
        frontier.remove(state.config)
    return None, None, None


def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    cmd = sum([calculate_manhattan_dist(idx, val, state.n) for idx, val in enumerate(state.config)])

    return cmd + state.cost

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    return abs(value%n-idx%n) + abs(int(value//n-idx//n))

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    return [*puzzle_state.config] == [*range(puzzle_state.n**2)]

# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    if   search_mode == "bfs": bfs_search(hard_state)
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        exit(-1)
        
    end_time = time.time()
    print("Program completed in %.3f second(s)"%(end_time-start_time))

if __name__ == '__main__':
    main()
