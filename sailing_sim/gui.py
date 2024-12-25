import sys
import pygame
import numpy as np
import math

from boat import Boat
from wind import Wind

from config import BLUE, WHITE


class GUI():

    def __init__(self, width: int, height: int, pixel_per_meter: int, caption: str, max_fps: int):
        self.width = width
        self.height = height
        self.max_fps = max_fps
        self.pixel_per_meter = pixel_per_meter

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)

    def check_running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    # Handle user input for movement
    def check_inputs(self, boat: Boat):
        keys = pygame.key.get_pressed()

        boat.inputs.up = keys[pygame.K_UP]
        boat.inputs.down = keys[pygame.K_DOWN]
        boat.inputs.left = keys[pygame.K_LEFT]
        boat.inputs.right = keys[pygame.K_RIGHT]

    def meters_to_pixels(self, meters: np.array):
        pixels = meters * self.pixel_per_meter
        pixels[1] = -pixels[1]
        pixels += np.array([self.width, self.height]) / 2
        return pixels


    def draw(self, boat, wind: Wind):
        self.screen.fill(BLUE)
        
        # # Draw wind field
        # for i in range(wind.grid_size):
        #     for j in range(wind.grid_size):
        #         start_pos = np.array([i * (self.width / wind.grid_size) - self.width / 2,
        #                               j * (self.height / wind.grid_size) - self.height / 2])
        #         end_pos = start_pos + wind.field[i, j] * self.pixel_per_meter
        #         pygame.draw.line(self.screen, WHITE, self.meters_to_pixels(start_pos), self.meters_to_pixels(end_pos))

        # Draw boat
        C = np.array([
            [math.cos(boat.rot),-math.sin(boat.rot)],
            [math.sin(boat.rot), math.cos(boat.rot)]])
        
        nodes = np.dot(C, np.transpose(boat.shape))
        nodes = np.add(nodes, boat.pos[:, np.newaxis])

        pygame.draw.polygon(self.screen, WHITE, [self.meters_to_pixels(node) for node in nodes.T])  # Simple boat as a rectangle

        # Display FPS
        fps = self.clock.get_fps()
        fps_text = self.font.render(f'FPS: {int(fps)}', True, WHITE)
        self.screen.blit(fps_text, (10, 10))

        pygame.display.flip()

        # Limit frame rate to the specified max FPS
        self.clock.tick(self.max_fps)
    
    def quit(self):
        pygame.quit()
        sys.exit()