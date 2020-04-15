from Grid       import Grid
from ComputerAI import ComputerAI
from IntelligentAgent  import IntelligentAgent
from Displayer  import Displayer

import time
import random

defaultInitialTiles = 2
defaultProbability  = 0.9

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT",
    None: "NONE" # For error logging
}

(PLAYER_TURN, COMPUTER_TURN) = (0, 1)

# Time Limit Before Losing
timeLimit = 0.5
allowance = 0.05
maxTime   = timeLimit + allowance

class GameManager:
    def __init__(self, size=4, intelligentAgent=None, computerAI=None, displayer=None):
        self.grid = Grid(size)
        self.possibleNewTiles = [2, 4]
        self.probability = defaultProbability
        self.initTiles   = defaultInitialTiles
        self.over        = False

        # Initialize the AI players
        self.computerAI = computerAI or ComputerAI()
        self.intelligentAgent   = intelligentAgent   or IntelligentAgent()
        self.displayer  = displayer  or Displayer()
        self.cnt = self.total_time = 0

    def updateAlarm(self, turn) -> None:
        """ Checks if move exceeded the time limit and updates the alarm """
        cost_time = time.process_time() - self.prevTime
        if turn == PLAYER_TURN:
            self.total_time += cost_time
            self.cnt += 1
        if cost_time > maxTime:
            self.over = True
        
        self.prevTime = time.process_time()

    def getNewTileValue(self) -> int:
        """ Returns 2 with probability 0.95 and 4 with 0.05 """
        return self.possibleNewTiles[random.random() > self.probability]

    def insertRandomTiles(self, numTiles:int):
        """ Insert numTiles number of random tiles. For initialization """
        for i in range(numTiles):
            tileValue = self.getNewTileValue()
            cells     = self.grid.getAvailableCells()
            cell      = random.choice(cells) if cells else None
            self.grid.setCellValue(cell, tileValue)

    def start(self) -> int:
        """ Main method that handles running the game of 2048 """

        # Initialize the game
        self.insertRandomTiles(self.initTiles)
        self.displayer.display(self.grid)
        turn          = PLAYER_TURN # Player AI Goes First
        self.prevTime = time.process_time()

        while self.grid.canMove() and not self.over:
            # Copy to Ensure AI Cannot Change the Real Grid to Cheat
            gridCopy = self.grid.clone()

            move = None

            if turn == PLAYER_TURN:
                print("Player's Turn: ", end="")
                move = self.intelligentAgent.getMove(gridCopy)
                
                print(actionDic[move])

                # If move is valid, attempt to move the grid
                if move != None and 0 <= move < 4:
                    if self.grid.canMove([move]):
                        self.grid.move(move)

                    else:
                        print("Invalid intelligentAgent Move - Cannot move")
                        self.over = True
                else:
                    print("Invalid intelligentAgent Move - Invalid input")
                    self.over = True
            else:
                print("Computer's turn: ")
                move = self.computerAI.getMove(gridCopy)

                # Validate Move
                if move and self.grid.canInsert(move):
                    self.grid.setCellValue(move, self.getNewTileValue())
                else:
                    print("Invalid Computer AI Move")
                    self.over = True

            # Comment out during heuristing optimizations to increase runtimes.
            # Printing slows down computation time.
            self.displayer.display(self.grid)

            # Exceeding the Time Allotted for Any Turn Terminates the Game
            self.updateAlarm(turn)
            turn = 1 - turn
        #print(self.intelligentAgent.cnt, len(self.intelligentAgent.cache))
        print("avg cost time: ",self.total_time/self.cnt)
        return self.grid.getMaxTile()

def main():
    intelligentAgent = IntelligentAgent()
    computerAI  = ComputerAI()
    displayer   = Displayer()
    gameManager = GameManager(4, intelligentAgent, computerAI, displayer)

    maxTile     = gameManager.start()
    print(maxTile)

if __name__ == '__main__':
    main()
