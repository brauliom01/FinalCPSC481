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

menu_open = False
menu_items = ["Resume", "Restart", "Difficulty: Easy", "Quit"]
menu_item_selected = None

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

    font = pygame.font.Font(None, 36)  # You can adjust the font size here
    title_text = font.render("Nine Men's Morris", True, (0, 0, 0))  # Render the title in black
    title_rect = title_text.get_rect(center=(size[0] // 2, size[1] - 30))  # Position the text at the bottom of the screen
    screen.blit(title_text, title_rect)
    
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


def draw_counters():
    # Assuming 9 pieces at the start for each player as per standard Nine Men's Morris rules
    remaining_black = 9 - sum(1 for pos in current_state.board.values() if pos == 'b')
    remaining_white = 9 - sum(1 for pos in current_state.board.values() if pos == 'w')
    font = pygame.font.Font(None, 24)  # Adjust font size as needed

    # Render black pieces counter
    black_text = font.render(f"Black pieces left: {remaining_black}", True, (0, 0, 0))
    black_rect = black_text.get_rect(topright=(size[0] - 10, 10))
    screen.blit(black_text, black_rect)

    # Render white pieces counter
    white_text = font.render(f"White pieces left: {remaining_white}", True, (255, 255, 255))
    white_rect = white_text.get_rect(topleft=(10, 10))
    screen.blit(white_text, white_rect)

def draw_settings_button():
    button_rect = pygame.Rect(10, 10, 40, 40)
    pygame.draw.rect(screen, (200, 200, 200), button_rect)
    line_y_offsets = [15, 25, 35]
    for offset in line_y_offsets:
        pygame.draw.line(screen, (0, 0, 0), (15, 10 + offset), (35, 10 + offset), 3)
    return button_rect

def draw_dropdown():
    if menu_open:
        base_height = 55
        for index, item in enumerate(menu_items):
            item_rect = pygame.Rect(10, base_height + 30 * index, 140, 30)
            pygame.draw.rect(screen, (200, 200, 200), item_rect)
            font = pygame.font.Font(None, 24)
            text = font.render(item, True, (0, 0, 0))
            text_rect = text.get_rect(center=item_rect.center)
            screen.blit(text, text_rect)

def handle_menu_selection(index):
    global menu_open, current_state
    selection = menu_items[index]
    if selection == "Resume":
        menu_open = False
    elif selection == "Restart":
        current_state = game.initial
        menu_open = False
    elif "Difficulty" in selection:
        if "Easy" in selection:
            menu_items[index] = "Difficulty: Hard"
        else:
            menu_items[index] = "Difficulty: Easy"
    elif selection == "Quit":
        pygame.quit()
        sys.exit()

settings_button_rect = draw_settings_button()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if settings_button_rect.collidepoint(pos):
                menu_open = not menu_open
            elif menu_open:  # Check if the click is within the menu area when the menu is open
                base_height = 55
                for index, item in enumerate(menu_items):
                    item_rect = pygame.Rect(10, base_height + 30 * index, 140, 30)
                    if item_rect.collidepoint(pos):  # Check if the click is on this menu item
                        handle_menu_selection(index)
                        break

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
        elif event.type == pygame.MOUSEBUTTONUP:
            if menu_open:
                draw_dropdown()
                                
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
    draw_counters()
    settings_button_rect = draw_settings_button()
    draw_dropdown()
    pygame.display.flip()

pygame.quit()
sys.exit()
