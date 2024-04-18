from ninemensmorris import NineMensMorris

# W       W   III   PPPPPP 
# W       W    I    P     P
# W       W    I    PPPPPP 
# W   W   W    I    P      
# W   W   W    I    P      
#  W W W W     I    P      
#   W   W     III   P      

nmm = NineMensMorris(difficulty='easy', ai=True)
current_state = nmm.initial
while(nmm.terminal_test(current_state) is False):
    if(current_state.to_move == 'b'):
        # Implement Logic for Prompting Move here
        move = NotImplemented
    else:
        if(nmm.ai is False):
            # Same Logic to prompt Player 2 for move here
            move = NotImplemented
        else:
            move = nmm.get_best_move(state=current_state, player='w')

    current_state = nmm.result(state=current_state, move=move)
    
winner = nmm.get_winner(state=current_state)
print(f'{winner} won the Game!')