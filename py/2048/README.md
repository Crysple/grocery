# A very simple AI for the Game 2048

### Introduction

2048 is played on a 4x4 grid with numbered tiles which can slide up, down, left, or right. This game can be modeled as a two player game, in which the computer AI generates a 2- or 4-tile placed randomly on the board, and the player then selects a direction to move the tiles. Note that the tiles move until they either (1) collide with another tile, or (2) collide with the edge of the grid. If two tiles of the same number collide in a move, they merge into a single tile valued at the sum of the two originals. The resulting tile cannot merge with another tile again in the same move.

![image](https://user-images.githubusercontent.com/20517842/79291598-0f4ea900-7e9d-11ea-893b-3c5ff31edb97.png)

Usually, each role in a two-player games has a similar set of moves to choose from, and similar objectives (e.g. chess). In 2048 however, the player roles are inherently asymmetric, as the Computer AI places tiles and the Player moves them. So I apply adversarial search to write a simple AI.


### Algo

I use a popular algorithm -- [Expectiminimax](https://en.wikipedia.org/wiki/Expectiminimax) to implement the AI.

The tile-generating Computer AI of 2048 is not particularly adversarial as it spawns tiles irrespective of whether a spawn is the most adversarial to the user’s progress, with a 90% probability of a 2 and 10% for a 4 (from GameManager.py). However, my Player AI will play as if the computer is adversarial since this proves more effective in beating the game.

With expectiminimax, the game playing strategy assumes the Computer AI chooses a tile to place in a way that minimizes the Player’s outcome. Note whether or not the Computer AI is optimally adversarial is a question to consider. As a general principle, how far the opponent’s behavior deviates from the player’s assumption certainly affects how well the AI performs. However, this strategy works well in this game.

For the evalution part, I use a very simple heuristic function that I used to use when I was playing this game before. That is, to keep a monotonic wiggling path across the board by using a weighted matrix as follow:

![image](https://user-images.githubusercontent.com/20517842/79292326-cdbefd80-7e9e-11ea-99ad-ccda38d1df33.png)

This idea is also borrowed from this [paper](http://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf). Please refer to it for more information.

### Result

There is no any dependency, so just use `python3 GameManager.py` to start the game. By default, this file will display the board at each move with color. Also, the object-oriented code is quite straight-fordward.

Since the heuristic is quite simple and depth is no large, it can only reach 4096 with a small probability as follow:

![image](https://user-images.githubusercontent.com/20517842/79292551-65bce700-7e9f-11ea-81cd-2816d7f0a874.png)

Some more common results are 2048 and 1024.
