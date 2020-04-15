import random, math
from BaseAI import BaseAI
from collections import Counter
# 1024 2048 256 2048 1024 4096 2048 1024 2048 512

class IntelligentAgent(BaseAI):
    def __init__(self):
        super(IntelligentAgent, self).__init__()
        weights_1d = [2*i for i in range(16)]
        self.possible_new_tiles_with_probs = [(2, 0.9), (4, 0.1)]
        self.max_depth = 4
        self.cache = dict()

        ws1 = [weights_1d[i*4:(i+1)*4][::(-1 if i & 1 else 1)] for i in range(4)]
        self.ws = [ws1]
        def rotate(x):
            return [*zip(*x)][::-1]
        for i in range(3):
            self.ws.append(rotate(self.ws[-1]))
        for i in range(4):
            self.ws.append(self.ws[i][::-1])

    def eval_score(self, grid):
        return max([sum([(grid.map[i][j] << w[i][j])
                 for i in range(4) for j in range(4)])
                 for w in self.ws])

    def chance_node(self, grid, cell, a, b, level):
        avg_score = 0
        for tile, prob in self.possible_new_tiles_with_probs:
            grid.setCellValue(cell, tile)
            avg_score += prob * self.maximize(grid, a, b, level)
        grid.setCellValue(cell, 0)
        return avg_score

    def minimize(self, grid, a, b, level):
        """
        Param:
            a, b: alpha-beta pruning
            level: current level of tree
        """
        key = tuple(tuple(line) for line in grid.map)
        if (key, a, b) in self.cache:
            return self.cache[key, a, b]
        if not level:
            return self.eval_score(grid)
        min_score = float("inf")
        available_cells = grid.getAvailableCells()
        for cell in random.sample(available_cells, min(4, len(available_cells))):
        #for cell in available_cells:
            if min_score < a:  # already have another greater score a at the previous maximum layer
                return min_score
            min_score = min(min_score, self.chance_node(
                grid, cell, a, min_score, level-1))

        self.cache[key, a, b] = min_score
        return self.cache[key, a, b]

    def maximize(self, grid, a, b, level, return_move=False):
        """
        Param:
            a, b: alpha-beta pruning
            level: current level of tree
            return_move: return max_score & corresponding move if True else only max_score
        """
        key = tuple(tuple(line) for line in grid.map)
        if (key, a, b) in self.cache:
            return self.cache[key, a, b]
        if not level:
            return self.eval_score(grid)
        max_score, cor_move = 0, None
        for move, grid_dup in grid.getAvailableMoves():
            if max_score > b:  # already have another smaller score a at the previous minimize layer
                return max_score
            score = self.minimize(grid_dup, max_score, b, level-1)
            # if move == 0:
            #     score *= 0.7
            if score >= max_score:
                max_score = score
                cor_move = move

        self.cache[key, a, b] = max_score
        if return_move:
            return max_score, cor_move
        return max_score

    def getMove(self, grid):
        # Selects a random move and returns it

        _, move = self.maximize(grid, -1, float('inf'), self.max_depth, True)
        return move

# with cache:   ---- Faster
# 2048: 0.015429719457013585   1024: 0.017464951781970665 0.01729022594142258 0.017409648283038467
# 4096: 0.015529674516400355   512: 0.01708577952755905
# without cache:
# 2048: 0.017768383321141182 0.018539023941068117   1024: 0.018481292553191492
