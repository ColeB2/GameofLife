import pygame
from pyVariables import *



class Cell:
    """
    A class to represent a single cell, created using pygame.Rect object,
    designed for use in Conway's Game of Life program.
    """
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = self.prev_state = state

        self.rect = pygame.Rect(TOP_LEFT_X+self.x*CELL_WIDTH,
                                TOP_LEFT_Y+self.y*CELL_WIDTH,
                                CELL_WIDTH-2,
                                CELL_WIDTH-2)
        self.neighbours = []



    def __str__(self):
        return f"Cell x: {self.x} Cell y: {self.y} Cell State: {self.state}"


    def __repr__(self):
        return f"{self.x},{self.y}:{self.state}"



    def get_neighbours(self, neighbourhood, neighbours=[-1,0,1]):
        """
        Gets all neighbouring cells and adds them to the list of neighbours
        """
        for j in neighbours:
            for i in neighbours:
                valid_neighbour = True
                if i == 0 and j == 0:
                    # Can't be neighbours with self
                    valid_neighbour = False
                elif self.x + i < 0 or self.y + j < 0:
                    #Can't be neighbours with cells off the board/ other side
                    valid_neighbour = False
                elif self.x + i > len(neighbourhood[0])-1 or self.y + j > len(neighbourhood)-1:
                    #Can't neighbours with cells that don't exists/ off the board
                    valid_neighbour = False

                if valid_neighbour:
                    self.neighbours.append(neighbourhood[self.y + j][self.x + i])


    def check_neighbour_state(self):
        """Checks the state of all neighbouring cells"""
        self.alive_neighbours = 0
        for cell in self.neighbours:
            if cell.prev_state:
                self.alive_neighbours += 1


    def draw_state(self):
        """Used for drawing purposes, flips state from 1,0 depending on state"""
        self.state=self.prev_state=0 if self.state else 1

    def calculate_state(self):
        """
        calculate_state - Used to calculate the state of of the cell. Does
        so by checking state of all the neighbours, and once given the amount
        of live neighbours in the area, uses given rules to calculate own state
        """
        self.check_neighbour_state()
        if self.state:
            self.state = 1 if self.alive_neighbours in [2,3] else 0
        else:
            self.state = 1 if self.alive_neighbours == 3 else 0


    def update(self, surface, *args):
        """cells main update method."""
        self.color = BLACK if self.state else GRAY
        pygame.draw.rect(surface, self.color, self.rect, width=0)






if __name__ == '__main__':
    """Sandbox Testing"""
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life Cell")

    """Create the Cells"""

    cells = []
    for j in range(BOARD_HEIGHT):
        row = []
        for i in range(BOARD_WIDTH):
            row.append(Cell(i,j, state=0))
        cells.append(row)


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
            cells[j][i].draw_state()

    last_cell_change = None
    def motionChange(pos):
        global last_cell_change
        i, j = get_cell(pos)
        # print(f"i:{i}----j:{j}----pos:{pos}")
        if collision_check(i,j) == True and last_cell_change != cells[j][i]:
            cells[j][i].draw_state()
            last_cell_change = cells[j][i]


    print(cells)
    """More Pygame Loop"""
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


        surface.fill((BG_COLOR))
        for row in cells:
            for cell in row:
                cell.update(surface)
        pygame.display.update()
