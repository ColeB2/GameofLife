from pyVariables import *
from board import Board
from menu import Menu
import pygame



class MainState:
    def __init__(self):
        self.B = Board(width=BOARD_WIDTH, height=BOARD_HEIGHT)

        self.run = True
        self.run_game = False
        self.last_cell_change = None
        self.M = Menu()
        self.button_info = [
            {"rect":(0,0,90,45),
              "text":"Play",
              "function": self.play_button_function,
              "function_args": None},
            {"rect":(90,0,90,45),
              "text":"Pause",
              "function": self.pause_button_function,
              "function_args": None},
            {"rect":(180,0,90,45),
              "text":"Clear",
              "function": self.reset_button_function,
              "function_args": None},
            {"rect":(550,0,90,45),
              "text":"Exploder",
              "function": self.B.load_state,
              "function_args": "exploder.txt"},
            {"rect":(640,0,90,45),
              "text":"SmallExp.",
              "function": self.B.load_state,
              "function_args": "explodersmall.txt"},
            {"rect":(730,0,90,45),
              "text":"Toad",
              "function": self.B.load_state,
              "function_args": "toad.txt"},
            {"rect":(820,0,90,45),
              "text":"Row",
              "function": self.B.load_state,
              "function_args": "row10cell.txt"},
            {"rect":(910,0,90,45),
              "text":"Random",
              "function": self.B.random_state,
              "function_args": None},
        ]
        self.create_buttons()

    def create_buttons(self):
        for button in self.button_info:
            self.M.create_buttons(
                                  button["rect"],
                                  button["text"],
                                  button["function"],
                                  button["function_args"])



    def play_button_function(self, *args):
        self.run_game = True


    def pause_button_function(self, *args):
        self.run_game = False


    def reset_button_function(self, *args):
        self.B.dead_state()


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


    def mouse_controls(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                self.click_change(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                self.motion_change(pygame.mouse.get_pos())


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if not self.run_game:
                self.mouse_controls(event)
            self.M.get_event(event)


    def update(self, surface):
        self.B.update(surface)
        self.M.update(surface, generations=self.B.generation)


    def main_loop(self, surface):
        self.event_loop()
        self.update(surface)
        if self.run_game:
            self.B.next_state()




if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life mainstate")

    game = MainState()
    while game.run:
        surface.fill(BG_COLOR)
        game.main_loop(surface)
        pygame.display.update()