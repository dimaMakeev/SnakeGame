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

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos) 
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx =-1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx =1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
         for i,c in enumerate(self.body):
            p=c.pos[:]
            if p in self.turns:
                 c.move(turn[0], turn[1])
                 if i == len(self.body)-1:
                     self.turns.pop(p) 
            else: 
                if c.dirnx = -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])



def redrawWindow(surface):
    global width, rows
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
def drawGrid(w, rows, surface):
    sizeBeetwen = w//rows
    x = 0
    y = 0
    for l in rows:
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
    #pygame.display.init()
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)  
        redrawWindow(win)
         
main()    