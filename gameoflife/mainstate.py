from pyVariables import *
from board import Board
import pygame



class MainState:
    def __init__(self):
        self.B = Board(width=BOARD_WIDTH, height=BOARD_HEIGHT)

        self.run = True
        self.last_cell_change = None



    def get_cell(self, pos):
        """Converts a mouse position x,y value into a Cell coordinate value and
        returns that value."""
        i = (pos[0] - TOP_LEFT_X) // CELL_WIDTH
        j = (pos[1] - TOP_LEFT_Y) // CELL_WIDTH
        return i, j


    def boundary_check(self, i,j):
        """Out of bound check, to test whether the mouse value is outside of the
        board."""
        if i >=0 and i <= BOARD_WIDTH-1  and j >=0 and j <=BOARD_HEIGHT-1:
            return True
        return False


    def click_change(self, pos):
        """Mouse control option:
        Controls state of cell by first finding the i,j value of the cell. Then
        calling the draw_state method on said cell if called. """
        i, j = self.get_cell(pos)
        if self.boundary_check(i,j):
            self.B.board[i][j].draw_state()


    def motion_change(self, pos):
        """Mouse control click and drag control option.
        Controls state of cell via i,j value  and calls the draw state method
        of all cells that come in contact with mouse pointer while click held
        down"""
        i, j = self.get_cell(pos)
        if self.boundary_check(i,j) == True and self.last_cell_change != self.B.board[i][j]:
            self.B.board[i][j].draw_state()
            self.last_cell_change = self.B.board[i][j]

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.click_change(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    self.motion_change(pygame.mouse.get_pos())


    def update(self, surface):
        self.B.update(surface)


    def main_loop(self, surface):
        self.event_loop()
        self.update(surface)




if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life mainstate")
