import pygame
from pyVariables import *



class Cell:
    """
    A class to represent a single cell for Conway's Game of Life
    """
    def __init__(self, rect, state=0):
        self.rect = pygame.Rect(rect)
        self.state = state

        self.color = GRAY


        self.clicked = False
        self.hovered = True
        self.hover_color = (LIGHT_GREEN)
        self.run_on_release = False


    def __str__(self):
        return f"Cell Rect: {self.rect} Cell State: {self.state}"



    """Event Handler"""
    def get_event(self, event, *args):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._handle_click(*args)
        elif event.type == pygame.MOUSEBUTTONUP and event.button ==1:
            self._handle_release(*args)


    """Internal Methods"""
    def _handle_click(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.clicked = True


    def _handle_release(self, *args):
        """Unused for now"""
        if self.clicked and self.run_on_release:
            pass
        self.clicked = False


    def _handle_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.hovered == False:
                self.hovered = True
        else:
            self.hovered = False


    def update(self, surface, *args):
        self._handle_hover()

        if self.clicked:
            color = self.hover_color
        elif self.hovered:
            color = self.hover_color



        if self.state == 1:
            self.color = BLACK
        elif self.state == 0:
            self.color = GRAY


        pygame.draw.rect(surface, self.color, self.rect, width=0)





if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600,600))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Tic Tac Toe Cell")

    """Create the Cells"""
    cell1 = Cell(rect=(100,100,100,100), state=0)
    cell2 = Cell(rect=(200,100,100,100), state=0)
    cell3 = Cell(rect=(100,200,100,100), state=0)
    cell4 = Cell(rect=(200,200,100,100), state=0)
    cells = [cell1, cell2, cell3, cell4]
    cells = []
    for i in range(10):
        for j in range(10):
            cells.append(Cell(rect=(100+i*30,100+j*30,28,28), state=0))

    print(cells)
    """More Pygame Loop"""
    run = True
    """Main Loop"""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            """Call get_event for all cells, --> Board method"""
            for cell in cells:
                cell.get_event(event)
                """Handle click function stuff"""
                if cell.clicked == True and cell.state == 0:
                    cell.state = 1
                elif cell.clicked == True and cell.state == 1:
                    cell.state = 0

        surface.fill((BG_COLOR))
        for CELL in cells:
            CELL.update(surface)
        pygame.display.update()
