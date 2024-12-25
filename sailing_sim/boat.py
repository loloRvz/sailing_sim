import numpy as np
import math

from config import W_HALF, H_HALF, BOAT_PARAMS

class Inputs():
    up = False
    down = False
    left = False
    right = False

class Boat():
    pos = np.array([0,0])
    vel = np.array([0,0])
    acc = np.array([0,0])

    rot = 0
    rot_vel = 0
    rot_acc = 0

    shape = BOAT_PARAMS.shape

    inputs = Inputs()

    def __init__(self, init_pos: list, dt: float):
        self.pos = init_pos
        self.dt = dt

    def loop(self):
        # Init force and torque
        force = np.zeros(2)
        torque = 0

        # Keel force (side force)
        rot_vec = np.array([math.cos(self.rot), math.sin(self.rot)])
        abs_long_vel = np.dot(self.vel, rot_vec)
        long_vel = abs_long_vel * rot_vec
        lat_vel = self.vel - long_vel

        # Motor force (front and back)
        force += BOAT_PARAMS.F * (self.inputs.up - self.inputs.down) * rot_vec

        # Rudder force (rotation)
        torque += BOAT_PARAMS.R * abs_long_vel * (self.inputs.left - self.inputs.right)

        # Keel force (lateral)
        force += BOAT_PARAMS.K * -lat_vel
        

        # F = ma
        self.acc = 1/BOAT_PARAMS.M * (force - BOAT_PARAMS.b * self.vel)
        self.vel = self.vel + self.acc * self.dt
        self.pos = self.pos + self.vel * self.dt

        # T = Jw'
        self.rot_acc = 1/BOAT_PARAMS.J * (torque - BOAT_PARAMS.v * self.rot_vel)
        self.rot_vel += self.rot_acc * self.dt
        self.rot += self.rot_vel * self.dt



        # Loop back boat position if out of screen
        if self.pos[0] > W_HALF:
            self.pos[0] = -W_HALF
        if self.pos[0] < -W_HALF:
            self.pos[0] = W_HALF
        if self.pos[1] > H_HALF:
            self.pos[1] = -H_HALF
        if self.pos[1] < -H_HALF:
            self.pos[1] = H_HALF


