import sys
sys.path.append('..')
from ninemensmorris import *

def Test_States():
    return [
        # Base State
        # GameState(
        #     board={'A1':'e', 'D1':'e', 'G1':'e', 'B2':'e', 'D2':'e', 'F2':'e', 'C3':'e', 'D3':'e', 'E3':'e', 'A4':'e', 'B4':'e', 'C4':'e', 'E4':'e', 'F4':'e', 'G4':'e', 'C5':'e', 'D5':'e', 'E5':'e', 'B6':'e', 'D6':'e', 'F6':'e', 'A7':'e', 'D7':'e', 'G7':'e'},
        #     to_move='b',
        #     move_type='set',
        #     pieces_b=9,
        #     pieces_w=9),

        # Move States 18 Pieces

        GameState(
            board={'C4': 'b', 'F4': 'b', 'G4': 'b', 'A4': 'b', 'D7': 'b', 'A7': 'b', 'B4': 'b', 'D3': 'b', 'C3': 'b', 'A1': 'w', 'B2': 'w', 'G1': 'w', 'B6': 'w', 'D1': 'w', 'D2': 'w', 'G7': 'w', 'F6': 'w', 'C5': 'w', 'D6': 'e', 'E5': 'e', 'D5': 'e', 'E3': 'e', 'E4': 'e', 'F2': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'D7': 'b', 'F6': 'b', 'F4': 'b', 'C3': 'b', 'E5': 'b', 'B6': 'b', 'C4': 'b', 'D6': 'b', 'E4': 'b', 'D5': 'w', 'C5': 'w', 'E3': 'w', 'G4': 'w', 'D1': 'w', 'G7': 'w', 'A4': 'w', 'A7': 'w', 'B4': 'w', 'F2': 'e', 'A1': 'e', 'D3': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'e'},
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'F6': 'b', 'G4': 'b', 'E5': 'b', 'B4': 'b', 'D7': 'b', 'B2': 'b', 'D2': 'b', 'D6': 'b', 'E3': 'b', 'B6': 'w', 'D5': 'w', 'C4': 'w', 'F4': 'w', 'D3': 'w', 'A4': 'w', 'D1': 'w', 'G7': 'w', 'G1': 'w', 'E4': 'e', 'C3': 'e', 'A7': 'e', 'A1': 'e', 'F2': 'e', 'C5': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'F2': 'b', 'E4': 'b', 'D7': 'b', 'D6': 'b', 'F6': 'b', 'G4': 'b', 'A7': 'b', 'B6': 'b', 'C4': 'b', 'F4': 'w', 'A4': 'w', 'D2': 'w', 'D1': 'w', 'D3': 'w', 'B2': 'w', 'A1': 'w', 'D5': 'w', 'G7': 'w', 'C5': 'e', 'B4': 'e', 'C3': 'e', 'E3': 'e', 'E5': 'e', 'G1': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'E3': 'b', 'D7': 'b', 'C3': 'b', 'G1': 'b', 'A1': 'b', 'D5': 'b', 'A4': 'b', 'C4': 'b', 'E5': 'b', 'A7': 'w', 'B2': 'w', 'D2': 'w', 'G4': 'w', 'C5': 'w', 'F4': 'w', 'D3': 'w', 'E4': 'w', 'F6': 'w', 'B4': 'e', 'G7': 'e', 'D1': 'e', 'F2': 'e', 'B6': 'e', 'D6': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A4': 'b', 'B6': 'b', 'G7': 'b', 'D7': 'b', 'D6': 'b', 'C5': 'b', 'E3': 'b', 'D3': 'b', 'E5': 'b', 'C3': 'w', 'A1': 'w', 'D2': 'w', 'E4': 'w', 'F6': 'w', 'F4': 'w', 'C4': 'w', 'B2': 'w', 'D1': 'w', 'A7': 'e', 'G1': 'e', 'G4': 'e', 'D5': 'e', 'F2': 'e', 'B4': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'C5': 'b', 'D5': 'b', 'E5': 'b', 'D1': 'b', 'B4': 'b', 'G4': 'b', 'F2': 'b', 'C4': 'b', 'E4': 'b', 'E3': 'w', 'G7': 'w', 'D3': 'w', 'D6': 'w', 'D7': 'w', 'C3': 'w', 'D2': 'w', 'A7': 'w', 'G1': 'w', 'B2': 'e', 'A4': 'e', 'A1': 'e', 'F6': 'e', 'B6': 'e', 'F4': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'G4': 'b', 'D3': 'b', 'E5': 'b', 'C4': 'b', 'C3': 'b', 'B2': 'b', 'D7': 'b', 'D1': 'b', 'B6': 'b', 'E3': 'w', 'F4': 'w', 'D6': 'w', 'E4': 'w', 'A7': 'w', 'D5': 'w', 'G1': 'w', 'A1': 'w', 'G7': 'w', 'F6': 'e', 'F2': 'e', 'C5': 'e', 'D2': 'e', 'A4': 'e', 'B4': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'E3': 'b', 'B6': 'b', 'A7': 'b', 'G4': 'b', 'G1': 'b', 'E4': 'b', 'F6': 'b', 'A4': 'b', 'D5': 'b', 'C3': 'w', 'D6': 'w', 'A1': 'w', 'G7': 'w', 'D2': 'w', 'B2': 'w', 'F4': 'w', 'E5': 'w', 'C4': 'w', 'C5': 'e', 'B4': 'e', 'D7': 'e', 'D3': 'e', 'D1': 'e', 'F2': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'F6': 'b', 'D3': 'b', 'D5': 'b', 'A4': 'b', 'A1': 'b', 'B2': 'b', 'G4': 'b', 'D1': 'b', 'A7': 'b', 'E5': 'w', 'C3': 'w', 'E3': 'w', 'D7': 'w', 'G7': 'w', 'G1': 'w', 'D6': 'w', 'B6': 'w', 'E4': 'w', 'F4': 'e', 'B4': 'e', 'D2': 'e', 'C5': 'e', 'C4': 'e', 'F2': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),

        # Move States Random Pieces

        GameState(
            board={'A1': 'b', 'D1': 'b', 'G1': 'b', 'B2': 'w', 'D2': 'w', 'F2': 'e', 'C3': 'w', 'D3': 'e', 'E3': 'w', 'A4': 'w', 'B4': 'e', 'C4': 'e', 'E4': 'e', 'F4': 'b', 'G4': 'w', 'C5': 'e', 'D5': 'w', 'E5': 'b', 'B6': 'w', 'D6': 'b', 'F6': 'w', 'A7': 'e', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'e', 'D1': 'b', 'G1': 'e', 'B2': 'b', 'D2': 'w', 'F2': 'w', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'e', 'E4': 'b', 'F4': 'e', 'G4': 'e', 'C5': 'w', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'e', 'F6': 'w', 'A7': 'b', 'D7': 'e', 'G7': 'b'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'e', 'F2': 'b', 'C3': 'b', 'D3': 'e', 'E3': 'e', 'A4': 'b', 'B4': 'w', 'C4': 'b', 'E4': 'e', 'F4': 'e', 'G4': 'e', 'C5': 'w', 'D5': 'e', 'E5': 'w', 'B6': 'w', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'w', 'G7': 'b'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'w', 'D1': 'w', 'G1': 'e', 'B2': 'w', 'D2': 'e', 'F2': 'e', 'C3': 'b', 'D3': 'b', 'E3': 'w', 'A4': 'w', 'B4': 'w', 'C4': 'e', 'E4': 'b', 'F4': 'w', 'G4': 'e', 'C5': 'e', 'D5': 'b', 'E5': 'w', 'B6': 'e', 'D6': 'e', 'F6': 'e', 'A7': 'w', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'e', 'D1': 'w', 'G1': 'b', 'B2': 'w', 'D2': 'e', 'F2': 'w', 'C3': 'e', 'D3': 'e', 'E3': 'w', 'A4': 'w', 'B4': 'e', 'C4': 'b', 'E4': 'b', 'F4': 'e', 'G4': 'e', 'C5': 'e', 'D5': 'b', 'E5': 'w', 'B6': 'e', 'D6': 'b', 'F6': 'b', 'A7': 'e', 'D7': 'b', 'G7': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'b', 'D1': 'b', 'G1': 'e', 'B2': 'w', 'D2': 'e', 'F2': 'e', 'C3': 'b', 'D3': 'w', 'E3': 'b', 'A4': 'b', 'B4': 'e', 'C4': 'e', 'E4': 'b', 'F4': 'e', 'G4': 'e', 'C5': 'b', 'D5': 'w', 'E5': 'w', 'B6': 'b', 'D6': 'b', 'F6': 'e', 'A7': 'w', 'D7': 'w', 'G7': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'b', 'D2': 'e', 'F2': 'b', 'C3': 'w', 'D3': 'b', 'E3': 'w', 'A4': 'b', 'B4': 'w', 'C4': 'b', 'E4': 'w', 'F4': 'b', 'G4': 'b', 'C5': 'e', 'D5': 'w', 'E5': 'w', 'B6': 'w', 'D6': 'w', 'F6': 'e', 'A7': 'w', 'D7': 'e', 'G7': 'b'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'e', 'D1': 'b', 'G1': 'e', 'B2': 'e', 'D2': 'e', 'F2': 'e', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'b', 'E4': 'e', 'F4': 'w', 'G4': 'e', 'C5': 'e', 'D5': 'w', 'E5': 'e', 'B6': 'b', 'D6': 'e', 'F6': 'b', 'A7': 'w', 'D7': 'w', 'G7': 'e'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'b', 'D1': 'e', 'G1': 'e', 'B2': 'b', 'D2': 'b', 'F2': 'w', 'C3': 'e', 'D3': 'e', 'E3': 'w', 'A4': 'e', 'B4': 'e', 'C4': 'w', 'E4': 'e', 'F4': 'w', 'G4': 'e', 'C5': 'e', 'D5': 'w', 'E5': 'b', 'B6': 'b', 'D6': 'e', 'F6': 'w', 'A7': 'e', 'D7': 'w', 'G7': 'w'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),
        GameState(
            board={'A1': 'e', 'D1': 'w', 'G1': 'w', 'B2': 'b', 'D2': 'e', 'F2': 'b', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'b', 'E4': 'e', 'F4': 'w', 'G4': 'b', 'C5': 'e', 'D5': 'e', 'E5': 'b', 'B6': 'b', 'D6': 'e', 'F6': 'w', 'A7': 'b', 'D7': 'e', 'G7': 'w'},
            to_move='b',
            move_type='move',
            pieces_b=0,
            pieces_w=0),

        # Set States Random Pieces

        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'e', 'F2': 'e', 'C3': 'b', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'e', 'E4': 'e', 'F4': 'e', 'G4': 'e', 'C5': 'w', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='set',
            pieces_b=8,
            pieces_w=8),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'e', 'F2': 'e', 'C3': 'b', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'e', 'E4': 'e', 'F4': 'e', 'G4': 'e', 'C5': 'e', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'w', 'F6': 'e', 'A7': 'e', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='set',
            pieces_b=8,
            pieces_w=8),
        GameState(
            board={'A1': 'w', 'D1': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'b', 'F2': 'e', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'b', 'B4': 'e', 'C4': 'w', 'E4': 'w', 'F4': 'e', 'G4': 'w', 'C5': 'e', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'b', 'F6': 'e', 'A7': 'b', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='set',
            pieces_b=5,
            pieces_w=5),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'b', 'D2': 'b', 'F2': 'e', 'C3': 'e', 'D3': 'w', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'e', 'E4': 'e', 'F4': 'e', 'G4': 'e', 'C5': 'e', 'D5': 'w', 'E5': 'e', 'B6': 'e', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='set',
            pieces_b=7,
            pieces_w=7),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'e', 'F2': 'e', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'e', 'E4': 'w', 'F4': 'e', 'G4': 'e', 'C5': 'b', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='set',
            pieces_b=8,
            pieces_w=8),
        GameState(
            board={'A1': 'w', 'D1': 'e', 'G1': 'w', 'B2': 'b', 'D2': 'w', 'F2': 'e', 'C3': 'w', 'D3': 'e', 'E3': 'e', 'A4': 'b', 'B4': 'e', 'C4': 'b', 'E4': 'b', 'F4': 'e', 'G4': 'e', 'C5': 'w', 'D5': 'b', 'E5': 'b', 'B6': 'w', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='set',
            pieces_b=3,
            pieces_w=3),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'e', 'F2': 'e', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'e', 'E4': 'e', 'F4': 'e', 'G4': 'w', 'C5': 'e', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'e', 'G7': 'b'},
            to_move='b',
            move_type='set',
            pieces_b=8,
            pieces_w=8),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'w', 'B2': 'e', 'D2': 'e', 'F2': 'e', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'e', 'C4': 'e', 'E4': 'e', 'F4': 'e', 'G4': 'e', 'C5': 'e', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'e', 'G7': 'b'},
            to_move='b',
            move_type='set',
            pieces_b=8,
            pieces_w=8),
        GameState(
            board={'A1': 'e', 'D1': 'b', 'G1': 'e', 'B2': 'w', 'D2': 'e', 'F2': 'b', 'C3': 'e', 'D3': 'e', 'E3': 'e', 'A4': 'e', 'B4': 'b', 'C4': 'e', 'E4': 'b', 'F4': 'w', 'G4': 'e', 'C5': 'e', 'D5': 'b', 'E5': 'w', 'B6': 'w', 'D6': 'w', 'F6': 'w', 'A7': 'b', 'D7': 'e', 'G7': 'e'},
            to_move='b',
            move_type='set',
            pieces_b=3,
            pieces_w=3),
        GameState(
            board={'A1': 'e', 'D1': 'e', 'G1': 'e', 'B2': 'e', 'D2': 'b', 'F2': 'e', 'C3': 'w', 'D3': 'e', 'E3': 'e', 'A4': 'b', 'B4': 'e', 'C4': 'e', 'E4': 'e', 'F4': 'e', 'G4': 'e', 'C5': 'b', 'D5': 'e', 'E5': 'e', 'B6': 'e', 'D6': 'e', 'F6': 'e', 'A7': 'e', 'D7': 'w', 'G7': 'w'},
            to_move='b',
            move_type='set',
            pieces_b=6,
            pieces_w=6)
    ]

 