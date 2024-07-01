import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Initialize Pygame and OpenGL
def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, -1, -10)
    glEnable(GL_DEPTH_TEST)

# Define the vertices and edges of a cube
vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Create a simple maze layout
maze_layout = np.array([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
])

def draw_maze():
    for z, layer in enumerate(maze_layout):
        for x, value in enumerate(layer):
            if value == 1:
                glPushMatrix()
                glTranslatef(x * 2, 0, z * 2)
                draw_cube()
                glPopMatrix()

# Player position
player_pos = [2, 0, 2]

def draw_player():
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], player_pos[2])
    glColor3f(1, 0, 0)  # Red color for player
    draw_cube()
    glPopMatrix()

# Check for collisions
def can_move(x, z):
    if maze_layout[int(z / 2)][int(x / 2)] == 0:
        return True
    return False

# Main loop
def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if can_move(player_pos[0] - 0.1, player_pos[2]):
                player_pos[0] -= 0.1
        if keys[pygame.K_RIGHT]:
            if can_move(player_pos[0] + 0.1, player_pos[2]):
                player_pos[0] += 0.1
        if keys[pygame.K_UP]:
            if can_move(player_pos[0], player_pos[2] - 0.1):
                player_pos[2] -= 0.1
        if keys[pygame.K_DOWN]:
            if can_move(player_pos[0], player_pos[2] + 0.1):
                player_pos[2] += 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_maze()
        draw_player()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
