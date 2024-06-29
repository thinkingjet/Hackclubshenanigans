# main.py

import pygame
import sys
import heapq

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

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heapq.heappop(oheap)[1]
        
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data
        
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1
            if 0 <= neighbor[0] < len(maze):
                if 0 <= neighbor[1] < len(maze[0]):
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue
            
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
            
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
    
    return False

# Find path from player to goal
path = astar(MAZE, tuple(player_position), tuple(goal_position))

def draw_path(path):
    if path:
        for position in path:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(position[1] * GRID_SIZE, position[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

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
    
    # Draw the path
    draw_path(path)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
