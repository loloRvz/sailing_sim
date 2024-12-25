import numpy as np
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class Wind():

    def __init__(self, direction: float, speed: float, window_width: int, window_height:int, grid_size: int = 20):

        self.direction = direction
        self.speed = speed

        # Grid params
        self.window_width = window_width
        self.window_height = window_height
        self.grid_size = grid_size

        self.field = self.create_wind_field()

    def create_wind_field(self):
        field = np.zeros((self.grid_size, self.grid_size, 2))
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                field[i, j] = [self.speed * np.cos(self.direction), self.speed * np.sin(self.direction)]
        return field

    def get_wind_at(self, position: np.array):
        x, y = position
        i = int((x + WINDOW_WIDTH / 2) / (WINDOW_WIDTH / self.grid_size))
        j = int((y + WINDOW_HEIGHT / 2) / (WINDOW_HEIGHT / self.grid_size))
        return self.field[i, j]

