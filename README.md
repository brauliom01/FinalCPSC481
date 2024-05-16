# Nine Men´s Morris - a Final Project for CPSC-481 Artificial Intelligence at Calstate Fullerton

## Group Members
- Felix Neu
- Braulio Martin
- Chris Pedroza

## About this Repository
This repository contains the game Nine Men's Morris, also known as Mills, programmed in Python. Players have the option to compete against each other or against an Artificial Intelligence (AI). The AI offers three difficulty levels: Easy, Medium, and Hard. It utilizes a depth-limited Alpha-Beta Pruning algorithm, where the depth is dynamically determined based on the game state to control response time variance. Each difficulty level uses different game state evaluation functions.

## Library Requirements
- pygame

## How to use
Simply run board.py and the Game UI will start right up!

## Files and Folders
- NineMensMorris.py: Includes Class NineMensMorrs() and is central point for Gamelogic and AI Algorithms
- board.py: Visual Representation of Game States provided by NineMensMorris using Pygame Library
- gamestate.py: Includes Class GameState used to represent Game States througout the whole Project
- heurisitcs.py: Includes Class Heuristics which is used to calculate different Evaluations for Game States
- ai_analytics/: Folder for analyzing AI-Performance
  - teststates.py: Includes set of 40 unique Game States used for Evaluations
  - analytics.iypnb: Notebook used to Evaluate Game States (Requires Pandas Library)
  - data/: Folder with Test Result Data
 
## Class NineMensMorris
### Public Methods
- __actions(state)__: Determines all possible moves for a given game state. The type of moves (set, move, take, or jump) depends on the current phase of the game and the state of the board. The function selects the appropriate action function based on the `move_type` attribute of the game state.
- __result(state, move)__: Returns the new game state that results from making a given move in the current state. It deep copies the current state to avoid modifying the original and then applies the move based on the `move_type`. The method ensures the move is legal and updates the state accordingly.
- __get_best_move(state, player, depth=None, dynamic_depth=True)__: Determines the best move for a player from the current state using a minimax algorithm with alpha-beta pruning. It evaluates the game tree up to a specified depth, which can be dynamically determined based on the game state. The function returns the move that maximizes the player's advantage or minimizes their disadvantage.
- __terminal_test(state)__: Checks if the game has reached a terminal state, meaning the game is over. It evaluates the game state to determine if there are no pieces left to place, no possible moves left, or if one player has two or fewer pieces left on the board. If any of these conditions are met, the game is considered over.
- __get_winner(state)__: Determines the winner of the game if it has reached a terminal state. It checks if the game is over using the terminal_test method and then evaluates the board to see which player has won. If a player cannot move or has two or fewer pieces remaining, the other player is declared the winner.

### Private Methods
- evaluation(self, state, player)
- utility(self, state, player)
- max_value(self, state, alpha, beta, current_depth, player)
- min_value(self, state, alpha, beta, current_depth, player)
- get_dynamic_depth(self, state)
- set_actions(self, state)
- move_actions(self, state)
- take_actions(self, state)
- jump_actions(self, state)
- piece_in_mill(self, board, piece)
- set_result(self, state, move)
- move_result(self, state, move)
- take_result(self, state, move)
- jump_result(self, state, move)
- can_take(self, board, player)
- can_jump(self, board, player)


