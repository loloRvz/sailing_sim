import pygame
import sys

from boat import Boat

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sailing Simulator")

# Colors
BLUE = (70, 130, 180)  # Water color
WHITE = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Main loop
def main():

    boat = Boat(init_pos = [WIDTH/2, HEIGHT/2], dt = 0.01)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle user input for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            boat.acc[1] = 1
        if keys[pygame.K_DOWN]:
            boat.acc[1] = -1
        if keys[pygame.K_LEFT]:
            boat.acc[0] = -1
        if keys[pygame.K_RIGHT]:
            boat.acc[0] = 1

        # Compute one physics loop
        boat.loop()

        # Draw everything
        screen.fill(BLUE)  # Background water
        pygame.draw.rect(screen, WHITE, (*boat.pos, 50, 20))  # Simple boat as a rectangle

        # Update the display
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()
