class Heuristics:
    def __init__(self) -> None:
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
        self.heuristics = {
            'easy': {
            self.own_pieces_value,
            self.opponent_pieces_value,
            self.own_open_mills_value,
            self.opponent_open_mills_value
            },
            'medium': {
            self.own_pieces_value,
            self.opponent_pieces_value,
            self.own_possible_moves_value,
            self.opponent_possible_moves_value,
            self.own_mills_value,
            self.opponent_mills_value,
            },
            'hard':{
            self.own_pieces_value,
            self.opponent_pieces_value,
            self.own_possible_moves_value,
            self.opponent_possible_moves_value,
            self.own_mills_value,
            self.opponent_mills_value,
            self.own_open_mills_value,
            self.opponent_open_mills_value,
            self.potential_moves_value
            }
        }

    def get_heuristic(self, state, player, difficulty):
        values = []
        for heuristic in self.heuristics[difficulty]:
            values.append(heuristic(state, player))

        return sum(values)

    def own_pieces_value(self, state, player):
        value_mapping = {
            9: 0.35,
            8: 0.3,
            7: 0.25,
            6: 0.2,
            5: 0.15,
            4: 0.1
        }

        amount_pieces = 0
        for value in state.board.values():
            if(value == player): amount_pieces += 1

        return value_mapping[amount_pieces] if amount_pieces > 3 else 0

    def opponent_pieces_value(self, state, player):
        opponent = 'b' if player == 'w' else 'w'
        return -self.own_pieces_value(state, opponent)
    
    def own_possible_moves_value(self, state, player):
        value_mapping = {
            9: 0.25,
            8: 0.25,
            7: 0.2,
            6: 0.2,
            5: 0.15,
            4: 0.15,
            3: 0.1,
            2: 0.1,
            1: 0,
            0: 0
        }

        amount_moves = 0
        for key, value in state.board.items():
            if(value == player):
                for neighbour in self.move_map[key]:
                    if(state.board[neighbour] == 'e'):
                        amount_moves +=1

        return value_mapping[amount_moves] if amount_moves in value_mapping else 0.3
    
    def opponent_possible_moves_value(self, state, player):
        opponent = 'b' if player == 'w' else 'w'
        return -self.own_possible_moves_value(state, opponent)
    
    def potential_moves_value(self, state, player):
        value_mapping = {
            6: 0.08,
            5: 0.08,
            4: 0.08,
            3: 0.04,
            2: 0.04,
            1: 0.02,
            0: 0,
            -1: -0.02,
            -2: -0.04,
            -3: -0.04,
            -4: -0.08,
            -5: -0.08,
            -6: -0.08
        }

        amount_own_moves = self.amount_potential_moves(state, player)
        amount_opponent_moves = self.amount_potential_moves(state, 'b' if player == 'w' else 'w')
        difference = amount_own_moves-amount_opponent_moves

        if(difference>=7): return 0.16
        elif(difference<=-7): return -0.16
        else: return value_mapping[difference]


    def amount_potential_moves(self, state, player):
        amount_moves = 0
        for key, value in state.board.items():
            if(value == player):
                for neighbour in self.move_map[key]:
                    amount_moves +=1
        return amount_moves

    def own_mills_value(self, state, player):
        amount_mills = 0

        for mill in self.mills:
            if(all(state.board[position] == player for position in mill)): amount_mills +=1

        if(amount_mills>1): return 0.02
        if(amount_mills==1): return 0.01
        return 0
    
    def opponent_mills_value(self, state, player):
        opponent = 'b' if player == 'w' else 'w'
        return -self.own_mills_value(state, opponent)
    
    def own_open_mills_value(self, state, player):
        amount_open_mills = 0

        for mill in self.mills:
            open_mill = False
            empty_count = 0
            for piece in mill:
                if state.board[piece] == player: continue
                elif state.board[piece] == 'e':
                    empty_count += 1
                    if any(state.board[position] == player for position in self.move_map[piece]): open_mill = True
                else:
                    open_mill = False
                    break
            if open_mill and empty_count == 1: amount_open_mills += 1

        if amount_open_mills > 1: return 0.04
        elif amount_open_mills == 1: return 0.02
        return 0


    def opponent_open_mills_value(self, state, player):
        opponent = 'b' if player == 'w' else 'w'
        return -self.own_open_mills_value(state, opponent)
