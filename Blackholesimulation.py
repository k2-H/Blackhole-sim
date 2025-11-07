import pygame
import math
import sys

pygame.init()
width, height = 1366, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blackhole with Thermal Color Effects")

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 139)
G = 2500
DAMPING = 0.98

# Blackhole setup
center = (width//2, height//2)
bh_radius = int(min(width, height) * 0.04)
photon_sphere = bh_radius * 8
influence_radius = photon_sphere * 2  # Start color transitions earlier

particles = []

class Particle:
    def __init__(self, pos):
        self.pos = list(pos)
        dx = center[0] - pos[0]
        dy = center[1] - pos[1]
        r = math.hypot(dx, dy)
        
        orbital_velocity = math.sqrt(G/r) * 0.99
        self.vel = [-dy/r * orbital_velocity, dx/r * orbital_velocity]
        self.trail = []

    def get_thermal_color(self, r):
        """Returns color based on distance using blackbody-inspired gradient"""
        if r > influence_radius:
            return WHITE
        
        # Stage 1: White to red (cooling phase)
        if influence_radius >= r > photon_sphere:
            t = (influence_radius - r) / (influence_radius - photon_sphere)
            return (255, int(255*(1-t)), int(255*(1-t)))
        
        # Stage 2: Red to blue (heating phase)
        if photon_sphere >= r > bh_radius*1.5:
            t = (photon_sphere - r) / (photon_sphere - bh_radius*1.5)
            return (int(255*(1-t)), 0, int(255*t))
        
        # Stage 3: Blue to dark blue (extreme gravity)
        if bh_radius*1.5 >= r > bh_radius:
            t = (bh_radius*1.5 - r) / (bh_radius*1.5 - bh_radius)
            return (0, 0, int(255*(1-t) + 139*t))
        
        return DARK_BLUE

    def update(self, dt):
        self.prev_pos = list(self.pos)
        
        dx = center[0] - self.pos[0]
        dy = center[1] - self.pos[1]
        r = math.hypot(dx, dy)
        
        if r > 0:
            acceleration = G / (r**2) * DAMPING
            self.vel[0] += (dx/r) * acceleration * dt
            self.vel[1] += (dy/r) * acceleration * dt
            
            self.pos[0] += self.vel[0] * dt
            self.pos[1] += self.vel[1] * dt

            current_color = self.get_thermal_color(r)
            self.trail.append((*map(int, self.pos), current_color))
            
            if len(self.trail) > 50:
                self.trail.pop(0)

    def draw(self):
        for i in range(len(self.trail)-1):
            start = self.trail[i]
            end = self.trail[i+1]
            color = start[2]  # Use stored color
            pygame.draw.line(screen, color, (start[0], start[1]), (end[0], end[1]), 1)

# Main loop remains the same
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(120)/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            particles.append(Particle(event.pos))

    screen.fill(BLACK)
    
    # Draw blackhole elements
    pygame.draw.circle(screen, BLACK, center, bh_radius)
    pygame.draw.circle(screen, (40, 40, 40), center, photon_sphere, 1)
    pygame.draw.circle(screen, (20, 20, 20), center, influence_radius, 1)
    
    # Update and draw particles
    for p in particles[:]:
        p.update(dt*10)
        p.draw()
        
        if math.dist(center, p.pos) < bh_radius:
            particles.remove(p)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
