import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

def main():
    init()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
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

        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
