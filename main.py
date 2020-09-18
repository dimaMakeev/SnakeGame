import math
import random
import pygame
import pygame.display
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__ (self): 
        pass
    def move(self):
        pass
    def draw(self):
        pass
class snake(object):
    body = []
    turns = {}
    def __init__(self):
        pass 
def redrawWindow(surface):
    global width, rows
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
def drawGrid(w, rows, surface):
    sizeBeetwen = w//rows
    x = 0
    y = 0
    for l in range (rows):
        x = x + sizeBeetwen
        y = y + sizeBeetwen
        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,x), (w,y))
    

def main():
    global width, rows  
    width = 500   
    rows = 20
    win = pygame.display.set_mode((width, width))
    #s = snake((255,0,0), (10,10))
    flag = True  
    
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)  
        redrawWindow(win)
         
main()    