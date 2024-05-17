from gamestate import GameState
from heuristics import Heuristics

import random
import copy

class NineMensMorris():
    def __init__(self, difficulty='easy', ai=True):
        self.difficulty = difficulty
        self.ai = ai
        self.initial = GameState()
        self.move_map = {
            'A1':{'A4', 'D1'},
            'D1':{'A1', 'D2', 'G1'},
            'G1':{'D1', 'G4'},
            'B2':{'B4', 'D2'},
            'D2':{'B2', 'D1', 'D3', 'F2'},
            'F2':{'D2', 'F4'},
            'C3':{'C4', 'D3'},
            'D3':{'C3', 'D2', 'E3'},
            'E3':{'D3', 'E4'},
            'A4':{'A1', 'A7', 'B4'},
            'B4':{'A4', 'B2', 'B6', 'C4'},
            'C4':{'B4', 'C3', 'C5'},
            'E4':{'E3', 'E5', 'F4'},
            'F4':{'E4', 'F2', 'F6', 'G4'},
            'G4':{'F4', 'G1', 'G7'},
            'C5':{'C4', 'D5'},
            'D5':{'C5', 'D6', 'E5'},
            'E5':{'D5', 'E4'},
            'B6':{'B4', 'D6'},
            'D6':{'B6', 'D5', 'D7', 'F6'},
            'F6':{'D6', 'F4'},
            'A7':{'A4', 'D7'},
            'D7':{'A7', 'D6', 'G7'},
            'G7':{'D7', 'G4'}
        }
        self.mills = {
            frozenset({'A1', 'D1', 'G1'}),
            frozenset({'B2', 'D2', 'F2'}),
            frozenset({'C3', 'D3', 'E3'}),
            frozenset({'A4', 'B4', 'C4'}),
            frozenset({'E4', 'F4', 'G4'}),
            frozenset({'C5', 'D5', 'E5'}),
            frozenset({'B6', 'D6', 'F6'}),
            frozenset({'A7', 'D7', 'G7'}),
            frozenset({'A1', 'A4', 'A7'}),
            frozenset({'B2', 'B4', 'B6'}),
            frozenset({'C3', 'C4', 'C5'}),
            frozenset({'D1', 'D2', 'D3'}),
            frozenset({'D5', 'D6', 'D7'}),
            frozenset({'E3', 'E4', 'E5'}),
            frozenset({'F2', 'F4', 'F6'}),
            frozenset({'G1', 'G4', 'G7'})
        }
        self.depth_mapping = {
            'easy': 2,
            'medium': 4,
            'hard': 6
        }

    def actions(self, state):
        action_map = {
            'set': self.set_actions,
            'move': self.move_actions,
            'take': self.take_actions,
            'jump': self.jump_actions
        }

        if state.move_type in action_map:
            moves = action_map[state.move_type](state=state)
            return moves    
        else:
            raise Exception(f"Invalid Move Type! Use 'set', 'move', 'take' or 'jump'.")

    
    def result(self, state, move):
        result_map = {
            'set': self.set_result,
            'move': self.move_result,
            'take': self.take_result,
            'jump': self.jump_result
        }
        cloned_state = copy.deepcopy(state)
        
        if cloned_state.move_type not in result_map: raise Exception("Invalid Move Type! Use 'set', 'move', 'take' or 'jump'.")
        if move not in self.actions(cloned_state): raise Exception(f"Move; {move} is Illegal for State:\n{state}\nUse one of these Moves: {self.actions(cloned_state)}")
        else: return result_map[state.move_type](state=cloned_state, move=move)
    
    def evaluation(self, state, player):
        heuristics = Heuristics()
        return heuristics.get_heuristic(state=state, player=player, difficulty=self.difficulty)
    
    def utility(self, state, player):
        return 1 if self.get_winner(state=state) == player else 0
    
    # Returns True if the Game has reached a terminal State and is over
    def terminal_test(self, state):
        if (state.pieces_b + state.pieces_w) != 0: return False
        if (len(self.actions(state=state))== 0): return True
        black_pieces = 0
        white_pieces = 0
        for piece in state.board.values():
            if(piece == 'b'): black_pieces += 1
            elif(piece == 'w'): white_pieces += 1
        return black_pieces <= 2 or white_pieces <= 2

    def max_value(self, state, alpha, beta, current_depth, player):
        if self.terminal_test(state): return self.utility(state, player) 
        if current_depth <= 0: return self.evaluation(state, player)
        
        v = float('-inf')
        next_depth = current_depth - 1
        moves = self.actions(state)
        for action in moves:
            next_state = self.result(state, action)
            if(next_state.to_move == player): v = max(v, self.max_value(next_state, alpha, beta, next_depth, player))
            else: v = max(v, self.min_value(next_state, alpha, beta, next_depth, player))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta, current_depth, player):
        if self.terminal_test(state): return self.utility(state, player)
        if current_depth <= 0: return self.evaluation(state, player)

        v = float('inf')
        next_depth = current_depth - 1
        moves = self.actions(state)
        for action in moves:
            next_state = self.result(state, action)
            if(next_state.to_move == player): v = min(v, self.max_value(next_state, alpha, beta, next_depth, player))
            else: v = min(v, self.min_value(next_state, alpha, beta, next_depth, player))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
    
    def get_best_move(self, state, player, depth=None, dynamic_depth=True):
        if dynamic_depth: depth = self.get_dynamic_depth(state=state)
        if not depth: raise Exception(f"Could not determine Search-Depth: Dynamic Depth was disabled and no Depth was given.")

        best_score = float('-inf')
        best_action = None
        for action in self.actions(state):
            next_state = self.result(state, action)
            if(next_state.to_move == player):
                score = self.max_value(next_state, best_score, float('inf'), depth - 1, player)
            else: 
                score = self.min_value(next_state, best_score, float('inf'), depth - 1, player)
            if score > best_score:
                best_score = score
                best_action = action

        return best_action
    
    def get_dynamic_depth(self, state):
        if state.to_move == 'jump': return 3
        pieces_on_board = 0
        for value in state.board.values():
            if value != 'e': pieces_on_board +=1
        depth = int(pieces_on_board/3) + 1
        return depth if depth >=3 else 4
    
    def get_winner(self, state):
        if not self.terminal_test(state): raise Exception("No Player has won yet. Continue the game")
        if (len(self.actions(state=state))== 0): return 'b' if state.to_move == 'w' else 'w'
        black_pieces = 0
        white_pieces = 0
        for piece in state.board.values():
            if(piece == 'b'): black_pieces += 1
            elif(piece == 'w'): white_pieces += 1
        return 'b' if white_pieces <= 2 else 'w'

    # Different Move_types take advantage of different Actions Methods

    def set_actions(self, state):
        moves = set()
        for key, value in state.board.items():
            if(value == 'e'): moves.add(key)
        return moves

    def move_actions(self, state):
        moves = set()
        for key, value in state.board.items():
            if(value == state.to_move):
                for neighbour in self.move_map[key]:
                    if(state.board[neighbour] == 'e'):
                        moves.add((key, neighbour))
        return moves

    def take_actions(self, state):
        opponent = 'w' if state.to_move == 'b' else 'b'
        moves = set()

        for key, value in state.board.items():
            if(value == opponent and not self.piece_in_mill(board=state.board, piece=key)): moves.add(key)
        return moves

    def jump_actions(self, state):
        moves = set()
        for key, value in state.board.items():
            if(value == state.to_move):
                for key2, value2 in state.board.items():
                    if(value2 == 'e'):
                        moves.add((key, key2))
        return moves
    
    # Returns True if a given Piece is in a Mill
    def piece_in_mill(self, board, piece):
        color = board[piece]

        for mill in self.mills:
            if(piece in mill):
                if(all(board[piece] == color for piece in mill)): return True

        return False

    # Different Move_types take advantage of different Result Methods

    def set_result(self, state, move):
        new_state = copy.deepcopy(state)
        new_state.board[move] = state.to_move
        if state.to_move == 'b': new_state.pieces_b -= 1
        else: new_state.pieces_w -= 1

        if self.piece_in_mill(board=new_state.board, piece=move) and self.can_take(board=new_state.board, player=state.to_move):
            new_state.move_type = 'take'
        else:
            new_state.to_move = 'b' if state.to_move == 'w' else 'w'
            if (new_state.pieces_b + new_state.pieces_w) == 0:
                new_state.move_type = 'move'
            else:
                new_state.move_type = 'set'
        return new_state


    def move_result(self, state, move):
        new_state = state
        new_state.board[move[0]], new_state.board[move[1]] = new_state.board[move[1]], new_state.board[move[0]]

        if(self.piece_in_mill(board=new_state.board, piece=move[1]) and self.can_take(board=new_state.board, player=state.to_move)):
            new_state.move_type = 'take'
            return new_state
        
        new_state.to_move = 'b' if state.to_move == 'w' else 'w'
        new_state.move_type = 'jump' if self.can_jump(board=new_state.board, player=new_state.to_move) else 'move'
        return new_state

    def take_result(self, state, move):
        new_state = state
        new_state.board[move] = 'e'
        new_state.to_move = 'b' if state.to_move == 'w' else 'w'

        if(self.can_jump(board=new_state.board, player=new_state.to_move)): new_state.move_type = 'jump'
        elif (new_state.pieces_b + new_state.pieces_w) != 0: new_state.move_type = 'set'
        else: new_state.move_type = 'move'

        return new_state

    def jump_result(self, state, move):
        return self.move_result(state=state, move=move)

    # Returns True if there are any enemy pieces which can be taken meaning they are not in mills
    def can_take(self, board, player):
        opponent = 'w' if player == 'b' else 'b'

        for key, value in board.items():
            if(value == opponent and not self.piece_in_mill(board=board, piece=key)): return True
        return False

    #Returns True if a Player has exactly 3 pieces meaning he is allowed to jump
    def can_jump(self, board, player):
        amount_pieces = 0
        for value in board.values():
            if(value == player): amount_pieces += 1
        return amount_pieces == 3
    
