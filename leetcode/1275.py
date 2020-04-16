class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check_win(moves):
            #print(moves)
            row = [0] * 3
            col = [0] * 3
            for i, j in moves:
                row[i] += 1
                col[j] += 1
            if max(row) == 3 or max(col) == 3:
                return True
            diagonal = rdiagonal = True
            for i in range(3):
                if [i, i] not in moves:
                    diagonal = False
                if [i, 2-i] not in moves:
                    rdiagonal = False
            return rdiagonal or diagonal

        if check_win(moves[0::2]):
            return "A"
        if check_win(moves[1::2]):
            return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"
