"""
Each sudoku board is represented as two-dimensional array with
int values.
"""
import sys
import time
from statistics import stdev


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in range(9):
        row = ''
        for j in range(9):
            row += (str(board[i][j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in range(9):
        for c in range(9):
            ordered_vals.append(str(board[r][c]))
    return ''.join(ordered_vals)

def pack(i, j):
    '''Pack as a tuple (row, column, block_id)'''
    return (i, j, i//3*3+j//3)

def get_minimum_remaining_value(remaining, domains):
    '''Get entry with minimum remaining values in its domain'''
    minv = 10
    entry = None
    for i, j, _ in remaining:
        if minv > len(domains[i, j]):
            minv = len(domains[i, j])
            entry = i, j
    return entry

def forward_checking(changed_entry, value, remaining, domains, board):
    '''Return False if there's any empty domain'''
    modify_entries = []
    for entry in remaining:
        if any([i==j for i, j in zip(entry, changed_entry)]) and value in domains[entry[:2]]:
            domains[entry[:2]].remove(value)
            modify_entries.append(entry)
            if not domains[entry[:2]]:
                return False, modify_entries
    return True, modify_entries

def add_values_to_doamin(modify_entries, domains, value):
    '''Reversion in bt: add values back to domain'''
    for r, c, _ in modify_entries:
        domains[r, c].add(value)

def _backtracking(board, remaining, domains):
    r, c = get_minimum_remaining_value(remaining, domains)
    remaining.remove(pack(r,c))
    for value in domains[r, c]:
        board[r][c] = value
        success, modify_entries = forward_checking(pack(r, c), value, remaining, domains, board)
        if success:
            if not remaining or _backtracking(board, remaining, domains):
                return True
        # revert domains no matter success or not
        add_values_to_doamin(modify_entries, domains, value)
    remaining.add(pack(r,c))
    board[r][c] = 0
    return False

def backtracking(board):
    """Takes a board and returns solved board."""
    remaining = set()
    domains = dict()
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                remaining.add(pack(i, j))
                domains[i, j] = set(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                if not forward_checking(pack(i, j), board[i][j], remaining, domains, board):
                    raise Exception("Error: this sudoku has no solution!")
    if not _backtracking(board, remaining, domains):
        raise Exception("Error: this sudoku has no solution!")
    return board


def check_my_ans():
    with open('sudokus_finish.txt') as ans:
        with open('output.txt') as myans:
            return ans.read() == myans.read()


if __name__ == '__main__':
    #  Argument Mode
    if len(sys.argv) > 1:
        sudoku_list = sys.argv[1]
        if sudoku_list == 'score':
            print(check_my_ans())
            exit(0)
    else:
        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    times = []
    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = [[int(line[9*r+c]) for c in range(9)] for r in range(9)]

        # Print starting board.
        # print_board(board)

        # Solve with backtracking

        start_time = time.time()
        solved_board = backtracking(board)
        #print_board(solved_board)
        times.append(time.time() - start_time)

        # Print solved board.
        # print_board(solved_board)

        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')
    print("Min Time: ", min(times))
    print("Max Time: ", max(times))
    print("Mean Time: ", sum(times)/len(times))
    print("Standard Deviation: ", stdev(times))
    


    print("Finishing all boards in file.")
