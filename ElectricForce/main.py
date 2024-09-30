import pygame as pg
from pygame.locals import *
from charges import Charge
import numpy as np

#pygame setup
WIDTH = 1000
HEIGHT = 1000
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Electric Force Simulation')


def display_grid(window):
    #draw grid in x direction
    y = 0
    x = 0
    for i in range(0, 10):
        pg.draw.line(window, (50, 50, 50), (0, y), (1000, y), 2)
        y += 100
    
    #draw grid in y direction
    for i in range(0, 10):
        pg.draw.line(window, (50, 50, 50), (x, 0), (x, 1000), 2)
        x+= 100

def main():
    source_charge = Charge(10, '+', 500, 500)
    current_charges = []

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN: 
                if event.key == pg.K_x: #press 'x' key to clear the screen
                    current_charges = []
                elif event.key == pg.K_RIGHT:
                    mouse_pos = pg.mouse.get_pos() #right arrow press for positive charge
                    current_charges.append(Charge(1, '+', int(mouse_pos[0]), int(mouse_pos[1])))
                elif event.key == pg.K_LEFT: #left arrow press for negative charge
                    mouse_pos = pg.mouse.get_pos()
                    if mouse_pos[0] > 480 and mouse_pos[0] < 520 and mouse_pos[1] > 480 and mouse_pos[1] < 520:
                        current_charges = current_charges
                    else:
                        current_charges.append(Charge(1, '-', int(mouse_pos[0]), int(mouse_pos[1])))
                

        window.fill((0, 0, 0))
        display_grid(window)
        pg.draw.circle(window, (200, 200, 200), (source_charge.x, source_charge.y), 20) #display the source charge
        pg.draw.line(window, (200, 0, 0), (496, 500), (504, 500))
        pg.draw.line(window, (200, 0, 0), (500, 496), (500, 504))

        #display the test charges and force vectors
        for ch in current_charges:
            ch.compute_force(source_charge)
            ch.display_charge(window)
            ch.compute_phi()
            ch.compute_vec_coords()
            ch.display_vec(window)

        pg.display.flip()

main()
