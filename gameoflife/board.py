import pygame
from pyVariables import *
from cell import Cell


class Board:
    """
    A class to represent a group of cells, laid out in a board like fashion,
        designed for use in Conway's Game of Life.
    """
    def __init__(self, width=10, height=10):
        self.width = width #row
        self.height = height #col
        self.board = []
        self.all_cells = []
        self.create_board()



    def create_board(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Cell(rect=(100+i*30, 100+j*30, 28,28), state=0))
            self.board.append(row)



if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life Board")

    B = Board(width=10, height=10)


    def clickChange(pos):
        """Mouse control option:
        Controls state of cell by first finding the i,j value of the cell. Then
        calling the change state method on said cell if called. """
        i = (pos[0] - 100) // 30
        j = (pos[1] - 100)// 30
        print(f"i:{i}----j:{j}----pos:{pos}")
        if i >=0 and i <= 9  and j >=0 and j <=9:
            B.board[i][j].change_state()

    run = True
    """Main Loop"""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    clickChange(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    clickChange(pygame.mouse.get_pos())


        surface.fill((BG_COLOR))
        for row in B.board:
            for cell in row:
                cell.update(surface)
        pygame.display.update()
