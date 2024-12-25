import numpy as np
import math

import config as cfg

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

    shape = cfg.BOAT_shape

    inputs = Inputs()

    def __init__(self, init_pos: list, dt: float):
        self.pos = init_pos
        self.dt = dt

    def loop(self):
        # Init force and torque
        force = np.zeros(2)
        torque = 0

        # Compute longitudinal and lateral velocity components
        rot_vec = np.array([math.cos(self.rot), math.sin(self.rot)])
        abs_long_vel = np.dot(self.vel, rot_vec)
        long_vel = abs_long_vel * rot_vec
        lat_vel = self.vel - long_vel

        # Motor force (front and back)
        force += cfg.BOAT_F * (self.inputs.up - self.inputs.down) * rot_vec

        # Rudder force (rotation)
        torque += cfg.BOAT_R * abs_long_vel * (self.inputs.left - self.inputs.right)

        # Keel force (lateral)
        force += cfg.BOAT_K * -lat_vel
        

        # F = ma
        self.acc = 1/cfg.BOAT_M * (force - cfg.BOAT_b * self.vel)
        self.vel = self.vel + self.acc * self.dt
        self.pos = self.pos + self.vel * self.dt

        # T = Jw'
        self.rot_acc = 1/cfg.BOAT_J * (torque - cfg.BOAT_v * self.rot_vel)
        self.rot_vel += self.rot_acc * self.dt
        self.rot += self.rot_vel * self.dt


        # Loop back boat position if out of screen
        if self.pos[0] > cfg.W_HALF:
            self.pos[0] = -cfg.W_HALF
        if self.pos[0] < -cfg.W_HALF:
            self.pos[0] = cfg.W_HALF
        if self.pos[1] > cfg.H_HALF:
            self.pos[1] = -cfg.H_HALF
        if self.pos[1] < -cfg.H_HALF:
            self.pos[1] = cfg.H_HALF


