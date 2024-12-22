import numpy as np

class Boat():
    pos = np.array([0,0])
    vel = np.array([0,0])
    acc = np.array([0,0])


    def __init__(self, init_pos: list, dt: float):
        self.pos = init_pos
        self.dt = dt

    def loop(self):
        print(self.vel)
        self.pos = self.pos + self.vel * self.dt
        self.vel = self.vel + self.acc * self.dt