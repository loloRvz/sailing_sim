import sys
import pygame
import numpy as np
import math

from boat import Boat, Inputs
from inputs import Inputs 

# Colors
BLUE = (70, 130, 180)  # Water color
WHITE = (255, 255, 255)


PIXEL_PER_METER = 10

class GUI():

    def __init__(self, width: int, height: int, caption: str):
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def check_running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    # Handle user input for movement
    def check_inputs(self, boat: Boat):
        keys = pygame.key.get_pressed()

        boat.inputs[Inputs.FRONT.value] = keys[pygame.K_UP]
        boat.inputs[Inputs.BACK.value] = keys[pygame.K_DOWN]
        boat.inputs[Inputs.LEFT.value] = keys[pygame.K_LEFT]
        boat.inputs[Inputs.RIGHT.value] = keys[pygame.K_RIGHT]

    def meters_to_pixels(self, meters: np.array):
        pixels = meters * PIXEL_PER_METER
        pixels[1] = -pixels[1]
        pixels += np.array([self.width, self.height]) / 2
        return pixels


    def draw(self, boat):
        self.screen.fill(BLUE)
        
        C = np.array([
            [math.cos(boat.rot),-math.sin(boat.rot)],
            [math.sin(boat.rot), math.cos(boat.rot)]])
        
        nodes = np.dot(C, np.transpose(boat.shape))
        nodes = np.add(nodes, boat.pos[:, np.newaxis])

        pygame.draw.polygon(self.screen, WHITE, [self.meters_to_pixels(node) for node in nodes.T])  # Simple boat as a rectangle

        pygame.display.flip()

        # Limit frame rate to 60 FPS
        self.clock.tick(60)
    
    def quit(self):
        pygame.quit()
        sys.exit()