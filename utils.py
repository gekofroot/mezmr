# modules
import pygame as pg
from pygame.locals import *
from colour_palette import *


# draw shapes
def lindraw(screen, colour, x_pos_1, y_pos_1, x_pos_2, y_pos_2, width=0):
    """ draws line to screen """
    start_pos = (x_pos_1, y_pos_1)
    end_pos = (x_pos_2, y_pos_2)
    pg.draw.line(screen, colour, start_pos, end_pos, width)

def drawrec(screen, colour, x_pos, y_pos, width, height, n=0):
    """ draws rectangle (filled) to screen """
    rect = Rect(x_pos, y_pos, width, height)
    pg.draw.rect(screen, colour, rect, n)

def polydraw(screen, colour, x_pos_1, y_pos_1, x_pos_2, y_pos_2, width=0):
    """ draws polygon (filled) to screen """
    place = (x_pos_1, y_pos_1, x_pos_2, y_pos_2)
    pg.draw.polygon(screen, colour, place, width)
    
def elidraw(screen, colour, x_1, y_1, x_2, y_2, width=0):
    """ draws ellipse (filled) to screen """
    place = (x_1, y_1, x_2, y_2)
    pg.draw.ellipse(screen, colour, place, width)

if __name__ == '__main__':
    main()
