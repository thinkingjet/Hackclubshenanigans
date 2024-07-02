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

def main():
    init()
    
    player_pos = [0, 0, 0]
    player_speed = 0.5
    
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

        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
