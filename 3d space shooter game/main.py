import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

# Initialize Pygame and OpenGL
def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -30)
    glEnable(GL_DEPTH_TEST)
    pygame.font.init()

# Draw the spaceship model
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

class Spaceship:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.bullets = []
        self.health = 100

    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        draw_spaceship()
        glPopMatrix()
        
        # Draw bullets
        for bullet in self.bullets:
            bullet.draw()

    def move(self, dx, dy, dz):
        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def shoot(self):
        bullet = Bullet(self.pos[0], self.pos[1], self.pos[2])
        self.bullets.append(bullet)

class Bullet:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.speed = 1.0

    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glColor3f(1, 0, 0)
        glutSolidSphere(0.1, 10, 10)
        glPopMatrix()

    def move(self):
        self.pos[2] -= self.speed

    def is_off_screen(self):
        return self.pos[2] < -50

class Enemy:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.health = 3

    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glColor3f(1, 0, 0)
        glutSolidCube(1)
        glPopMatrix()

    def move(self):
        self.pos[2] += 0.1

    def is_off_screen(self):
        return self.pos[2] > 10

def render_text(text, pos):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(*pos, 0)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def main():
    init()

    spaceship = Spaceship(0, 0, 0)
    enemies = [Enemy(random.uniform(-5, 5), 0, random.uniform(-50, -10)) for _ in range(5)]
    spaceship_speed = 0.5
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                spaceship.shoot()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship.move(-spaceship_speed, 0, 0)
        if keys[pygame.K_RIGHT]:
            spaceship.move(spaceship_speed, 0, 0)
        if keys[pygame.K_UP]:
            spaceship.move(0, 0, spaceship_speed)
        if keys[pygame.K_DOWN]:
            spaceship.move(0, 0, -spaceship_speed)
        
        # Clear the screen and set up the perspective
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Update the camera to follow the spaceship
        gluLookAt(
            spaceship.pos[0], spaceship.pos[1] + 5, spaceship.pos[2] + 10,
            spaceship.pos[0], spaceship.pos[1], spaceship.pos[2],
            0, 1, 0
        )
        
        # Draw the background
        draw_background()
        
        # Draw and move the spaceship
        spaceship.draw()
        
        for bullet in spaceship.bullets:
            bullet.move()
        
        # Remove bullets that are off-screen
        spaceship.bullets = [bullet for bullet in spaceship.bullets if not bullet.is_off_screen()]

        # Draw and move enemies
        for enemy in enemies:
            enemy.draw()
            enemy.move()
        
        # Remove enemies that are off-screen
        enemies = [enemy for enemy in enemies if not enemy.is_off_screen()]

        # Check for collisions
        for bullet in spaceship.bullets:
            for enemy in enemies:
                if (abs(bullet.pos[0] - enemy.pos[0]) < 1 and
                        abs(bullet.pos[1] - enemy.pos[1]) < 1 and
                        abs(bullet.pos[2] - enemy.pos[2]) < 1):
                    spaceship.bullets.remove(bullet)
                    enemy.health -= 1
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                        score += 10
                    break
        
        # Display health and score
        render_text(f"Health: {spaceship.health}", (-4, 5, 0))
        render_text(f"Score: {score}", (2, 5, 0))

        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
