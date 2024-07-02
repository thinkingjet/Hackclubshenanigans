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
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, -5, -30)
    glEnable(GL_DEPTH_TEST)

# Draw the ground model
def draw_ground():
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.6, 0.2)  # Green color for the ground
    glVertex3f(-50, 0, -50)
    glVertex3f(50, 0, -50)
    glVertex3f(50, 0, 50)
    glVertex3f(-50, 0, 50)
    glEnd()

# Draw the player model
def draw_player(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(0.8, 0.3, 0.3)  # Red color for the player
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 2, 1)
    glVertex3f(-1, 2, 1)
    # Back face
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 2, -1)
    glVertex3f(-1, 2, -1)
    # Left face
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 2, 1)
    glVertex3f(-1, 2, -1)
    # Right face
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 2, 1)
    glVertex3f(1, 2, -1)
    # Top face
    glVertex3f(-1, 2, -1)
    glVertex3f(1, 2, -1)
    glVertex3f(1, 2, 1)
    glVertex3f(-1, 2, 1)
    # Bottom face
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()
    glPopMatrix()

# Draw the arrow model
def draw_arrow(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(1, 0.5, 0)  # Orange color for the flaming arrow
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-0.1, 0, 0.5)
    glVertex3f(0.1, 0, 0.5)
    glVertex3f(0.1, 0.5, 0.5)
    glVertex3f(-0.1, 0.5, 0.5)
    # Back face
    glVertex3f(-0.1, 0, -0.5)
    glVertex3f(0.1, 0, -0.5)
    glVertex3f(0.1, 0.5, -0.5)
    glVertex3f(-0.1, 0.5, -0.5)
    # Left face
    glVertex3f(-0.1, 0, -0.5)
    glVertex3f(-0.1, 0, 0.5)
    glVertex3f(-0.1, 0.5, 0.5)
    glVertex3f(-0.1, 0.5, -0.5)
    # Right face
    glVertex3f(0.1, 0, -0.5)
    glVertex3f(0.1, 0, 0.5)
    glVertex3f(0.1, 0.5, 0.5)
    glVertex3f(0.1, 0.5, -0.5)
    # Top face
    glVertex3f(-0.1, 0.5, -0.5)
    glVertex3f(0.1, 0.5, -0.5)
    glVertex3f(0.1, 0.5, 0.5)
    glVertex3f(-0.1, 0.5, 0.5)
    # Bottom face
    glVertex3f(-0.1, 0, -0.5)
    glVertex3f(0.1, 0, -0.5)
    glVertex3f(0.1, 0, 0.5)
    glVertex3f(-0.1, 0, 0.5)
    glEnd()
    glPopMatrix()

def main():
    init()
    
    player_pos = [0, 0, 0]
    player_speed = 0.5
    arrows = []
    arrow_speed = 1.0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
        if keys[pygame.K_UP]:
            player_pos[2] -= player_speed
        if keys[pygame.K_DOWN]:
            player_pos[2] += player_speed
        if keys[pygame.K_SPACE]:
            arrows.append([player_pos[0], player_pos[1] + 1, player_pos[2]])

        # Move arrows
        for arrow in arrows:
            arrow[2] -= arrow_speed

        # Clear the screen and set up the perspective
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Update the camera position
        gluLookAt(
            0, 10, 30,
            0, 0, 0,
            0, 1, 0
        )
        
        # Draw the ground
        draw_ground()
        
        # Draw the player
        draw_player(player_pos[0], player_pos[1], player_pos[2])
        
        # Draw the arrows
        for arrow in arrows:
            draw_arrow(arrow[0], arrow[1], arrow[2])

        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
