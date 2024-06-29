# main.py

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black
GRID_SIZE = 40
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Solver')

# Load images
player_image = pygame.image.load('assets/player.png')
goal_image = pygame.image.load('assets/goal.png')

# Player and goal positions
player_position = [1, 1]
goal_position = [9, 9]

def draw_maze():
    for y, row in enumerate(MAZE):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_player():
    screen.blit(player_image, (player_position[0] * GRID_SIZE, player_position[1] * GRID_SIZE))

def draw_goal():
    screen.blit(goal_image, (goal_position[0] * GRID_SIZE, goal_position[1] * GRID_SIZE))

def move_player(dx, dy):
    new_x = player_position[0] + dx
    new_y = player_position[1] + dy
    if (0 <= new_x < len(MAZE[0])) and (0 <= new_y < len(MAZE)) and (MAZE[new_y][new_x] == 0):
        player_position[0] = new_x
        player_position[1] = new_y

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)
            elif event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)
    
    # Fill the background
    screen.fill(BACKGROUND_COLOR)
    
    # Draw the maze
    draw_maze()
    
    # Draw the goal
    draw_goal()
    
    # Draw the player
    draw_player()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
