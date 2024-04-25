import pygame
import sys


pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Nine Men's Morris")


outer_square_size = 400
middle_square_size = 250
inner_square_size = 100
offset = 100  


def draw_square(screen, top_left_x, top_left_y, size):
    pygame.draw.rect(screen, (0, 0, 0), (top_left_x, top_left_y, size, size), 3)


def draw_connecting_lines(screen, outer, middle, inner):
    
    points = [
        ((outer[0] + outer[2] // 2, outer[1]), (inner[0] + inner[2] // 2, inner[1])),  # Top vertical
        ((outer[0] + outer[2], outer[1] + outer[3] // 2), (inner[0] + inner[2], inner[1] + inner[3] // 2)),  # Right horizontal
        ((outer[0] + outer[2] // 2, outer[1] + outer[3]), (inner[0] + inner[2] // 2, inner[1] + inner[3])),  # Bottom vertical
        ((outer[0], outer[1] + outer[3] // 2), (inner[0], inner[1] + inner[3] // 2))  # Left horizontal
    ]
    for point1, point2 in points:
        pygame.draw.line(screen, (0, 0, 0), point1, point2, 3)


def draw_board(screen):
    outer_top_left = (offset, offset)
    middle_top_left = ((outer_square_size - middle_square_size) // 2 + offset,
                       (outer_square_size - middle_square_size) // 2 + offset)
    inner_top_left = ((outer_square_size - inner_square_size) // 2 + offset,
                      (outer_square_size - inner_square_size) // 2 + offset)
    
    
    draw_square(screen, *outer_top_left, outer_square_size)
    draw_square(screen, *middle_top_left, middle_square_size)
    draw_square(screen, *inner_top_left, inner_square_size)

    
    draw_connecting_lines(screen, (offset, offset, outer_square_size, outer_square_size),
                          (middle_top_left[0], middle_top_left[1], middle_square_size, middle_square_size),
                          (inner_top_left[0], inner_top_left[1], inner_square_size, inner_square_size))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  
    draw_board(screen)  
    pygame.display.update()  
