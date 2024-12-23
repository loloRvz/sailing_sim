import numpy as np
import math

from inputs import Inputs 

class Boat():
    M = 20
    J = 40
    b = 10
    v = 40

    F = 1000
    R = 30

    pos = np.array([0,0])
    vel = np.array([0,0])
    acc = np.array([0,0])

    rot = 0
    rot_vel = 0
    rot_acc = 0

    shape = np.array([
        [3,0],
        [2,-1],
        [-3,-1],
        [-3,1],
        [2,1]])

    inputs = np.array([0,0,0,0])

    def __init__(self, init_pos: list, dt: float):
        self.pos = init_pos
        self.dt = dt

    def loop(self):        
        # F = ma
        force = np.zeros(2)
        if self.inputs[Inputs.FRONT.value] or self.inputs[Inputs.BACK.value]:
            force = np.array([math.cos(self.rot),math.sin(self.rot)])
            force *= self.F * (self.inputs[Inputs.FRONT.value] - self.inputs[Inputs.BACK.value])

        self.acc = 1/self.M * (force - self.b * self.vel)
        self.vel = self.vel + self.acc * self.dt
        self.pos = self.pos + self.vel * self.dt

        rot_force = 0
        if self.inputs[Inputs.LEFT.value] or self.inputs[Inputs.RIGHT.value]:
            abs_vel = self.vel[0] * math.cos(self.rot) + self.vel[1] * math.sin(self.rot)
            rot_force = self.R * abs_vel * (self.inputs[Inputs.LEFT.value] - self.inputs[Inputs.RIGHT.value])

        self.rot_acc = 1/self.J * (rot_force - self.v * self.rot_vel)
        self.rot_vel += self.rot_acc * self.dt
        self.rot += self.rot_vel * self.dt

