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
    
   # Update the main game loop
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
        for target in targets:
            if check_collision(arrow, target):
                score += 10
                targets.remove(target)
                arrows.remove(arrow)
                break

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
    
    # Draw the targets
    for target in targets:
        draw_target(target[0], target[1], target[2])
    
    # Draw the score
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    score_surface = pygame.image.fromstring(score_text.tobytes(), score_text.get_size(), score_text.get_mode())
    screen = pygame.display.get_surface()
    screen.blit(score_surface, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)

# Draw the target model
def draw_target(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(0, 0, 1)  # Blue color for the target
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
# Main function variables
targets = [
    [10, 0, -50],
    [-10, 0, -70],
    [15, 0, -90]
]
score = 0
font = pygame.font.SysFont('Arial', 25)
# Collision detection function
def check_collision(arrow, target):
    return (
        target[0] - 1 <= arrow[0] <= target[0] + 1 and
        target[1] <= arrow[1] <= target[1] + 2 and
        target[2] - 1 <= arrow[2] <= target[2] + 1
    )


# Draw the arrow model with rotation
def draw_arrow(x, y, z, angle):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(angle, 1, 0, 0)
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

arrows = []
arrow_speed = 1.0
arrow_rotation_speed = 10.0
# Update the main game loop
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
        arrows.append([player_pos[0], player_pos[1] + 1, player_pos[2], 0])

    # Move and rotate arrows
    for arrow in arrows:
        arrow[2] -= arrow_speed
        arrow[3] += arrow_rotation_speed
        for target in targets:
            if check_collision(arrow, target):
                score += 10
                targets.remove(target)
                arrows.remove(arrow)
                break

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
        draw_arrow(arrow[0], arrow[1], arrow[2], arrow[3])
    
    # Draw the targets
    for target in targets:
        draw_target(target[0], target[1], target[2])
    
    # Draw the score
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    score_surface = pygame.image.fromstring(score_text.tobytes(), score_text.get_size(), score_text.get_mode())
    screen = pygame.display.get_surface()
    screen.blit(score_surface, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)


if __name__ == "__main__":
    main()
