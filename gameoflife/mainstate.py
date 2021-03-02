from pyVariables import *
from board import Board
import pygame



class GameOfLife:
    def __init__(self):
        self.B = Board(width=BOARD_WIDTH, height=BOARD_HEIGHT)

        self.run = True



    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    clickChange(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    motionChange(pygame.mouse.get_pos())


    def update(self):
        pass
