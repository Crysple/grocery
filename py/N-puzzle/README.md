# Introduction

The N-puzzle game consists of a board holding N = m2 − 1 distinct movable tiles, plus one empty space. There is one tile for each number in the set {0, 1,..., m2 − 1}. In this code, I will represent the blank space with the number 0 and focus on the m = 3 case (8-puzzle).

In this combinatorial search problem, the aim is to get from any initial board state to the configuration with all tiles arranged in ascending order {0, 1,..., m2 − 1} – this is the goal state. The search space is the set of all possible states reachable from the initial state. Each move consists of swapping the empty space with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}. Give each move a cost of one. Thus, the total cost of a path will be equal to the number of moves made.



# Algorithms

- **bfs (Breadth-First Search)**
- **dfs (Depth-First Search)**
- **ast (A-Star Search)**

For each algorithm, the outputs are the solution and some other statistics, including `path to goal`, `cost of path`, `nodes expanded`,  `search depth`, `max search depth`, `running time`, `max ram usage`.



# Usage

The board argument will be a comma-separated list of integers containing no spaces. For example, to use the bread-first search strategy to solve the input board given by the starting configuration {0,8,7,6,5,4,3,2,1}, the program will be executed like so (with no spaces between commas):

`$ python3 puzzle_solver.py bfs 1,2,5,3,4,0,6,7,8`

This should result in the solution path:

![image](https://user-images.githubusercontent.com/20517842/76239220-90b07d00-6207-11ea-99ea-d0f747e2e0f0.png)

The output file will contain exactly the following lines:

- path to goal: [‘Up’, ‘Left’, ‘Left’]
- cost of path: 3
- nodes expanded: 10
- search depth: 3
- max search depth: 4
- running time: 0.00188088
- max ram usage: 0.07812500
