import pygame
from pyVariables import *



class Cell:
    """
    A class to represent a single cell for Conway's Game of Life
    """
    def __init__(self, rect, state=0):
        self.rect = pygame.Rect(rect)
        self.state = state
        self.prev_state = None

        self.color = GRAY




    def __str__(self):
        return f"Cell Rect: {self.rect} Cell State: {self.state}"



    """Event Handler"""
    def get_event(self, event, *args):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._handle_click(*args)


    def change_state(self):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1



    """Internal Methods"""
    def _handle_click(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.state = 1


    def update(self, surface, *args):
        if self.state == 1:
            self.color = BLACK
        elif self.state == 0:
            self.color = GRAY


        pygame.draw.rect(surface, self.color, self.rect, width=0)





if __name__ == '__main__':
    pygame.init()
    WIDTH = 600
    surface = pygame.display.set_mode((WIDTH, WIDTH))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life Cell")

    """Create the Cells"""

    cells = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(Cell(rect=(100+i*30,100+j*30,28,28), state=0))
        cells.append(row)

    def clickChange(pos, state):
        i = (pos[0] - 100) // 30
        j = (pos[1] - 100)// 30
        print(f"i:{i}----j:{j}----pos:{pos}")
        if i >=0 and i <= 9  and j >=0 and j <=9:
            print('yes')
            cells[i][j].change_state()


    print(cells)
    """More Pygame Loop"""
    run = True
    """Main Loop"""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed():
                    clickChange(pygame.mouse.get_pos(), 1)
                if pygame.mouse.get_pressed():
                    clickChange(pygame.mouse.get_pos(), 0)
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    clickChange(pygame.mouse.get_pos(), 1)



            """Call get_event for all cells, --> Board method"""
            # for row in cells:
            #     for cell in row:
            #         cell.get_event(event)


        surface.fill((BG_COLOR))
        for row in cells:
            for cell in row:
                cell.update(surface)
        pygame.display.update()
