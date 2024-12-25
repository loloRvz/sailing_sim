import sys
import pygame
import numpy as np
import math
import time

from boat import Boat
from wind import Wind

import config as cfg


class GUI():

    def __init__(self, width: int, height: int, pixel_per_meter: int, bg_colour: list, caption: str):
        # Graphics setup
        self.width = width
        self.height = height
        self.pixel_per_meter = pixel_per_meter
        self.bg_colour = bg_colour

        # Game setup
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont(None, 24)

        #CLock setup
        self.last_time = time.time()

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

    def draw(self, boat: Boat, wind: Wind, fps: float, cpu_load: float):
        # Draw background
        self.screen.fill(self.bg_colour)
        
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
        pygame.draw.polygon(self.screen, cfg.WHITE, [self.meters_to_pixels(node) for node in nodes.T])

        if cfg.PRINT_PERF:
            current_time = time.time()
            fps = 1 / (current_time - self.last_time)
            self.last_time = current_time

            # Display FPS
            fps_text = self.font.render(f'FPS: {float(fps)}', True, cfg.WHITE)
            self.screen.blit(fps_text, (10, 10))

            cpu_load_text = self.font.render(f'CPU: {int(cpu_load*100)}%', True, cfg.WHITE)
            self.screen.blit(cpu_load_text, (10, 30))

        pygame.display.flip()

    
    def quit(self):
        pygame.quit()
        sys.exit()