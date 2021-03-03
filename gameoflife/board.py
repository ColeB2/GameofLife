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
        self.generation = 0
        self.create_board()
        self.set_cell_neighbours()



    def __repr__(self):
        pass

    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])
        print()


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
                cell = Cell(x=i, y=j, state=0)
                row.append(cell)
            self.board.append(row)


    def load_state(self, filename):
        path = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.dirname(path) + '/States/'
        cell_states = []
        with open(file_path + filename, 'r') as f:
            for line in f:
                line = line.split(',')
                if line:
                    line = [int(i) for i in line]
                    cell_states.append(line)
        ##Clear Board First
        self.dead_state()

        #APply loaded file states
        start_cell_x = int((BOARD_WIDTH - len(cell_states[0])) //2)
        start_cell_y = int((BOARD_HEIGHT - len(cell_states)) //2)
        i = start_cell_x
        j = start_cell_y
        print(f"i {i}j {j}")
        for row in cell_states:
            for value in enumerate(row):
                x = int(i + value[0])

                print(f"value {value} j: {j} i: {x}")
                print(self.board[j][i])
                self.board[x][j].state = value[1]
                self.board[x][j].prev_state = value[1]
                print(self.board[j][i])
            j += 1
        # self.print_board()



    def random_state(self, *args):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                cell.state = random.randint(0,1)
                cell.prev_state = cell.state


    def dead_state(self):
        """Kills all cells in the board, does so by iterating through all cells
        and changing their state to 0."""
        for row in self.board:
            for cell in row:
                cell.state = 0
                cell.prev_state = 0
        self.generation = 0


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
        self.set_cell_prev_state()
        self.generation += 1


    def cell_update(self, surface, *args):
        for row in self.board:
            for cell in row:
                cell.update(surface, *args)


    def update(self, surface):
        self.cell_update(surface)





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

        B.update(surface)
        BB.update(surface)
        if UPDATE:
            B.next_state()
            B.print_board()
            pygame.time.wait(300)

        pygame.display.update()
