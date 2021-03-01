from pyVariables import *
from cell import Cell
import random
import os


class Board:
    """
    A class to represent a group of cells, laid out in a board like fashion,
    designed for use in Conway's Game of Life.
    """
    def __init__(self, width=10, height=10):
        self.width = width #row
        self.height = height #col
        self.board = []
        self.create_board()
        print(self.board)
        self.set_cell_neighbours()


    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])
        print()


    def random_state(self):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                cell.state = random.randint(0,1)
                cell.prev_state = cell.state


    def dead_state(self):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                cell.state = 0
                cell.prev_state = cell.state


    def set_cell_prev_state(self):
        """Sets the all the cell's in the board prev_state attribute to be the
        value of all current state values."""
        for row in range(len(self.board)):
            for cell in self.board[row]:
                cell.prev_state = cell.state




    def create_board(self):
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(Cell(x=i,
                                y=j,
                                state=0))
            self.board.append(row)


    def dead_state(self):
        """Kills all cells in the board, does so by iterating through all cells
        and changing their state to 0."""
        for row in range(len(self.board)):
            for cell in self.board[row]:
                cell.state = 0


    def set_cell_neighbours(self):
        """Iterates through all cells, and creates a list of neighbours
        for each cell."""
        for row in range(len(self.board)):
            for cell in self.board[row]:
                cell.get_neighbours(self.board)



    def next_state(self):
        """
        Calculates the next state the board should be in. Does so by
        iterating through all cells in the board, and calling their
        calculate_state methods
        """
        for row in range(len(self.board)):
            for cell in self.board[row]:
                cell.calculate_state()
        self.reset_state()



if __name__ == "__main__":
    from buttons import Button
    import pygame
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life Board")

    """button"""
    UPDATE = False
    def BF():
        global UPDATE
        if UPDATE == False:
            UPDATE = True
        else:
            UPDATE = False

    BB = Button(rect=(0,0,100,100), function=BF)

    B = Board(width=BOARD_WIDTH, height=BOARD_HEIGHT)


    def get_cell(pos):
        i = (pos[0] - TOP_LEFT_X) // CELL_WIDTH
        j = (pos[1] - TOP_LEFT_Y) // CELL_WIDTH
        return i, j

    def collision_check(i,j):
        if i >=0 and i <= BOARD_WIDTH-1  and j >=0 and j <=BOARD_HEIGHT-1:
            return True
        return False


    def clickChange(pos):
        """Mouse control option:
        Controls state of cell by first finding the i,j value of the cell. Then
        calling the change state method on said cell if called. """
        i, j = get_cell(pos)
        if collision_check(i,j):
            B.board[i][j].draw_state()

    last_cell_change = None
    def motionChange(pos):
        global last_cell_change
        i, j = get_cell(pos)
        # print(f"i:{i}----j:{j}----pos:{pos}")
        if collision_check(i,j) == True and last_cell_change != B.board[i][j]:
            B.board[i][j].draw_state()
            last_cell_change = B.board[i][j]

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
                    motionChange(pygame.mouse.get_pos())

            BB.get_event(event)


        surface.fill((BG_COLOR))
        for row in B.board:
            for cell in row:
                cell.update(surface)

        BB.update(surface)
        if UPDATE:
            B.next_state()
            B.print_board()
            pygame.time.wait(300)

        pygame.display.update()
