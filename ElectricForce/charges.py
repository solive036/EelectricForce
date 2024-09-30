import pygame as pg
import numpy as np


class Charge(pg.sprite.Sprite):
    def __init__(self, magnitude, charge_type, x, y):
        super().__init__()
        self.magnitude = magnitude
        self.charge_type = charge_type
        self.x = x
        self.y = y
        self.force = 0
        self.phi = 0
        self.vec = [0, 0]

    #displays the charge according to charge type (+ or -)
    def display_charge(self, window):
        if self.charge_type == '+':
            COLOR = (255, 0, 0)
        else:
            COLOR = (0, 0, 255)
        pg.draw.circle(window, COLOR, (self.x, self.y), 10)

    #calculates the force between the two point charges
    def compute_force(self, source):
        self.force = (source.magnitude)*(self.magnitude)*(100000)/(np.sqrt((self.x - 500)**2 + (self.y - 500) **2) **2)
    
    #calculates the angle between the source charge and the test charge
    def compute_phi(self):
        dx = self.x - 500
        dy = self.y - 500
        self.phi = np.arctan2(dy, dx)

    #calculates the end coordinates of the force vector in relation to the test charge
    def compute_vec_coords(self):
        x_temp = self.force*np.cos(self.phi)
        y_temp = self.force*np.sin(self.phi)

        if self.charge_type == '-':
            x_temp = -x_temp
            y_temp = -y_temp

        self.vec[0] = self.x + x_temp
        self.vec[1] = self.y + y_temp

    #displays the force vector for the corresponding test charge
    def display_vec(self, window):
        pg.draw.line(window, (255, 255, 255), (self.x, self.y), (self.vec[0], self.vec[1]), 2)
