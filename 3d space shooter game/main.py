import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Initialize Pygame and OpenGL
def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -30)
    glEnable(GL_DEPTH_TEST)

# Define a simple spaceship model
def draw_spaceship():
    glBegin(GL_TRIANGLES)
    
    # Body of the spaceship
    glColor3f(0.5, 0.5, 1.0)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)

    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)

    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)

    glEnd()

    glBegin(GL_QUADS)
    
    # Bottom of the spaceship
    glColor3f(0.3, 0.3, 0.6)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    
    glEnd()

# Define the background
def draw_background():
    glBegin(GL_QUADS)
    
    glColor3f(0, 0, 0)  # Black background
    glVertex3f(-50, -50, -100)
    glVertex3f(50, -50, -100)
    glVertex3f(50, 50, -100)
    glVertex3f(-50, 50, -100)
    
    glEnd()

# Main loop
def main():
    init()
    
    spaceship_pos = [0, 0, 0]
    spaceship_speed = 0.5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship_pos[0] -= spaceship_speed
        if keys[pygame.K_RIGHT]:
            spaceship_pos[0] += spaceship_speed
        if keys[pygame.K_UP]:
            spaceship_pos[2] += spaceship_speed
        if keys[pygame.K_DOWN]:
            spaceship_pos[2] -= spaceship_speed
        
        # Clear the screen and set up the perspective
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Update the camera to follow the spaceship
        gluLookAt(
            spaceship_pos[0], spaceship_pos[1] + 5, spaceship_pos[2] + 10,
            spaceship_pos[0], spaceship_pos[1], spaceship_pos[2],
            0, 1, 0
        )
        
        # Draw the background
        draw_background()
        
        # Draw the spaceship
        glPushMatrix()
        glTranslatef(spaceship_pos[0], spaceship_pos[1], spaceship_pos[2])
        draw_spaceship()
        glPopMatrix()
        
        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
