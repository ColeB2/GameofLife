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

        self.generation = 0

        self._create_board()
        self._set_cell_neighbours()



    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])
        print()


    def set_cell_prev_state(self):
        """Sets the all the cell's in the board prev_state attribute to be the
        value of all current state values."""
        for row in self.board:
            for cell in row:
                cell.prev_state = cell.state


    def _create_board(self):
        """
        Internal method to be called upon init. Creates a 2d array/list and
        populates the list with Cell objects with a default state of 0/dead
        """
        self.board = [[Cell(x=i, y=j, state=0) for i in range(self.width)]\
                                               for j in range(self.height) ]


    def _load_file(self, filename):
        """
        Returns a list of cell states. Does so by loading a file and
        creating a list of states for the cells
        params:
            filename: str - name of the file for which to pull the information
        from --> 'filename.txt'
        """
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.dirname(path) + '/States/'
        cell_states = []
        with open(file_path + filename, 'r') as f:
            for line in f:
                line = line.split(',')
                if line:
                    line = [int(i) for i in line]
                    cell_states.append(line)
        return cell_states


    def _apply_state(self, cell_list):
        """
        Applys the state to the approrpiate cells in the board. Tries to
        to center the state as well.
        params:
            cell_list: 2D list of cells and their state value
                [[1,1,1],
                 [1,0,1],
                 [1,1,1]]
        """
        i = int((self.width - len(cell_list[0])) //2)
        j = int((self.height - len(cell_list)) //2)
        for row in cell_list:
            for x_offset, state in enumerate(row):
                x = int(i + x_offset)
                self.board[j][x].state = self.board[j][x].prev_state = state
            j += 1


    def load_state(self, filename):
        """
        Clears the board by calling the dead_state method. Loads the state to
        be applied via _load_file method and passes information on to the
        _apply_state method to apply the given state to the board.
        """
        self.dead_state()
        cell_states = self._load_file(filename)
        self._apply_state(cell_states)


    def random_state(self, *args):
        """Creates a random state by looping through each cell and randomly
        selecting a state for it to be in."""
        for row in self.board:
            for cell in row:
                cell.state = cell.prev_state = random.randint(0,1)


    def dead_state(self, *args):
        """Kills all cells in the board, does so by iterating through all cells
        and changing their state and prev_state to 0 while also resetting the
        generation counter."""
        for row in self.board:
            for cell in row:
                cell.state = cell.prev_state = 0
        self.generation = 0


    def _set_cell_neighbours(self):
        """Internal method, iterates through all cells, and creates a list of
        neighbours for each cell."""
        for row in self.board:
            for cell in row:
                cell.get_neighbours(self.board)


    def next_state(self):
        """
        Calculates the next state the board should be in. Does so by
        iterating through all cells in the board, and calling their
        calculate_state methods
        """
        for row in self.board:
            for cell in row:
                cell.calculate_state()
        self.set_cell_prev_state()
        self.generation += 1


    def cell_update(self, surface, *args):
        """Update method which calls each individual cells update methods."""
        for row in self.board:
            for cell in row:
                cell.update(surface, *args)


    def update(self, surface):
        """Update Function for the board"""
        self.cell_update(surface)







if __name__ == "__main__":
    """Sandbox Testing"""
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
        if i >=0 and i <= B.width-1  and j >=0 and j <= B.height-1:
            return True
        return False


    def clickChange(pos):
        """Mouse control option:
        Controls state of cell by first finding the i,j value of the cell. Then
        calling the change state method on said cell if called. """
        i, j = get_cell(pos)
        if collision_check(i,j):
            B.board[j][i].draw_state()

    last_cell_change = None
    def motionChange(pos):
        global last_cell_change
        i, j = get_cell(pos)
        if collision_check(i,j) == True and last_cell_change != B.board[j][i]:
            B.board[j][i].draw_state()
            last_cell_change = B.board[j][i]

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
