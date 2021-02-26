import pygame
from pyVariables import *



class Cell:
    """
    A class to represent a single cell, created using pygame.Rect object,
        designed for use in Conway's Game of Life program.
    """
    def __init__(self, rect, state=0):
        self.rect = pygame.Rect(rect)
        self.state = state
        self.prev_state = None
        self.color = GRAY



    def __str__(self):
        return f"Cell Rect: {self.rect} Cell State: {self.state}"



    def change_state(self):
        if self.state == 1:
            self.state = 0
            self.prev_state = 1
        else:
            self.state = 1
            self.prev_state = 0


    def update(self, surface, *args):
        if self.state == 1:
            self.color = BLACK
        elif self.state == 0:
            self.color = GRAY

        pygame.draw.rect(surface, self.color, self.rect, width=0)





if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life Cell")

    """Create the Cells"""

    cells = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(Cell(rect=(100+i*30,100+j*30,28,28), state=0))
        cells.append(row)


    def get_cell(pos):
        i = (pos[0] - 100) // 30
        j = (pos[1] - 100) // 30
        return i, j

    def collision_check(i,j):
        if i >=0 and i <= 9  and j >=0 and j <=9:
            return True
        return False


    def clickChange(pos):
        """Mouse control option:
        Controls state of cell by first finding the i,j value of the cell. Then
        calling the change state method on said cell if called. """
        i, j = get_cell(pos)
        if collision_check(i,j):
            cells[i][j].change_state()

    last_cell_change = None
    def motionChange(pos):
        global last_cell_change
        i, j = get_cell(pos)
        print(f"i:{i}----j:{j}----pos:{pos}")
        if collision_check(i,j) == True and last_cell_change != cells[i][j]:
            cells[i][j].change_state()
            last_cell_change = cells[i][j]


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
