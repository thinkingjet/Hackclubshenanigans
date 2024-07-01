import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

# Initialize Pygame and OpenGL
def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, -1, -10)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 1, 0])

# Load texture from file
def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", True)
    width, height = texture_surface.get_size()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return texture

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

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
)

def draw_cube(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glTexCoord2fv([(vertex % 2) * 1, ((vertex // 2) % 2) * 1])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Create a more complex maze layout
maze_layout = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Define start and end points
start_pos = [1, 0, 1]
end_pos = [7, 0, 5]

# Define obstacles and power-ups
obstacles = [[3, 0, 3], [5, 0, 1]]
power_ups = [[2, 0, 4], [6, 0, 2]]

def draw_maze(wall_texture):
    for z, layer in enumerate(maze_layout):
        for x, value in enumerate(layer):
            if value == 1:
                glPushMatrix()
                glTranslatef(x * 2, 0, z * 2)
                draw_cube(wall_texture)
                glPopMatrix()

# Player position
player_pos = start_pos.copy()
player_speed = 0.1

def draw_player(player_texture):
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], player_pos[2])
    glColor3f(1, 1, 1)  # White color for player with texture
    draw_cube(player_texture)
    glPopMatrix()

def draw_end_point():
    glPushMatrix()
    glTranslatef(end_pos[0], end_pos[1], end_pos[2])
    glColor3f(0, 1, 0)  # Green color for end point
    draw_cube(0)
    glPopMatrix()

def draw_obstacles():
    glColor3f(1, 0, 0)  # Red color for obstacles
    for obstacle in obstacles:
        glPushMatrix()
        glTranslatef(obstacle[0], obstacle[1], obstacle[2])
        draw_cube(0)
        glPopMatrix()

def draw_power_ups():
    glColor3f(0, 0, 1)  # Blue color for power-ups
    for power_up in power_ups:
        glPushMatrix()
        glTranslatef(power_up[0], power_up[1], power_up[2])
        draw_cube(0)
        glPopMatrix()

# Check for collisions
def can_move(x, z):
    if maze_layout[int(z / 2)][int(x / 2)] == 0:
        return True
    return False

def is_obstacle(x, z):
    return [x, 0, z] in obstacles

def is_power_up(x, z):
    return [x, 0, z] in power_ups

# Update the camera to follow the player
def update_camera():
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    gluLookAt(player_pos[0], player_pos[1] + 1, player_pos[2] + 5, player_pos[0], player_pos[1], player_pos[2], 0, 1, 0)

# Main loop
def main():
    init()
    wall_texture = load_texture('textures/wall_texture.png')
    player_texture = load_texture('textures/player_texture.png')
    score = 0
    start_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        new_pos = player_pos.copy()
        if keys[pygame.K_LEFT]:
            new_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            new_pos[0] += player_speed
        if keys[pygame.K_UP]:
            new_pos[2] -= player_speed
        if keys[pygame.K_DOWN]:
            new_pos[2] += player_speed

        if can_move(new_pos[0], new_pos[2]) and not is_obstacle(new_pos[0], new_pos[2]):
            player_pos = new_pos
            score += 1

        if is_power_up(player_pos[0], player_pos[2]):
            power_ups.remove([player_pos[0], 0, player_pos[2]])
            score += 10

        # Check if player reached the end
        if player_pos == end_pos:
            end_time = time.time()
            total_time = end_time - start_time
            print(f'Congratulations! You completed the maze with a score of {score} in {total_time:.2f} seconds!')
            pygame.quit()
            quit()

        update_camera()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_maze(wall_texture)
        draw_player(player_texture)
        draw_end_point()
        draw_obstacles()
        draw_power_ups()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
