import pygame
import sys
from ninemensmorris import NineMensMorris, GameState

# Initialize Pygame
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Nine Men's Morris")
game = NineMensMorris(ai=True)  # Ensure the AI is enabled
current_state = game.initial

# Constants for the board design
offset = 100
outer_square_size = 400
middle_square_size = 250
inner_square_size = 100
node_radius = 10  # Radius for the nodes
piece_radius = 20  # Radius for the game pieces

# Initialize game logic
game = NineMensMorris()
current_state = game.initial

# Define node positions based on square dimensions
nodes_positions = {
    'A1': (offset, offset),
    'D1': (offset + outer_square_size//2, offset),
    'G1': (offset + outer_square_size, offset),
    'B2': (offset + (outer_square_size - middle_square_size)//2, offset + (outer_square_size - middle_square_size)//2),
    'D2': (offset + outer_square_size//2, offset + (outer_square_size - middle_square_size)//2),
    'F2': (offset + outer_square_size - (outer_square_size - middle_square_size)//2, offset + (outer_square_size - middle_square_size)//2),
    'C3': (offset + (outer_square_size - inner_square_size)//2, offset + (outer_square_size - inner_square_size)//2),
    'D3': (offset + outer_square_size//2, offset + (outer_square_size - inner_square_size)//2),
    'E3': (offset + outer_square_size - (outer_square_size - inner_square_size)//2, offset + (outer_square_size - inner_square_size)//2),
    'A4': (offset, offset + outer_square_size//2),
    'B4': (offset + (outer_square_size - middle_square_size)//2, offset + outer_square_size//2),
    'C4': (offset + (outer_square_size - inner_square_size)//2, offset + outer_square_size//2),
    'E4': (offset + outer_square_size - (outer_square_size - inner_square_size)//2, offset + outer_square_size//2),
    'F4': (offset + outer_square_size - (outer_square_size - middle_square_size)//2, offset + outer_square_size//2),
    'G4': (offset + outer_square_size, offset + outer_square_size//2),
    'C5': (offset + (outer_square_size - inner_square_size)//2, offset + outer_square_size - (outer_square_size - inner_square_size)//2),
    'D5': (offset + outer_square_size//2, offset + outer_square_size - (outer_square_size - inner_square_size)//2),
    'E5': (offset + outer_square_size - (outer_square_size - inner_square_size)//2, offset + outer_square_size - (outer_square_size - inner_square_size)//2),
    'B6': (offset + (outer_square_size - middle_square_size)//2, offset + outer_square_size - (outer_square_size - middle_square_size)//2),
    'D6': (offset + outer_square_size//2, offset + outer_square_size - (outer_square_size - middle_square_size)//2),
    'F6': (offset + outer_square_size - (outer_square_size - middle_square_size)//2, offset + outer_square_size - (outer_square_size - middle_square_size)//2),
    'A7': (offset, offset + outer_square_size),
    'D7': (offset + outer_square_size//2, offset + outer_square_size),
    'G7': (offset + outer_square_size, offset + outer_square_size)
}

# Create a reverse dictionary to map positions to nodes for game logic integration
nodes = {v: k for k, v in nodes_positions.items()}

selected_piece = None

# Function to draw the squares and connecting lines
def draw_board():
    screen.fill((255, 255, 255))  # Clear screen and fill with white
    # Outer square
    pygame.draw.rect(screen, (0, 0, 0), (offset, offset, outer_square_size, outer_square_size), 3)
    # Middle square
    pygame.draw.rect(screen, (0, 0, 0), (offset + (outer_square_size - middle_square_size)//2, offset + (outer_square_size - middle_square_size)//2, middle_square_size, middle_square_size), 3)
    # Inner square
    pygame.draw.rect(screen, (0, 0, 0), (offset + (outer_square_size - inner_square_size)//2, offset + (outer_square_size - inner_square_size)//2, inner_square_size, inner_square_size), 3)
    
    # Vertical connecting lines
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['D1'], nodes_positions['D2'], 3)
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['D2'], nodes_positions['D3'], 3)
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['D6'], nodes_positions['D5'], 3)
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['D5'], nodes_positions['D7'], 3)
    
    # Horizontal connecting lines
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['A4'], nodes_positions['B4'], 3)
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['B4'], nodes_positions['C4'], 3)
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['E4'], nodes_positions['F4'], 3)
    pygame.draw.line(screen, (0, 0, 0), nodes_positions['F4'], nodes_positions['G4'], 3)

# Function to draw nodes
def draw_nodes():
    for pos in nodes_positions.values():
        pygame.draw.circle(screen, (0, 255, 0), pos, node_radius)  # Draw green node circles

# Function to draw pieces on the board
def draw_pieces():
    for pos, state in current_state.board.items():
        if state == 'b':
            pygame.draw.circle(screen, (0, 0, 0), nodes_positions[pos], piece_radius)  # Black for 'b'
        elif state == 'w':
            pygame.draw.circle(screen, (255, 0, 0), nodes_positions[pos], piece_radius)  # Red for 'w'

def display_message(message):
    font = pygame.font.Font(None, 36)  # You can adjust the font size here
    text = font.render(message, True, (255, 0, 0))  # Render the message in red
    text_rect = text.get_rect(center=(size[0] // 2, 50))  # Position the text at the top of the screen
    screen.fill((0, 0, 0), (0, 0, size[0], 100))  # Clear the area where the text is displayed
    screen.blit(text, text_rect)
    pygame.display.update(text_rect)  # Update only the part of the screen with the text
    pygame.time.wait(3000)  # Display the message for 3 seconds




# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if current_state.move_type == 'jump':
                if selected_piece:
                    # Allow the player to place the selected piece in any empty spot
                    for node_key, node_pos in nodes_positions.items():
                        if (node_pos[0] - node_radius < pos[0] < node_pos[0] + node_radius) and (node_pos[1] - node_radius < pos[1] < node_pos[1] + node_radius):
                            if current_state.board[node_key] == 'e':  # Check if spot is empty
                                move = (selected_piece, node_key)
                                print(f"Jumping piece from {selected_piece} to {node_key}")
                                current_state = game.result(current_state, move)
                                selected_piece = None  # Deselect after jumping
                                break
                else:
                    # Select a piece to jump
                    for node_key, node_pos in nodes_positions.items():
                        if (node_pos[0] - node_radius < pos[0] < node_pos[0] + node_radius) and (node_pos[1] - node_radius < pos[1] < node_pos[1] + node_radius):
                            if current_state.board[node_key] == current_state.to_move:
                                selected_piece = node_key
                                print(f"Selected piece at {selected_piece} for jumping")
                                break
            elif current_state.move_type == 'take':
                # Allow the player to remove an opponent's piece
                for node_key, node_pos in nodes_positions.items():
                    if (node_pos[0] - node_radius < pos[0] < node_pos[0] + node_radius) and (node_pos[1] - node_radius < pos[1] < node_pos[1] + node_radius):
                        if node_key in [action for action in game.actions(current_state)]:
                            print(f"Taking piece at: {node_key}")
                            current_state = game.result(current_state, node_key)
                            selected_piece = None  # Clear selection after taking a piece
                            break
            elif current_state.move_type == 'set':
                # Handle setting pieces
                for node_key, node_pos in nodes_positions.items():
                    if (node_pos[0] - node_radius < pos[0] < node_pos[0] + node_radius) and (node_pos[1] - node_radius < pos[1] < node_pos[1] + node_radius):
                        if node_key in [action for action in game.actions(current_state)]:
                            print(f"Placing piece at: {node_key}")
                            current_state = game.result(current_state, node_key)
                            break
            elif current_state.move_type == 'move':
                # Handle moving pieces
                if selected_piece:
                    for node_key, node_pos in nodes_positions.items():
                        if (node_pos[0] - node_radius < pos[0] < node_pos[0] + node_radius) and (node_pos[1] - node_radius < pos[1] < node_pos[1] + node_radius):
                            move = (selected_piece, node_key)
                            if move in [action for action in game.actions(current_state)]:
                                print(f"Moving piece from {selected_piece} to {node_key}")
                                current_state = game.result(current_state, move)
                                selected_piece = None  # Deselect after moving
                            break
                else:
                    for node_key, node_pos in nodes_positions.items():
                        if (node_pos[0] - node_radius < pos[0] < node_pos[0] + node_radius) and (node_pos[1] - node_radius < pos[1] < node_pos[1] + node_radius):
                            if current_state.board[node_key] == current_state.to_move:
                                selected_piece = node_key
                                print(f"Selected piece at {selected_piece} for moving")
                                break
                                
    # AI Move
    if current_state.to_move == 'w' and not game.terminal_test(current_state):
        ai_move = game.get_best_move(current_state, 'w')
        current_state = game.result(current_state, ai_move)

        print(f"AI moved to: {ai_move}")
        print(f"New game state: {current_state}")
        print(f"Available moves: {game.actions(current_state)}")
    
    if game.terminal_test(current_state):
        winner = game.get_winner(current_state)
        display_message(f"{winner} wins the game!")
        pygame.time.wait(3000)  # Give some time to read the message
        running = False

    draw_board()
    draw_nodes()
    draw_pieces()
    pygame.display.flip()

pygame.quit()
sys.exit()
