from gamestate import GameState
from heuristics import Heuristics

import random

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

    def actions(self, state):
        action_map = {
            'set': self.set_actions,
            'move': self.move_actions,
            'take': self.take_actions,
            'jump': self.jump_actions
        }

        if state.move_type in action_map:
            return action_map[state.move_type](state=state)
        else:
            raise Exception("Invalid Move Type! Use 'set', 'move', 'take' or 'jump'.")

    
    def result(self, state, move):
        result_map = {
            'set': self.set_result,
            'move': self.move_result,
            'take': self.take_result,
            'jump': self.jump_result
        }

        if state.move_type not in result_map: raise Exception("Invalid Move Type! Use 'set', 'move', 'take' or 'jump'.")
        if move not in self.actions(state): raise Exception(f"Illegal Move! Use one of these Moves: {self.actions(state)}")
        else: return result_map[state.move_type](state=state, move=move)
    
    def utility(self, state, player):
        heuristics = Heuristics()
        return heuristics.get_heuristic(state=state, player=player, difficulty=self.difficulty)
    
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
    
    def get_best_move(self, state, player):
        raise NotImplementedError
    
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
        new_state = state
        new_state.board[move] = state.to_move
        if state.to_move == 'b': new_state.pieces_b -= 1
        else: new_state.pieces_w -= 1

        if(self.piece_in_mill(board=new_state.board, piece=move) and self.can_take(board=new_state.board, player=state.to_move)):
            new_state.move_type = 'take'
            return new_state
        
        new_state.to_move = 'b' if state.to_move == 'w' else 'w'
        new_state.move_type = 'move' if (new_state.pieces_b + new_state.pieces_w) == 0 else 'set'
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
    

if __name__ == '__main__':
    nmm = NineMensMorris(difficulty='easy')
    current_state = nmm.initial

    while not nmm.terminal_test(current_state):
        moves = nmm.actions(state=current_state)
        print(current_state)
        if current_state.to_move == 'b':
            # Logic to ask User for one of the Moves
            print("Available moves:", moves)
            user_move = input("Please select a move from the list: ")
            while user_move not in moves:
                print("Invalid move. Please select a move from the list.")
                user_move = input("Please select a move from the list: ")
            move = user_move
        else:
            # Logic for a random selector to select one random move
            move = random.choice(list(moves))
            
        current_state = nmm.result(state=current_state, move=move)
        
    winner = nmm.get_winner(state=current_state)
    print(f'{winner} won the game!')
