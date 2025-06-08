import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
PARTICLE_COLOR = (0, 0, 255)
PARTICLE_RADIUS = 10
NUM_PARTICLES = 10
VDW_RADIUS = 100
VDW_FORCE_CONSTANT = 0.05
DAMPING = 0.95

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Van der Waals Forces Visualization")

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.dragged = False

    def update(self):
        if not self.dragged:
            self.x += self.vx
            self.y += self.vy

            # Keep inside bounds
            if self.x < PARTICLE_RADIUS or self.x > WIDTH - PARTICLE_RADIUS:
                self.vx *= -1
                self.x = max(PARTICLE_RADIUS, min(self.x, WIDTH - PARTICLE_RADIUS))
            if self.y < PARTICLE_RADIUS or self.y > HEIGHT - PARTICLE_RADIUS:
                self.vy *= -1
                self.y = max(PARTICLE_RADIUS, min(self.y, HEIGHT - PARTICLE_RADIUS))

            # Apply damping
            self.vx *= DAMPING
            self.vy *= DAMPING

    def draw(self):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

    def is_mouse_over(self, mouse_pos):
        dx = self.x - mouse_pos[0]
        dy = self.y - mouse_pos[1]
        return math.hypot(dx, dy) <= PARTICLE_RADIUS

# Generate particles
particles = [Particle(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)) for _ in range(NUM_PARTICLES)]

# Dragging state
dragged_particle = None

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for particle in particles:
                if particle.is_mouse_over(mouse_pos):
                    dragged_particle = particle
                    dragged_particle.dragged = True
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragged_particle:
                dragged_particle.dragged = False
                dragged_particle = None

        elif event.type == pygame.MOUSEMOTION:
            if dragged_particle:
                dragged_particle.x, dragged_particle.y = mouse_pos
                dragged_particle.vx = 0
                dragged_particle.vy = 0

    screen.fill(BACKGROUND_COLOR)

    # Calculate forces
    for i, p1 in enumerate(particles):
        if p1.dragged:
            continue
        for j, p2 in enumerate(particles):
            if i != j:
                dx = p1.x - p2.x
                dy = p1.y - p2.y
                dist = math.hypot(dx, dy)

                # Lennard-Jones parameters
                epsilon = 0.1
                sigma = 2 * PARTICLE_RADIUS
                max_force = 5

                if dist < VDW_RADIUS and dist > 1e-2:
                    # Lennard-Jones force magnitude
                    lj_scalar = 24 * epsilon * ((2 * (sigma / dist)**13) - ((sigma / dist)**7)) / dist

                    # Force components
                    fx = lj_scalar * dx
                    fy = lj_scalar * dy

                    # Cap the force to prevent instability
                    fx = max(-max_force, min(fx, max_force))
                    fy = max(-max_force, min(fy, max_force))

                    p1.vx += fx
                    p1.vy += fy



    # Update and draw particles
    for p in particles:
        p.update()
        p.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
