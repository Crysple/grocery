class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        X = O = n_win = 0
        def check_win_by_row(board, player):
            for row in board:
                if ''.join(row) == player*3:
                    return True
            return False
        def check_win_by_diagonal(board, player):
            return ''.join(board[i][i] for i in range(3)) == player*3 \
                or ''.join(board[i][2-i] for i in range(3)) == player*3
        # corner case: X > O but O wins
        cnt = collections.Counter("".join(board))
        if cnt['X']-cnt['O'] not in [0, 1]:
            return False
        if (check_win_by_row(board, 'X') or check_win_by_row(zip(*board), 'X')\
                or check_win_by_diagonal(board, 'X'))\
            and cnt['X']-cnt['O'] != 1:
            return False
        if (check_win_by_row(board, 'O') or check_win_by_row(zip(*board), 'O')\
                or check_win_by_diagonal(board, 'O'))\
            and cnt['X'] != cnt['O']:
            return False
        return True
