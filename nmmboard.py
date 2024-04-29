import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Nine Men's Morris")

# Constants for the board design
outer_square_size = 400
middle_square_size = 250
inner_square_size = 100
offset = 100  # Offset from the edge of the window
node_radius = 10  # Radius for the nodes
piece_radius = 15  # Radius for the game pieces

# Function to draw the squares
def draw_square(screen, top_left_x, top_left_y, size):
    pygame.draw.rect(screen, (0, 0, 0), (top_left_x, top_left_y, size, size), 3)

# Function to draw connecting lines between squares
def draw_connecting_lines(screen):
    midpoints = [
        (size[0]//2, offset),  # Top
        (size[0]//2, size[1]-offset),  # Bottom
        (offset, size[1]//2),  # Left
        (size[0]-offset, size[1]//2)  # Right
    ]
    inner_midpoints = [
        (size[0]//2, offset + (outer_square_size - inner_square_size) // 2),  # Top
        (size[0]//2, size[1] - offset - (outer_square_size - inner_square_size) // 2),  # Bottom
        (offset + (outer_square_size - inner_square_size) // 2, size[1]//2),  # Left
        (size[0] - offset - (outer_square_size - inner_square_size) // 2, size[1]//2)  # Right
    ]
    for i in range(4):
        pygame.draw.line(screen, (0, 0, 0), midpoints[i], inner_midpoints[i], 3)

nodes = []
square_sizes = [outer_square_size, middle_square_size, inner_square_size]
for i, square_size in enumerate(square_sizes):
    top_left_x = (size[0] - square_size) // 2
    top_left_y = (size[1] - square_size) // 2
    step = square_size // 2
    for x in range(3):
        for y in range(3):
            if not (x == 1 and y == 1):  
                node_x = top_left_x + x * step
                node_y = top_left_y + y * step
                nodes.append((node_x, node_y))

node_states = {node: 0 for node in nodes}

# Function to draw nodes
def draw_nodes(screen, nodes):
    for node in nodes:
        pygame.draw.circle(screen, (0, 255, 0), node, node_radius)

# Function to draw game pieces
def draw_pieces(screen, node_states):
    for node, state in node_states.items():
        if state == 1:
            pygame.draw.circle(screen, (0, 0, 0), node, piece_radius)
        elif state == 2:
            pygame.draw.circle(screen, (255, 0, 0), node, piece_radius)

# Function to place a random piece for the computer (User 2)
def place_random_piece(node_states):
    empty_nodes = [node for node, state in node_states.items() if state == 0]
    if empty_nodes:
        chosen_node = random.choice(empty_nodes)
        node_states[chosen_node] = 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for node in nodes:
                if node_states[node] == 0 and (node[0] - node_radius < mouse_pos[0] < node[0] + node_radius) and \
                   (node[1] - node_radius < mouse_pos[1] < node[1] + node_radius):
                    node_states[node] = 1
                    place_random_piece(node_states)
                    break

    screen.fill((255, 255, 255))  # Clear screen and fill with white
    for square_size in square_sizes:
        top_left_x = (size[0] - square_size) // 2
        top_left_y = (size[1] - square_size) // 2
        draw_square(screen, top_left_x, top_left_y, square_size)
    draw_connecting_lines(screen)
    draw_nodes(screen, nodes)  # Draw nodes on the board
    draw_pieces(screen, node_states)  # Draw game pieces
    pygame.display.update()  # Update the display
