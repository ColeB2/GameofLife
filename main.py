import pygame
import os, sys
sys.path.append(os.path.join('.',  'gameoflife'))
from pyVariables import *
from mainstate import MainState


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    game = MainState()
    while game.run:
        current_time = pygame.time.get_ticks()
        clock.tick(FPS)
        surface.fill(BG_COLOR)
        game.main_loop(surface, current_time)
        pygame.display.update()
